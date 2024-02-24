from enum import Enum

from utils.constants.color_levels import ColorLevels
from utils.constants.colors import Color
from utils.models.company_intrinsic_value import CompanyIntrinsicValue

class CompanyProfile:
    def __init__(self, name, ticker_name):
        self.name = name
        self.symbol = ticker_name
        self.company_intrinsic_value = CompanyIntrinsicValue(name, ticker_name)

    # Get Cash to Market cap score
    def get_cash_to_market_cap_score(self):
        value = self.company_intrinsic_value.get_cash_to_market_cap()
        if value >= ColorLevels.CASH_TO_MARKETCAP_GREEN:
            return Color.GREEN.value
        elif value >= ColorLevels.CASH_TO_MARKETCAP_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value >= ColorLevels.CASH_TO_MARKETCAP_YELLOW:
            return Color.YELLOW.value
        elif value >= ColorLevels.CASH_TO_MARKETCAP_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get P/E Price to Earnings score
    def get_pe_score(self):
        value = self.company_intrinsic_value.get_pe()
        if value < ColorLevels.PE_GREEN:
            return Color.GREEN.value
        elif value <= ColorLevels.PE_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value <= ColorLevels.PE_YELLOW:
            return Color.YELLOW.value
        elif value <= ColorLevels.PE_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get P/FCF Price to Free Cash Flow score
    def get_p_fcf_price_to_free_cash_flow_score(self):
        value = self.company_intrinsic_value.get_p_fcf()
        if value < ColorLevels.P_FCF_GREEN:
            return Color.GREEN.value
        elif value <= ColorLevels.P_FCF_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value <= ColorLevels.P_FCF_ORANGE:
            return Color.YELLOW.value
        elif value <= ColorLevels.P_FCF_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get ROE Return on Equity (net income / equity) score
    def get_roe_score(self):
        value = self.company_intrinsic_value.get_roe()
        if value > ColorLevels.ROE_GREEN:
            return Color.GREEN.value
        elif value >= ColorLevels.ROE_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value >= ColorLevels.ROE_YELLOW:
            return Color.YELLOW.value
        elif value >= ColorLevels.ROE_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get ROIC Return on Invested Capital (net income / (equity + financial debt - cash & cash equivalents)) score
    def get_roic_score(self):
        value = self.company_intrinsic_value.get_roic()
        if value > ColorLevels.ROIC_GREEN:
            return Color.GREEN.value
        elif value >= ColorLevels.ROIC_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value >= ColorLevels.ROIC_YELLOW:
            return Color.YELLOW.value
        elif value >= ColorLevels.ROIC_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get Capital spread (ROIC - expected return as shareholder) score
    def get_capital_spread_score(self):
        value = self.company_intrinsic_value.get_capital_spread()
        if value > ColorLevels.CAPITAL_SPREAD_GREEN:
            return Color.GREEN.value
        elif value >= ColorLevels.CAPITAL_SPREAD_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value >= ColorLevels.CAPITAL_SPREAD_YELLOW:
            return Color.YELLOW.value
        elif value >= ColorLevels.CAPITAL_SPREAD_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get # D/E Debt to equity score
    def get_debt_to_equity_score(self):
        value = self.company_intrinsic_value.get_debt_to_equity()
        if value < ColorLevels.DE_GREEN:
            return Color.GREEN.value
        elif value <= ColorLevels.DE_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value <= ColorLevels.DE_YELLOW:
            return Color.YELLOW.value
        elif value <= ColorLevels.DE_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get Interest coverage ratio score
    def get_interest_coverage_ratio_score(self):
        value = self.company_intrinsic_value.get_interest_coverage_ratio()
        if value > ColorLevels.INTEREST_COVERAGE_RATIO_GREEN:
            return Color.GREEN.value
        elif value > ColorLevels.INTEREST_COVERAGE_RATIO_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value >= ColorLevels.INTEREST_COVERAGE_RATIO_YELLOW:
            return Color.YELLOW.value
        elif value >= ColorLevels.INTEREST_COVERAGE_RATIO_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get Cash to Long-term debt/liabilities score
    def get_cash_to_debt_liabilities_score(self):
        value = self.company_intrinsic_value.get_cash_to_debt_liabilities()
        if value > ColorLevels.LIABILITIES_GREEN:
            return Color.GREEN.value
        elif value >= ColorLevels.LIABILITIES_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value >= ColorLevels.LIABILITIES_YELLOW:
            return Color.YELLOW.value
        elif value >= ColorLevels.LIABILITIES_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get P/B Price to Book score
    def get_pb_score(self):
        value = self.company_intrinsic_value.get_pb()
        if value < ColorLevels.PB_GREEN:
            return Color.GREEN.value
        elif value <= ColorLevels.PB_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value <= ColorLevels.PB_YELLOW:
            return Color.YELLOW.value
        elif value <= ColorLevels.PB_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get Payout Ration score
    def get_payout_ratio_score(self):
        value = self.company_intrinsic_value.get_payout_ratio()
        if value > ColorLevels.PAYOUT_RATIO_GREEN and value <= ColorLevels.MAX_PAYOUT_RATIO:
            return Color.GREEN.value
        elif value >= ColorLevels.PAYOUT_RATIO_LIGHT_GREEN and value <= ColorLevels.MAX_PAYOUT_RATIO:
            return Color.LIGHT_GREEN.value
        elif value >= ColorLevels.PAYOUT_RATIO_YELLOW and value <= ColorLevels.MAX_PAYOUT_RATIO:
            return Color.YELLOW.value
        elif value >= ColorLevels.PAYOUT_RATIO_ORANGE and value <= ColorLevels.MAX_PAYOUT_RATIO:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get Cash dividend yield score
    def get_cash_dividend_yield_score(self):
        value = self.company_intrinsic_value.get_cash_dividend_yield()
        if value > ColorLevels.CASH_DIVIDEND_YIELD_GREEN:
            return Color.GREEN.value
        elif value >= ColorLevels.CASH_DIVIDEND_YIELD_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value >= ColorLevels.CASH_DIVIDEND_YIELD_YELLOW:
            return Color.YELLOW.value
        elif value >= ColorLevels.CASH_TO_MARKETCAP_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get Total shareholder yield (cash dividends + share buybacks) score
    def get_total_shareholder_yield_score(self):
        value = self.company_intrinsic_value.get_total_shareholder_yield()
        if value > ColorLevels.TOTAL_SHAREHOLDER_YIELD_GREEN:
            return Color.GREEN.value
        elif value >= ColorLevels.TOTAL_SHAREHOLDER_YIELD_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value >= ColorLevels.TOTAL_SHAREHOLDER_YIELD_YELLOW:
            return Color.YELLOW.value
        elif value >= ColorLevels.TOTAL_SHAREHOLDER_YIELD_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get Margin of safety vs current share price for DDM (dividend yield & no dividend increase) score
    def get_mos_ddm_no_dividend_increase_score(self):
        value = self.company_intrinsic_value.get_mos_ddm_no_dividend_increase()
        if value >= ColorLevels.MARGIN_OF_SAFETY_GREEN:
            return Color.GREEN.value
        elif value >= ColorLevels.MARGIN_OF_SAFETY_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value >= ColorLevels.MARGIN_OF_SAFETY_YELLOW:
            return Color.YELLOW.value
        elif value >= ColorLevels.MARGIN_OF_SAFETY_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    # Get Margin of safety vs current share price for DDM (dividend yield and its growth) score
    def get_mos_ddm_with_dividend_increase_score(self):
        value = self.company_intrinsic_value.get_mos_ddm_with_dividend_increase()
        if value >= ColorLevels.MARGIN_OF_SAFETY_GREEN:
            return Color.GREEN.value
        elif value >= ColorLevels.MARGIN_OF_SAFETY_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value >= ColorLevels.MARGIN_OF_SAFETY_YELLOW:
            return Color.YELLOW.value
        elif value >= ColorLevels.MARGIN_OF_SAFETY_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value
    # Get Margin of safety vs current share price for DDM (dividend yield and its growth) score
    def get_mos_ddm_with_dividend_increase_buybacks_score(self):
        value = self.company_intrinsic_value.get_mos_ddm_with_dividend_increase_buybacks()
        if value >= ColorLevels.MARGIN_OF_SAFETY_GREEN:
            return Color.GREEN.value
        elif value >= ColorLevels.MARGIN_OF_SAFETY_LIGHT_GREEN:
            return Color.LIGHT_GREEN.value
        elif value >= ColorLevels.MARGIN_OF_SAFETY_YELLOW:
            return Color.YELLOW.value
        elif value >= ColorLevels.MARGIN_OF_SAFETY_ORANGE:
            return Color.ORANGE.value
        else:
            return Color.RED.value

    def get_final_score(self):
        scores = [
            self.get_cash_to_market_cap_score(),
            self.get_pe_score(),
            self.get_p_fcf_price_to_free_cash_flow_score(),
            self.get_roe_score(),
            self.get_roic_score(),
            self.get_capital_spread_score(),
            self.get_debt_to_equity_score(),
            self.get_interest_coverage_ratio_score(),
            self.get_cash_to_debt_liabilities_score(),
            self.get_pb_score(),
            self.get_payout_ratio_score(),
            self.get_cash_dividend_yield_score(),
            self.get_total_shareholder_yield_score(),
            self.get_mos_ddm_no_dividend_increase_score(),
            self.get_mos_ddm_with_dividend_increase_score(),
            self.get_mos_ddm_with_dividend_increase_buybacks_score()
        ]
        return sum(scores) * 10 / 60


