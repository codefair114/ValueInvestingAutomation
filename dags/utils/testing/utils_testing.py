from utils.models.company_intrinsic_value import CompanyIntrinsicValue
from utils.models.company_profile import CompanyProfile

company = CompanyProfile("Apple", "FDX")

print(company.get_cash_to_market_cap_score())
print(company.get_pe_score())
print(company.get_p_fcf_price_to_free_cash_flow_score())
print(company.get_roe_score())
print(company.get_roic_score())
print(company.get_capital_spread_score())
print(company.get_debt_to_equity_score())
print(company.get_interest_coverage_ratio_score())
print(company.get_cash_to_debt_liabilities_score())
print(company.get_pb_score())
print(company.get_payout_ratio_score())
print(company.get_cash_dividend_yield_score())
print(company.get_total_shareholder_yield_score())
print(company.get_mos_ddm_no_dividend_increase_score())
print(company.get_mos_ddm_with_dividend_increase_score())
print(company.get_mos_ddm_with_dividend_increase_buybacks_score())

print("Final score: ", company.get_final_score())