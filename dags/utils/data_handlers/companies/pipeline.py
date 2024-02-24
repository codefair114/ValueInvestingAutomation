import pandas as pd
import requests
import psycopg2

from utils.constants.db import INVESTING_DB
from utils.constants.queries import QUERIES
from utils.models.company_profile import CompanyProfile
# Function to check if the ticker exists in the table
def ticker_exists(cursor, ticker):
    query = "SELECT EXISTS(SELECT 1 FROM public.company_scores WHERE ticker = %s)"
    cursor.execute(query, (ticker,))
    return cursor.fetchone()[0]

class IntrinsicValueDataPipeline:

    # Function to fetch tickers from the database
    @staticmethod
    def fetch_tickers():
        conn = psycopg2.connect(
            dbname=INVESTING_DB.PG_DB_NAME,
            user=INVESTING_DB.PG_DB_USER,
            password=INVESTING_DB.PG_DB_PASS,
            host=INVESTING_DB.PG_DB_HOST,
            port=INVESTING_DB.PG_DB_PORT
        )
        cursor = conn.cursor()

        cursor.execute(QUERIES.SELECT_SEC_DATA)
        tickers = [row[0] for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        return tickers

    # Function to calculate scores for a single ticker
    @staticmethod
    def calculate_scores(ticker):
        # Connect to the database
        conn = psycopg2.connect(
            dbname=INVESTING_DB.PG_DB_NAME,
            user=INVESTING_DB.PG_DB_USER,
            password=INVESTING_DB.PG_DB_PASS,
            host=INVESTING_DB.PG_DB_HOST,
            port=INVESTING_DB.PG_DB_PORT
        )
        cursor = conn.cursor()

        # Instantiate CompanyProfile with the ticker
        company = CompanyProfile(ticker, ticker)

        # Calculate scores using the provided functions
        cash_to_market_cap_score = company.get_cash_to_market_cap_score()
        pe_score = company.get_pe_score()
        p_fcf_price_to_free_cash_flow_score = company.get_p_fcf_price_to_free_cash_flow_score()
        roe_score = company.get_roe_score()
        roic_score = company.get_roic_score()
        capital_spread_score = company.get_capital_spread_score()
        debt_to_equity_score = company.get_debt_to_equity_score()
        interest_coverage_ratio_score = company.get_interest_coverage_ratio_score()
        cash_to_debt_liabilities_score = company.get_cash_to_debt_liabilities_score()
        pb_score = company.get_pb_score()
        payout_ratio_score = company.get_payout_ratio_score()
        cash_dividend_yield_score = company.get_cash_dividend_yield_score()
        total_shareholder_yield_score = company.get_total_shareholder_yield_score()
        mos_ddm_no_dividend_increase_score = company.get_mos_ddm_no_dividend_increase_score()
        mos_ddm_with_dividend_increase_score = company.get_mos_ddm_with_dividend_increase_score()
        mos_ddm_with_dividend_increase_buybacks_score = company.get_mos_ddm_with_dividend_increase_buybacks_score()
        final_score = company.get_final_score()
        query = QUERIES.INSERT_SCORES if ticker_exists(cursor, ticker) is False else QUERIES.UPDATE_SCORES

        cursor.execute(query, (
            cash_to_market_cap_score,
            pe_score,
            p_fcf_price_to_free_cash_flow_score,
            roe_score,
            roic_score,
            capital_spread_score,
            debt_to_equity_score,
            interest_coverage_ratio_score,
            cash_to_debt_liabilities_score,
            pb_score,
            payout_ratio_score,
            cash_dividend_yield_score,
            total_shareholder_yield_score,
            mos_ddm_no_dividend_increase_score,
            mos_ddm_with_dividend_increase_score,
            mos_ddm_with_dividend_increase_buybacks_score,
            final_score,
            ticker
        ))
        conn.commit()

        # Close database connection
        cursor.close()
        conn.close()