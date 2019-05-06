from mine import get_renovate_able_list, turn_renovated_qc_into_num

#----------------------------------------------
# GET Numerics columns
#----------------------------------------------
def get_numberics(df):
    return df._get_numeric_data()


#----------------------------------------------
# GET Non-numerrics columns
#----------------------------------------------
def get_categorical(df):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    
    return df.select_dtypes(exclude=numerics)


#----------------------------------------------
# Selected custom columns
#----------------------------------------------
def get_custom_col(df, list):
    return df[list].copy()


#----------------------------------------------
## STATIC
# Renovate-able DATAFRAME
#----------------------------------------------
def build_renovate_df(df_name):

    ### RELY ON "mine.py"
    ## Initialize the renovated list
    list_reno_able = get_renovate_able_list(df_name)

    # # Add "Neighborhood" column from "list_non_renovated"
    # list_reno_able.append(list_non_renovated[0])

    ### RELY on "m_df.py"
    df_renovate = get_custom_col(df_name,list_reno_able)

    # Fill "NaN" with "0"
    df_renovate.fillna('NA',inplace=True)

    ## Turn Qual/Cond columns into number
    ### RELY on "mine.py"
    turn_renovated_qc_into_num(df_renovate)

    ## Drop this list from "df_name" DataFrame
    df_name.drop(labels=list_reno_able, axis=1, inplace=True)

    return df_renovate



#----------------------------------------------
## STATIC
# Convertable DATAFRAME
#----------------------------------------------
def build_convertable_df(df_name):
    ## Initialize List
    list_convertable = ['CentralAir','PavedDrive','BsmtExposure','GarageFinish',
                        'LotShape', 'Street', 'Alley','LandContour','Utilities',
                        'LandSlope','Fence']
    df_convertable = df_name[list_convertable].copy()

    # Fill "NaN" with "NA"
    df_convertable.fillna('NA',inplace=True)

    # CentralAir (Y,N) to numberic
    # PavedDrive (Y,P,N) to numberic
    exchange_convertable_list(df_convertable)

    ## Drop this list from "df_name" DataFrame
    df_name.drop(labels=list_convertable, axis=1, inplace=True)

    return df_convertable

    


#----------------------------------------------
## STATIC
# Pre-2010 DATAFRAME
#----------------------------------------------
def build_pre_2010_df(df):
    return df.loc[df['YrSold'] < 2010]



#----------------------------------------------
## STATIC
# Post-2010 DATAFRAME
#----------------------------------------------
def build_post_2010_df(df):
    return df.loc[df['YrSold'] == 2010]



#----------------------------------------------
## STATIC
# Combine "renovate" and "convertable" DATAFRAME
#----------------------------------------------
def m_build_df(df_target):
    # ARE renovate-able:
    # - Roof and exterior features
    # - "Quality" metrics, such as kitchen quality
    # - "Condition" metrics, such as condition of garage
    # - Heating and electrical components
    # ----------------------------------------------------
    df_renovate = build_renovate_df(df_target)

    # Build-in "Convertable" Dataframe
    df_convertable = build_convertable_df(df_target)

    return df_renovate, df_convertable