import pandas as pd 

class PublisherAnalysis:

    def get_publisher_counts(data, top_n=10):
        """
        Return counts of articles per publisher.
        """
        publisher_counts = data['publisher'].value_counts()
        print(f"\nTop {top_n} publishers:\n", publisher_counts.head(top_n))
        # return publisher_counts

    def get_publisher_sentiment_distribution(data, top_n=10):
        """
        Show sentiment distribution per publisher.
        Requires a 'sentiment' column.
        """
        if 'sentiment' not in data.columns:
            print("No 'sentiment' column found. Run sentiment analysis first.")
            return None

        sentiment_dist = (data.groupby('publisher')['sentiment'].value_counts(normalize=True).unstack().fillna(0))

        print(f"\nSentiment distribution for top {top_n} publishers:")
        sentiment_dist.head(top_n)

        return sentiment_dist
    
    def extract_publisher_domains(data):
        """
        Adds a 'publisher_domain' column if publisher contains an email address.
        """
        data['publisher_domain'] = data['publisher'].apply(
            lambda x: x.split('@')[1].lower() if isinstance(x, str) and '@' in x else None
        )

        domain_counts = data['publisher_domain'].value_counts()
        print("\nTop email domains:\n", domain_counts.head(10))


