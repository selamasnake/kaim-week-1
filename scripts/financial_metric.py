from pynance import portfolio_optimizer as po
import pandas as pd

class FinancialMetirc:
    def calculate_financial_metric():

        TICKERS = ["AAPL", "AMZN", "MSFT", "META", "NVDA"]

        # Create the portfolio calculations object
        portfolio = po.PortfolioCalculations(TICKERS)

        print("=== Max Sharpe Portfolio (risk/return) ===")
        print(portfolio.max_sharpe_portfolio("rr"))

        print("\n=== Max Sharpe Portfolio weights ===")
        print(portfolio.max_sharpe_portfolio("df").head())

        print("\n=== Min Variance Portfolio (risk/return) ===")
        print(portfolio.min_var_portfolio("rr"))

        print("\n=== Min Variance Portfolio weights ===")
        print(portfolio.min_var_portfolio("df").head())