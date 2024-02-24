class ColorLevels:
    # Cash to Market cap levels
    CASH_TO_MARKETCAP_GREEN = 0.1
    CASH_TO_MARKETCAP_LIGHT_GREEN = 0.09
    CASH_TO_MARKETCAP_YELLOW = 0.08
    CASH_TO_MARKETCAP_ORANGE = 0.07

    # P/E Price to Earnings levels
    PE_GREEN = 15
    PE_LIGHT_GREEN = 16
    PE_YELLOW = 17
    PE_ORANGE = 18

    # P/FCF Price to Free Cash Flow levels
    P_FCF_GREEN = 15
    P_FCF_LIGHT_GREEN = 16
    P_FCF_YELLOW = 17
    P_FCF_ORANGE = 18

    # ROE Return on Equity (net income / equity) levels
    ROE_GREEN = 0.15
    ROE_LIGHT_GREEN = 0.14
    ROE_YELLOW = 0.13
    ROE_ORANGE = 0.12

    # ROIC Return on Invested Capital (net income / (equity + financial debt - cash & cash equivalents))
    ROIC_GREEN = 0.1
    ROIC_LIGHT_GREEN = 0.09
    ROIC_YELLOW = 0.07
    ROIC_ORANGE = 0.06

    # Capital spread (ROIC - expected return as shareholder)
    CAPITAL_SPREAD_GREEN = 0.02
    CAPITAL_SPREAD_LIGHT_GREEN = 0
    CAPITAL_SPREAD_YELLOW = -0.005
    CAPITAL_SPREAD_ORANGE = -0.01

    # D/E Debt to equity
    DE_GREEN = 1
    DE_LIGHT_GREEN = 1.5
    DE_YELLOW = 2
    DE_ORANGE = 2.5

    # Interest coverage ratio
    INTEREST_COVERAGE_RATIO_GREEN = 8
    INTEREST_COVERAGE_RATIO_LIGHT_GREEN = 5
    INTEREST_COVERAGE_RATIO_YELLOW = 4
    INTEREST_COVERAGE_RATIO_ORANGE = 3.5

    # Cash to Long-term debt/liabilities
    LIABILITIES_GREEN = 0.9
    LIABILITIES_LIGHT_GREEN = 0.8
    LIABILITIES_YELLOW = 0.7
    LIABILITIES_ORANGE = 0.6

    # P/B Price to Book
    PB_GREEN = 3
    PB_LIGHT_GREEN = 3.5
    PB_YELLOW = 4
    PB_ORANGE = 5

    # Payout ratio
    MAX_PAYOUT_RATIO = 0.7
    PAYOUT_RATIO_GREEN = 0.6
    PAYOUT_RATIO_LIGHT_GREEN = 0.5
    PAYOUT_RATIO_YELLOW = 0.3
    PAYOUT_RATIO_ORANGE = 0.2

    # Cash dividend yield
    CASH_DIVIDEND_YIELD_GREEN = 0.06
    CASH_DIVIDEND_YIELD_LIGHT_GREEN = 0.05
    CASH_DIVIDEND_YIELD_YELLOW = 0.03
    CASH_DIVIDEND_YIELD_ORANGE = 0.02

    # Total shareholder yield (cash dividends + share buybacks)
    TOTAL_SHAREHOLDER_YIELD_GREEN = 0.05
    TOTAL_SHAREHOLDER_YIELD_LIGHT_GREEN = 0.04
    TOTAL_SHAREHOLDER_YIELD_YELLOW = 0.03
    TOTAL_SHAREHOLDER_YIELD_ORANGE = 0.02

    # Margin of safety
    MARGIN_OF_SAFETY_GREEN = 0.3
    MARGIN_OF_SAFETY_LIGHT_GREEN = 0.25
    MARGIN_OF_SAFETY_YELLOW = 0.20
    MARGIN_OF_SAFETY_ORANGE = 0.10
