from utils.data_handlers.market_data.finance import FinanceAPI


class CashFlow:
    def __init__(self, name, ticker_name):
        self.name = name
        self.symbol = ticker_name
        self.cash_flow = FinanceAPI.get_cash_flow(ticker_name)
        self.dividends = FinanceAPI.get_dividends(ticker_name)

    # Latest annual free cash flow
    def get_free_cash_flow(self):
        try:
            free_cash_flow = \
                self.cash_flow.iloc[:, 0][self.cash_flow.index == \
                                          'Cash Flow From Continuing Operating Activities'].iloc[0] + \
                self.cash_flow.iloc[:, 0][self.cash_flow.index == \
                                          'Cash Flow From Continuing Investing Activities'].iloc[0]

            return free_cash_flow
        except Exception as e:
            return f"Error: {e}"

    # Cash dividends paid excluding share buybacks
    def get_cash_dividend_paid(self):
        try:
            cash_dividend_paid = \
                self.cash_flow.iloc[:, 0][self.cash_flow.index == \
                                          'Cash Dividends Paid'].iloc[0]

            return -cash_dividend_paid
        except Exception as e:
            return f"Error: {e}"

    # Latest annual dividend per share (or 3y or 5y average)
    def get_annual_dividend_per_share(self):
        try:
            annual_dividend_per_share = self.dividends.iloc[-1]
            return annual_dividend_per_share
        except Exception as e:
            return f"Error: {e}"

    # Dividend growth (I recommend to take 3 to 5y average)
    def get_dividend_growth(self):
        try:
            annual_dividend_Y1 = self.dividends.iloc[-1]
            annual_dividend_Y2 = self.dividends.iloc[-2]
            annual_dividend_Y3 = self.dividends.iloc[-3]
            return ((((annual_dividend_Y2 - annual_dividend_Y3) * 100 / annual_dividend_Y2) + \
                    ((annual_dividend_Y1 - annual_dividend_Y2) * 100 / annual_dividend_Y1)) / 3) / 100
        except Exception as e:
            return f"Error: {e}"

    # Total Issuance of (-) /Payment for Common Stock (+)
    def get_common_stocks_payments(self):
        try:
            common_stocks_payments = \
                self.cash_flow.iloc[:, 0][self.cash_flow.index == \
                                          'Common Stock Payments'].iloc[0]

            return -common_stocks_payments
        except Exception as e:
            return f"Error: {e}"