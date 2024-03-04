import pytest
import pandas as pd

from analyse_903_tool.utils import ingress

def test_ingress():
    df = pd.DataFrame([{'SEX':1},
                       {'SEX':2}])
    output_df = ingress(df)

    male = len(output_df[output_df['SEX'] == 'Male'])
    female = len(output_df[output_df['SEX'] == 'Female'])

    assert male == 1
    assert female == 1
