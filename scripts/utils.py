import pandas as pd 


def load_data(filepath):
    """
        Load CSV from local filepath.
    """
    pd.set_option('display.max_columns', 15)
    data = pd.read_csv(filepath)
    return data


class DataPreprocessor: 
    """
    Class for exploring and preprocessing data.
    """
    def explore_data(data):
        print("Shape of the data:", data.shape)
        print("Info of the data:", data.info())

    def check_null_values(data):
        """
        Return the number of missing values per column.
        """
        return data.isnull().sum()
        

    def convert_date_dtype(data):
        """
        Convert 'date' column from object to datetime type.
        """
        data['date'] = pd.to_datetime(data['date'], format="mixed", utc=True)
        print("Converted 'date' dtype:", data['date'].dtype)

        return data
    

    def drop_unnamed_column(data):
        """
        Drop 'Unnamed: 0' column.
        """
        data = data.drop(columns=['Unnamed: 0'])
        return data

