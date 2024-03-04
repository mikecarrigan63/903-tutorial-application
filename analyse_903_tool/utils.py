import pandas as pd

def read_data(filepath):
    # TODO write docstring
    """
    Reads in CSV from filepath and returns dataframe for analysis

    Inputs:
    filepath -> str: path to csv

    Outputs:
    df -> DataFrame: DataFrame for analysis

    """
    df = pd.read_csv(filepath)
    return df

def ingress(df):
    # TODO write docstring
    # TODO convert the birthday colums to datetimes
    df['SEX'] = df['SEX'].map(
        {1:'Male',
         2:'Female'}
    )
    df = df.drop_duplicates('CHILD', keep='first')
    return df

def gender_count(df):
    # TODO docstring
    # TODO write test
    male = len(df[df['SEX'] == 'Male'])
    female = len(df[df['SEX'] == 'Female'])

    return male, female

def child_count(df):
    # TODO docstring
    # TODO write  test
    return len(df['CHILD'].unique())