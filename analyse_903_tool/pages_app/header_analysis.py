# Order of coding
# 1. importing modules
# 2. classes (if using)
# 3. user defined functions
# 4. code

import pandas as pd
import streamlit as st
import numpy as np
import json
import plotly.express as px
from datetime import datetime

def ingress(df):
    # TODO write docstring
    # TODO convert the birthday colums to datetimes
    # TODO take birthday column fromtoday's datetime to get age
    # convert/round the age to a whole number of years
    df['SEX'] = df['SEX'].map(
        {1:'Male',
         2:'Female'}
    )
    df = df.drop_duplicates('CHILD', keep='first')
    # convert birthday to datetime with force blank DOB to NaN etc.
    df['DOB'] = pd.to_datetime(df['DOB'], format="%d/%m/%Y", errors='coerce')

    # version using Datetime module
    #df['Age'] = df['DOB'].apply(lambda x: (datetime.today() - x).days // 365)

    # alternative version
    df['AGE'] = pd.to_datetime('today').normalize() - df['DOB']
    df['AGE'] = (df['AGE'] / np.timedelta64(1, 'Y')).astype('int')


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

st.title('903 Header Analysis App')

upload = st.file_uploader("Upload 903 header file")

if upload:
    df = pd.read_csv(upload)

    with st.sidebar:
        ethnicities = st.sidebar.multiselect(
            'Select ethnicities for analysis',
            df['ETHNIC'].unique(),
            default=df['ETHNIC'].unique(),
        )

    df = df[df['ETHNIC'].isin(ethnicities)]
    
    df = ingress(df)
    
    child_pop = child_count(df)
    male, female = gender_count(df)
    average_age = round(df['AGE'].mean())

    st.write(f'The total population of children is: {child_pop}')
    st.write(f'The total number of males is: {male}')
    st.write(f'The total number of females is: {female}')
    st.write(f'The average age of all children is: {average_age}')

    gender_bar = px.bar(df, 
                        x='SEX',
                        title = 'Number of children in 903 by gender',
                        labels =   {'SEX':'Sex',
                                    'count':'No. of children'}
                        )
    ethnicity_bar = px.bar(df, 
                        x='ETHNIC',
                        title = 'Number of children in 903 by ethnicity',
                        labels =   {'ETHNIC':'Ethnicity',
                                    'count':'No. of children'}
                        )
    age_hist = px.histogram(df['AGE'],
                        labels={'value':'Age','count':'Number of children'},
                        title = 'Spread of ages of children in 903 by age',
                        )
    
    st.plotly_chart(gender_bar)
    st.plotly_chart(ethnicity_bar)
    st.plotly_chart(age_hist)

    st.dataframe(df)

    
