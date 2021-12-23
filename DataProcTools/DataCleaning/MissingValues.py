import pandas as pd

def height_imputer(dataset, average_height):
    for row in dataset.index:    
        if((dataset['Height'].isna()[row])):        
            NOC_value = dataset['NOC'][row]
            height_per_NOC = average_height.loc[NOC_value, 'Height']
            dataset['Height'].fillna(height_per_NOC, inplace=True)
            
def weight_imputer(dataset, average_weight):
    for row in dataset.index:
        if((dataset['Weight'].isna()[row])):
            NOC_value = dataset['NOC'][row]
            weight_per_NOC = average_weight.loc[NOC_value, 'Weight']
            dataset['Weight'].fillna(weight_per_NOC, inplace=True)    

def age_imputer(dataset, average_age): 
    dataset['Age'].fillna(average_age, inplace=True)

def arbitrary_value_imputer(dataset, column, value):
    dataset[column].fillna(value, inplace=True)

def notes_imputer(noc_df):
    noc_df['notes'].fillna('region_is_noc', inplace=True)

def region_imputer(dataset, imputer, imputing):
    for row in dataset.index:
        if(dataset[imputing].isna()[row]):
            imputer_value = dataset[imputer][row]
            dataset[imputing].fillna(imputer_value, inplace=True)
        
def get_nan_values_percentage(df):
    info = {}
    for col in df:
        numMissingVals = df[col].isna().sum()
        if numMissingVals > 0:
            info[col]=round(
                    100*numMissingVals/df[col].size
                    ,3)

    return info
    

