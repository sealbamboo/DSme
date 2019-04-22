
def feature_dataframe(df_target):
    # Return DataFrame
    df_result = pd.DataFrame()

    # -----
    # Non-numerrics columns
    # -----
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    df_name = df_target.select_dtypes(exclude=numerics)

    # -----
    # Numerics columns
    # -----
    df_numerics = df_target._get_numeric_data()

    # -----
    # Fill NAN value with 0
    df_numerics = df_numerics.fillna(0)

    # Merge Bathrooms columns into Bathrooms
    list_bathrooms = ['BsmtFullBath', 'BsmtHalfBath', 'FullBath','HalfBath']
    df_temp = df_numerics[list_bathrooms].copy()
    df_numerics['Bathrooms'] = df_temp.sum(axis=1)
    df_numerics.drop(labels=list_bathrooms, axis=1,inplace=True)

    # List of Years Columns
    list_Years = ['YrSold' ,'YearBuilt' ,'GarageYrBlt' ,'YearRemodAdd','MoSold']
    df_temp = df_numerics[list_Years].copy()

    # HouseAge = YrSold - YearBuilt
    df_numerics['HouseAge'] = df_numerics[list_Years[0]] - df_numerics[list_Years[1]]

    # GarageAge = YrSold - GarageYrBlt
    df_numerics['GarageAge'] = df_numerics[list_Years[0]] - df_numerics[list_Years[2]]

    # RemodAge = YrSold - YearRemodAdd
    df_numerics['RemodAge'] = df_numerics[list_Years[0]] - df_numerics[list_Years[3]]

    df_numerics.drop(labels=list_Years, axis=1, inplace=True)

    # Inspect the Basement's Square Feet
    list_Basements = ['BsmtFinSF1','BsmtFinSF2','BsmtUnfSF','TotalBsmtSF']
    df_temp = df_numerics[list_Basements].copy()
    df_temp['Sum3'] = df_temp[list_Basements[:3]].sum(axis=1) > df_temp[list_Basements[3]]
    df_numerics.drop(labels=list_Basements[:3],axis=1,inplace=True)

    # Inspect "Porch"
    list_Porchs = ['OpenPorchSF','EnclosedPorch','3SsnPorch','ScreenPorch']
    df_temp = df_numerics[list_Porchs].copy()
    df_numerics.drop(labels=list_Porchs, axis=1, inplace=True)
    df_numerics['PorchSF'] = df_temp.sum(axis=1)

    # Create Heatmap to see the correlations
    # correlation_heat_map(df_numerics)
    plt.subplots(figsize=(30,30))
    sns.heatmap(df_numerics.corr(), annot=True)