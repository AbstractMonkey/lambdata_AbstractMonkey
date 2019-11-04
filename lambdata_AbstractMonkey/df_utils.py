import pandas as pd
import numpy as np

def break_out_datetime(df, column):
     # Convert dates to pd.datetime format and break them out into days, months, and years
     df[column] = pd.to_datetime(df[column])
     df['day'] = df[column].dt.day
     df['month'] = df[column].dt.month
     df['year'] = df[column].dt.year
     return df
     
def calc_precision(corr_neg_preds, total_neg_preds):     
     # Precision = Correct value predictions of a class / Total predictions for class
     precision = corr_neg_preds / total_neg_preds
     return precision
