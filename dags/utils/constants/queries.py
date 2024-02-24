import os

class QUERIES:
    INSERT_SEC_DATA = "INSERT INTO listed_companies (cik_str, ticker, company_name) VALUES (%s, %s, %s);"
    DETELE_SEC_DATA = "TRUNCATE TABLE listed_companies;"
    SELECT_SEC_DATA = "SELECT ticker FROM listed_companies;"
    INSERT_SCORES = """
            INSERT INTO company_scores (
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
            ) VALUES (
                %s, -- cash_to_market_cap_score
                %s, -- pe_score
                %s, -- p_fcf_price_to_free_cash_flow_score
                %s, -- roe_score
                %s, -- roic_score
                %s, -- capital_spread_score
                %s, -- debt_to_equity_score
                %s, -- interest_coverage_ratio_score
                %s, -- cash_to_debt_liabilities_score
                %s, -- pb_score
                %s, -- payout_ratio_score
                %s, -- cash_dividend_yield_score
                %s, -- total_shareholder_yield_score
                %s, -- mos_ddm_no_dividend_increase_score
                %s, -- mos_ddm_with_dividend_increase_score
                %s, -- mos_ddm_with_dividend_increase_buybacks_score
                %s, -- final_score
                %s -- ticker
            );
    """
    UPDATE_SCORES = """
            UPDATE company_scores
            SET cash_to_market_cap_score = %s,
                pe_score = %s,
                p_fcf_price_to_free_cash_flow_score = %s,
                roe_score = %s,
                roic_score = %s,
                capital_spread_score = %s,
                debt_to_equity_score = %s,
                interest_coverage_ratio_score = %s,
                cash_to_debt_liabilities_score = %s,
                pb_score = %s,
                payout_ratio_score = %s,
                cash_dividend_yield_score = %s,
                total_shareholder_yield_score = %s,
                mos_ddm_no_dividend_increase_score = %s,
                mos_ddm_with_dividend_increase_score = %s,
                mos_ddm_with_dividend_increase_buybacks_score = %s,
                final_score = %s
            WHERE ticker = %s;
        """
