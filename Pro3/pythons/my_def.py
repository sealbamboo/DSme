def year_in_float(house_num):
    # List of Years Columns
    list_Years = ['YrSold' ,'YearBuilt' ,'GarageYrBlt' ,'YearRemodAdd','MoSold']

    # HouseAge = YrSold - YearBuilt
    house_num['HouseAge'] = house_num[list_Years[0]] - house_num[list_Years[1]] + house_num[list_Years[4]]

    # GarageAge = YrSold - GarageYrBlt
    house_num['GarageAge'] = house_num[list_Years[0]] - house_num[list_Years[2]]

    # RemodAge = YrSold - YearRemodAdd
    house_num['RemodAge'] = house_num[list_Years[0]] - house_num[list_Years[3]]

    house_num.drop(labels=list_Years, axis=1, inplace=True)