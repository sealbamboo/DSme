
#----------------------------------------------
# Numerics columns
#----------------------------------------------
def get_numberics(df):
    return df._get_numeric_data()


#----------------------------------------------
# Non-numerrics columns
#----------------------------------------------
def get_categorical(df):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    
    return df.select_dtypes(exclude=numerics)


#----------------------------------------------
# Selected custom columns
#----------------------------------------------
def get_custom_col(df, list):
    return df[list].copy()