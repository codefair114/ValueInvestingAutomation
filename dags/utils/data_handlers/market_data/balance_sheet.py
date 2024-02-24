import yfinance as yf

from utils.data_handlers.market_data.finance import FinanceAPI
class BalanceSheet:
    def __init__(self, name, ticker_name):
        self.name = name
        self.symbol = ticker_name
        self.balance_sheet = FinanceAPI.get_balance_sheet(ticker_name)

    # Equity Attributable to Parent Stockholders
    def get_stockholders_equity(self):
        try:
            total_revenue = \
                self.balance_sheet.iloc[:, 0][self.balance_sheet.index == \
                                                         'Stockholders Equity'].iloc[0]

            return total_revenue
        except Exception as e:
            return f"Error: {e}"

    # Number of outstanding shares
    def get_number_of_shares(self):
        try:
            ticker = yf.Ticker(self.symbol)
            outstanding_shares = ticker.info['sharesOutstanding']
            return outstanding_shares
        except Exception as e:
            return f"Error: {e}"

    # Cash & cash equivalents
    def get_cash_equivalents(self):
        try:
            cash_equivalents = \
                self.balance_sheet.iloc[:, 0][self.balance_sheet.index == \
                                                         'Cash And Cash Equivalents'].iloc[0]

            return cash_equivalents
        except Exception as e:
            return f"Error: {e}"

    # Financing liabilities long-term/non-current
    def get_financial_liabilities_non_current(self):
        try:
            # Calculate Long-term Financing Liabilities
            long_term_debt = \
                self.balance_sheet.iloc[:, 0][self.balance_sheet.index == \
                                                         'Long Term Debt'].iloc[0] \
                    if 'Long Term Debt' in self.balance_sheet.index else 0

            long_term_debt_capital_lease_obligation = \
                self.balance_sheet.iloc[:, 0][self.balance_sheet.index == \
                                                         'Long Term Debt And Capital Lease Obligation'].iloc[0] \
                    if 'Long Term Debt And Capital Lease Obligation' in self.balance_sheet.index \
                    else 0

            return long_term_debt + long_term_debt_capital_lease_obligation
        except Exception as e:
            return f"Error: {e}"

    # Intangible assets (trademarks, patents, IP, …) excluding Goodwill
    def get_intangible_assets(self):
        try:
            # Calculate all intangible assets
            intangible_assets = \
                self.balance_sheet.iloc[:, 0][self.balance_sheet.index == \
                                                         'Other Intangible Assets'].iloc[0] \
                    if 'Other Intangible Assets' in self.balance_sheet.index else 0
            # Calculate Goodwill
            goodwill = \
                self.balance_sheet.iloc[:, 0][self.balance_sheet.index == \
                                                         'Goodwill'].iloc[0] \
                    if 'Goodwill' in self.balance_sheet.index else 0

            return intangible_assets - goodwill
        except Exception as e:
            return f"Error: {e}"

    # Get/estimate brand value
    def get_brand_value(self):
        # Calculate all intangible assets / 2 as brand value
        return self.balance_sheet.iloc[:, 0][self.balance_sheet.index == \
                                      'Other Intangible Assets'].iloc[0] * 0.5 \
            if 'Other Intangible Assets' in self.balance_sheet.index else 0