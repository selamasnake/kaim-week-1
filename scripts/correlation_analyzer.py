class CorrelationAnalysis:
    def sentiment_correlation_analysis(data):
        """
        Compute correlation between sentiment and stock metrics.
        """
        # Correlation with daily returns
        corr_returns = data['sentiment_score'].corr(data['daily_returns'])
        print(f'Correlation between {'sentiment_score'} and {'daily_returns'} is {corr_returns:.4f}')
        
        # Correlation with closing prices
        corr_close = data['sentiment_score'].corr(data['close'])
        print(f'Correlation between {'sentiment_score'} and {'close'} is {corr_close:.4f}')

        return corr_returns, corr_close