import pandas as pd



def get_nan_values_percentage(df):
    info = {}
    for col in df:
        numMissingVals = df[col].isna().sum()
        if numMissingVals > 0:
            info[col]=round(
                    100*numMissingVals/df[col].size
                    ,3)

    return info
    

