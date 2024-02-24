import time

import yfinance as yf


class FinanceAPI:

    @staticmethod
    def get_financials(ticker_name):
        ticker = yf.Ticker(ticker_name)
        financials = ticker.financials
        financials.rename(columns={financials.columns[0]: financials.columns[0].year}, inplace=True)
        financials.rename(columns={financials.columns[1]: financials.columns[1].year}, inplace=True)
        financials.rename(columns={financials.columns[2]: financials.columns[2].year}, inplace=True)
        return financials

    @staticmethod
    def get_balance_sheet(ticker_name):
        ticker = yf.Ticker(ticker_name)
        bs = ticker.balance_sheet
        bs.rename(columns={bs.columns[0]: bs.columns[0].year}, inplace=True)
        bs.rename(columns={bs.columns[1]: bs.columns[1].year}, inplace=True)
        bs.rename(columns={bs.columns[2]: bs.columns[2].year}, inplace=True)
        return bs

    @staticmethod
    def get_dividends(ticker_name):
        ticker = yf.Ticker(ticker_name)
        dividends = ticker.dividends
        # Assuming dividends are provided on a quarterly basis, summing them to get annual dividends
        annual_dividends = dividends.groupby(dividends.index.year).sum()
        return annual_dividends

    @staticmethod
    def get_cash_flow(ticker_name):
        ticker = yf.Ticker(ticker_name)
        cash_flow = ticker.cash_flow
        cash_flow.rename(columns={cash_flow.columns[0]: cash_flow.columns[0].year}, inplace=True)
        cash_flow.rename(columns={cash_flow.columns[1]: cash_flow.columns[1].year}, inplace=True)
        cash_flow.rename(columns={cash_flow.columns[2]: cash_flow.columns[2].year}, inplace=True)
        return cash_flow
