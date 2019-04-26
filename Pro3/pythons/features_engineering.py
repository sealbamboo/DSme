from plotting import correlation_heat_map, m_pair_plot, m_box_plot
from split_df import get_categorical, get_numberics

def feature_dataframe(df_target):

    #----------------------------------------------
    # __Init__ DataFrames
    #----------------------------------------------
    df_result = pd.DataFrame()
    df_numerics = get_numberics(df_target)
    df_name = get_categorical(df_target)


    #----------------------------------------------
    #### Numberics Dataframe
    #----------------------------------------------
    # Fill NAN value with 0
    df_numerics = df_numerics.fillna(0)

    # Merge Bathrooms columns into Bathrooms
    list_bathrooms = ['BsmtFullBath', 'BsmtHalfBath', 'FullBath','HalfBath']
    df_temp = df_numerics[list_bathrooms].copy()
    df_numerics['Bathrooms'] = df_temp.sum(axis=1)
    df_numerics.drop(labels=list_bathrooms, axis=1,inplace=True)

    # Inspect the Basement's Square Feet
    list_Basements = ['BsmtFinSF1','BsmtFinSF2','BsmtUnfSF','TotalBsmtSF']
    df_temp = df_numerics[list_Basements].copy()
    df_temp['Sum3'] = df_temp[list_Basements[:3]].sum(axis=1) > df_temp[list_Basements[3]]
    df_numerics.drop(labels=list_Basements[:3],axis=1,inplace=True)

    # Inspect 'GrLivArea'
    list_Livingspace =['1stFlrSF','2ndFlrSF','LowQualFinSF','GrLivArea']
    df_temp = df_numerics[list_Livingspace].copy()
    df_temp['isTotal'] = df_temp[list_Livingspace[0:3]].sum(axis=1) == df_temp[list_Livingspace[3]]
    df_numerics.drop(labels=list_Livingspace[0:3],axis=1,inplace=True)

    # Inspect "Porch"
    list_Porchs = ['OpenPorchSF','EnclosedPorch','3SsnPorch','ScreenPorch']
    df_temp = df_numerics[list_Porchs].copy()
    df_numerics.drop(labels=list_Porchs, axis=1, inplace=True)
    df_numerics['PorchSF'] = df_temp.sum(axis=1)

    # Create Heatmap to see the correlations
    # correlation_heat_map(df_numerics)
    # plt.subplots(figsize=(30,30))


    # ViZz
    df_temp = df_numerics.copy()
    df_temp.drop(labels='SalePrice',axis=1, inplace=True)

    m_pair_plot(df_temp)
    m_box_plot(df_temp)

    # Half-heatmap display
    correlation_heat_map(df_numerics)
    # sns.heatmap(df_numerics.corr(), annot=True)


    #----------------------------------------------
    #### Categorical Dataframe
    #----------------------------------------------
    df_dummies = pd.get_dummies(df_name)

    return df_numerics, df_dummies

def feature_house_age(df):

    # List of Years Columns
    list_Years = ['YrSold' ,'YearBuilt' ,'GarageYrBlt' ,'YearRemodAdd','MoSold']

    # HouseAge = YrSold - YearBuilt
    df['HouseAge'] = df[list_Years[0]] - df[list_Years[1]] + df[list_Years[4]]/12

    # GarageAge = YrSold - GarageYrBlt
    df['GarageAge'] = df[list_Years[0]] - df[list_Years[2]]

    # RemodAge = YrSold - YearRemodAdd
    df['RemodAge'] = df[list_Years[0]] - df[list_Years[3]]

    df.drop(labels=list_Years, axis=1, inplace=True)

    return df