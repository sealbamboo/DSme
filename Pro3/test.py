import pandas as pd

def test_print():
    return "Hello World"

def mean(list):
    return np.mean(list)

def merge_columns_to_one(df,list_added_columns, new_column_name):
    
    df_result = pd.DataFrame()
    df_temp = df[list_added_columns]
    df_result[str(new_column_name)] = df_temp.sum(axis=1)
    
    return df_result

#---------------------------------------------------------------------
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

#---------------------------------------------------------------------
# This function does a pairplot across your variables with the color
# set as the outcome "malignant" class variable
def bcw_pairplotter(df, variables, sample_frac=0.3):
    # sample_frac lets you specify an amount of the data to sample for the plot.
    # this speeds up the function which can take awhile with the full data.
    
    # get the number of rows/data points:
    rows = df.shape[0]
    
    # get downsample indicies for the data, if specified
    if sample_frac < 1.0:
        sample_inds = np.random.choice(list(range(0,rows)), 
                                       size=int(round(rows*sample_frac)), 
                                       replace=False).astype(int)
    
    # make the pairplot for the variables:
    pairs = sns.pairplot(df.iloc[sample_inds, :], 
                         vars=variables, 
                         hue="malignant", 
                         palette=sns.xkcd_palette(['windows blue', 'amber']))

#---------------------------------------------------------------------
# Count frequency of value in list
from itertools import groupby
[len(list(group)) for key, group in groupby(a)]
