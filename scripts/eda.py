import pandas as pd 


class EDA:
    """
    Class for exploratory data analysis.
    """

    def get_headline_stats(data):
        """
        Desriptive statistics for the headline column and 
        calculate max, min, average headline lengths.
        """
        headline_stats = data['headline'].describe()
        print (headline_stats, "\n")

        data['headline_length'] = data['headline'].apply(len)  

        average_length = data['headline_length'].mode()[0]
        print(f"Average Headline Length: {average_length}")

        max_length = data['headline_length'].max()
        print(f"Max Headline Length: {max_length}")

        min_length = data['headline_length'].min()
        print(f"Min Headline Length: {min_length}")

        length_range = max_length - min_length
        print(f"Headline Length Range: {length_range}")

        
        
    def articles_per_publisher(data):
        """
        Count the number of articles published by each publisher.
        """
        popular_publishers = data.groupby('publisher').size().sort_values(ascending=False)  
        return popular_publishers
    
    
    
    def analyze_publication_trends(data):
        """
        Analyze  publication counts by day, month, and year.
        """
        publications_by_day = data['date'].dt.to_period('D').value_counts().sort_index()
        publications_by_month = data['date'].dt.to_period('M').value_counts().sort_index()
        publications_by_year = data['date'].dt.to_period('Y').value_counts().sort_index()

        return publications_by_day, publications_by_month, publications_by_year
    
    def analyze_publication_time(data):
        """
        Analyze publications by the hour of the day.
        """
        data['publication_hour'] = data['date'].dt.hour  # Extract hour from datetime
        publications_by_hour = data.groupby('publication_hour').size()
        return publications_by_hour
    
