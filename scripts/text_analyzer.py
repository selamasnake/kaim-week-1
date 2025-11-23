import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy
from gensim import corpora
from gensim.models import LdaModel
import pyLDAvis.gensim_models

# Load the small English model once
nlp = spacy.load("en_core_web_sm")

class TextAnalyzer:
    """
    Class for headline sentiment and topic Modeling
    """

    def analyze_headline_sentiment(data):
        """
        Perform sentiment analysis on the 'headline' column using VADER.
        Adds 'sentiment_score' and 'sentiment' columns to the dataframe.
        """
        analyzer = SentimentIntensityAnalyzer()

        def classify_sentiment(compound_score):
            if compound_score >= 0.05:
                return 'positive'
            elif compound_score <= -0.05:
                return 'negative'
            else:
                return 'neutral'

        data['sentiment_score'] = data['headline'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
        data['sentiment'] = data['sentiment_score'].apply(classify_sentiment)

        return data


    def preprocess_text_spacy(data, batch_size=1000, n_process=-1):
        """
        Preprocess headlines using SpaCy: lowercase, lemmatize, remove stopwords and punctuation.
        Adds a new column 'processed_headline'.

        Parameters:
        - data: pandas DataFrame with 'headline' column
        - batch_size: number of documents to process in a batch
        - n_process: number of parallel processes (-1 uses all cores)
        """
        processed_headlines = []

        # Use nlp.pipe for faster batch processing
        for doc in nlp.pipe(data['headline'].str.lower(), batch_size=batch_size, n_process=n_process):
            # Lemmatize and remove stopwords and punctuation
            lemmatized_headline = ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
            processed_headlines.append(lemmatized_headline)

        data['processed_headline'] = processed_headlines
        return data


    def apply_lda(data, num_topics=10):
        """
        Perform LDA topic modeling on preprocessed headlines.
        Prints top 5 words per topic and displays an interactive PyLDAvis visualization.

        Parameters:
        - data: pandas DataFrame with 'processed_headline' column
        - num_topics: number of LDA topics to extract

        Returns:
        - lda_model: trained LdaModel object
        - topics: list of topic strings
        - dictionary: gensim Dictionary object
        """
        processed_headline = data['processed_headline'].apply(lambda x: x.split())
        dictionary = corpora.Dictionary(processed_headline)

        # Create the corpus (bag-of-words representation)
        corpus = [dictionary.doc2bow(text) for text in processed_headline]


        # Train the LDA model using the corpus and dictionary
        lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)
        topics = lda_model.print_topics(num_words=5)

        print("LDA Topics:")
        for topic in topics:
            print(topic)

        pyLDAvis.enable_notebook(local=True)
        vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
        pyLDAvis.display(vis)

        return lda_model, topics, dictionary
