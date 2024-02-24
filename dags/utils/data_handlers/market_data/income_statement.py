from utils.data_handlers.market_data.finance import FinanceAPI

class IncomeStatement:
    def __init__(self, name, ticker_name):
        self.name = name
        self.symbol = ticker_name
        self.financials = FinanceAPI.get_financials(ticker_name)

    # Latest annual revenue/gross income
    def get_total_revenue(self):
        try:
            total_revenue = \
                self.financials.iloc[:, 0][self.financials.index == \
                                                         'Total Revenue'].iloc[0]

            return total_revenue
        except Exception as e:
            return f"Error: {e}"

    # Latest annual net income/income after taxes
    def get_net_income(self):
        try:
            net_income = \
                self.financials.iloc[:, 0][self.financials.index == \
                                                         'Net Income'].iloc[0]

            return net_income
        except Exception as e:
            return f"Error: {e}"

    # Interest expense
    def get_net_interest_income(self):
        try:
            net_interest_income = \
                self.financials.iloc[:, 0][self.financials.index == \
                                                         'Net Interest Income'].iloc[0]

            return -net_interest_income
        except Exception as e:
            return f"Error: {e}"