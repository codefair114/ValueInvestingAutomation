import yfinance as yf

from utils.data_handlers.market_data.balance_sheet import BalanceSheet
from utils.data_handlers.market_data.cash_flow import CashFlow
from utils.data_handlers.market_data.income_statement import IncomeStatement

class CompanyIntrinsicValue:
    def __init__(self, name, ticker_name, expected_returns = 0.09):
        self.name = name
        self.symbol = ticker_name
        self.ticker = yf.Ticker(ticker_name)
        self.current_price = self.ticker.history(period='1d')['Close'].iloc[-1]
        self.balance_sheet = BalanceSheet(name, ticker_name)
        self.income_statement = IncomeStatement(name, ticker_name)
        self.cash_flow = CashFlow(name, ticker_name)
        # Expected return as shareholder / your cost of capital
        self.expected_returns = expected_returns

    ''' Blue chip indicators '''
    # Market cap of the company
    def get_market_cap(self):
        try:
            return self.ticker.info.get('marketCap', 'Not Available')
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1
    # Cash / Market cap
    def get_cash_to_market_cap(self):
        try:
            return self.balance_sheet.get_cash_equivalents() / self.get_market_cap()
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1
    ''' Price multiple indicators '''
    # P/E Price to Earnings
    def get_pe(self):
        try:
            return self.income_statement.get_net_income() / self.balance_sheet.get_number_of_shares()
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1
    # P/FCF Price to Free Cash Flow
    def get_p_fcf(self):
        try:
            return self.current_price / \
                (self.cash_flow.get_free_cash_flow() / self.balance_sheet.get_number_of_shares())
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1
    ''' Profitability indicators '''
    # ROE Return on Equity (net income / equity)
    def get_roe(self):
        try:
            return self.income_statement.get_net_income() / self.balance_sheet.get_stockholders_equity()
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1
    # ROIC Return on Invested Capital (net income / (equity + financial debt - cash & cash equivalents))
    def get_roic(self):
        try:
            return self.income_statement.get_net_income() / \
                (self.balance_sheet.get_financial_liabilities_non_current() + \
                 self.balance_sheet.get_stockholders_equity() - \
                 self.balance_sheet.get_cash_equivalents() \
                )
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1

    # Capital spread (ROIC - expected return as shareholder)
    def get_capital_spread(self):
        try:
            return self.get_roic() - self.expected_returns
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1

    ''' Risk indicators '''
    # D/E Debt to equity
    def get_debt_to_equity(self):
        try:
            return self.balance_sheet.get_financial_liabilities_non_current() / \
                self.balance_sheet.get_stockholders_equity()
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1

    # Interest coverage ratio
    def get_interest_coverage_ratio(self):
        try:
            return self.income_statement.get_net_income() / \
                self.income_statement.get_net_interest_income()
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1
    # Cash to Long-term debt/liabilities
    def get_cash_to_debt_liabilities(self):
        try:
            return self.balance_sheet.get_cash_equivalents() / \
                self.balance_sheet.get_financial_liabilities_non_current()
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1

    ''' Book value indicators '''
    # Book value per share
    def get_book_value_per_share(self):
        try:
            return self.balance_sheet.get_stockholders_equity() / \
                self.balance_sheet.get_number_of_shares()
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1

    # P/B Price to Book
    def get_pb(self):
        try:
            return self.current_price / self.get_book_value_per_share()
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1

    ''' Dividends and buybacks indicators '''
    # Payout ratio
    def get_payout_ratio(self):
        try:
            return self.cash_flow.get_cash_dividend_paid() / \
                self.income_statement.get_net_income()
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1

    # Cash dividend yield
    def get_cash_dividend_yield(self):
        try:
            return self.cash_flow.get_annual_dividend_per_share() / self.current_price
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1
    # Share buyback dividend (in absolute currency per share)
    def get_share_buyback_dividend(self):
        try:
            return self.cash_flow.get_common_stocks_payments() / \
                self.balance_sheet.get_number_of_shares()
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1

    # Total shareholder yield (cash dividends + share buybacks)
    def get_total_shareholder_yield(self):
        try:
            return (self.cash_flow.get_annual_dividend_per_share() + \
                    self.get_share_buyback_dividend()) / self.current_price
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1

    ''' Intrinsic value dividends method '''

    # Intrinsic value per share for DDM (dividend yield & no dividend increase)
    def get_value_ddm_no_dividend_increase(self):
        try:
            return self.cash_flow.get_annual_dividend_per_share() / self.expected_returns
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1
    # Margin of safety vs current share price for DDM (dividend yield & no dividend increase)
    def get_mos_ddm_no_dividend_increase(self):
        try:
            return (self.get_value_ddm_no_dividend_increase() - self.current_price) / self.current_price
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1
    # Intrinsic value per share for DDM (dividend yield and its growth)
    def get_value_ddm_with_dividend_increase(self):
        try:
            return self.cash_flow.get_annual_dividend_per_share() / \
                (self.expected_returns - self.cash_flow.get_dividend_growth())
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1
    # Margin of safety vs current share price for DDM (dividend yield and its growth)
    def get_mos_ddm_with_dividend_increase(self):
        try:
            return (self.get_value_ddm_with_dividend_increase() - self.current_price) / self.current_price
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1
    # Intrinsic value per share for DDM (dividend yield, its growth and yield brought by buybacks)
    def get_value_ddm_with_dividend_increase_buybacks(self):
        try:
            return (self.cash_flow.get_annual_dividend_per_share() + self.get_share_buyback_dividend()) / \
                (self.expected_returns - self.cash_flow.get_dividend_growth())
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1
    # Margin of safety vs current share price for DDM (dividend yield and its growth)
    def get_mos_ddm_with_dividend_increase_buybacks(self):
        try:
            return (self.get_value_ddm_with_dividend_increase_buybacks() - self.current_price) / \
                self.current_price
        except TypeError as e:
            # Handle the TypeError gracefully
            print("Error:", e)
            # You can choose to return a default value or None
            return -1