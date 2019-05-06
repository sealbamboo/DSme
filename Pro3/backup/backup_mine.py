
#### GLOBAL
__list_quality__ = ['NA','Po','Fa','TA','Gd','Ex']
__list_regex__ = ["(^Exterior)","(Qu)(al)?","(Cond$)","(QC$)","(^Heating$)","(Electrical)"]
__list_yes_no__ = ['N', 'Y']
__list_paved_drive__ = ['NA','N','P','Y']
__list_bsmt_exposure__ = ['NA','No','Mn','Av','Gd']
__list_garage_finish__ = ['NA','Unf','RFn','Fin']
__list_lot_shape__ = ['NA','IR3','IR2','IR3','Reg']
__list_street__ = ['NA','Pave','Grvl']
__list_alley__ = ['NA','Pave','Grvl']
__list_land_contour__ = ['NA','Low','HLS','Bnk','Lvl']
__list_utilities__ = ['NA','ELO','NoSeWa','NoSeWr','AllPub']
__list_land_slope = ['NA','Sev','Mod','Gtl']


# ---------------------------------------------------
### FIND THE METRICS COLUMN BY REGEX
# ---------------------------------------------------
def get_metrics_col(df, regex):
    columns = df.columns

    metrics = []
    for key, value in enumerate(columns):
        test = re.search(regex,value)
        if test:
            metrics.append(value)

    return metrics


# ---------------------------------------------------
### STATIC
### GET RENOVATE-ABLE LIST
# ---------------------------------------------------
def get_renovate_able_list(df):
    result = list()

    for key, value in enumerate(__list_regex__):
        result += get_metrics_col(df,value)

    return result

# ---------------------------------------------------
### CONVERT QUALITY SCALE INTO NUMBER
# ---------------------------------------------------
def get_qual_score(sample):

    for key, value in enumerate(__list_quality__):
        if value == sample:
            return key

    return -1       


# ---------------------------------------------------
### STATIC
### GET & CONVERT RENOVATE-ABLE LIST TO NUMBERICS
# ---------------------------------------------------
def turn_qual_into_num(df):
    list_target = list()

    # Target list will be Qual & Cond metrics
    for i_ in range(1,4):
        list_target += get_metrics_col(df,__list_regex__[i_])

    # Iterate through DataFrame
    for value in list_target:
        df[value] = df[value].apply(get_qual_score)

# ---------------------------------------------------
### STATIC
### CONVERTABLE LIST TO NUMBERICS
# ---------------------------------------------------
__this_group_functions = dict({
                            'CentralAir': ['N', 'Y'],
                            'PavedDrive': ['NA','N','P','Y'],
                            'BsmtExposure': ['NA','No','Mn','Av','Gd'],
                            'GarageFinish': ['NA','Unf','RFn','Fin'],
                            'LotShape': ['NA','IR3','IR2','IR3','Reg'],
                            'Street': ['NA','Pave','Grvl'],
                            'Alley': ['NA','Pave','Grvl'],
                            'LandContour': ['NA','Low','HLS','Bnk','Lvl'],
                            'Utilities': ['NA','ELO','NoSeWa','NoSeWr','AllPub']})

def exchange_convertable_list(df):
    columns = df.columns

    for key, value in enumerate(columns):
        df[value] = df[value].apply(lambda row: check_value_in_specific_list(__this_group_functions[value],row))

    # # CentralAir
    # df[columns[0]] = df[columns[0]].apply(check_value_in_list_yes_no)
    # # df[columns[0]] = df[columns[0]].map(lambda row: key if row == value else -1 for key, value in enumerate(__list_yes_no__))

    # # PavedDrive
    # df[columns[1]] = df[columns[1]].apply(check_value_in_list_paved_drive)

    # # BsmtExposure
    # df[columns[2]] = df[columns[2]].apply(check_value_in_list_bsmt_exposure)

    # # GarageFinish    
    # df[columns[3]] = df[columns[3]].apply(check_value_in_list_garage_finish)

    # # LotShape
    # df[columns[4]] = df[columns[4]].apply(check_value_in_list_lot_shape)

    # # Street
    # df[columns[5]] = df[columns[5]].apply(check_value_in_list_street)

    # # Alley
    # df[columns[6]] = df[columns[6]].apply(check_value_in_list_alley)

    # # LandContour
    # df[columns[7]] = df[columns[7]].apply(check_value_in_list_land_contour)

    # # Utilities
    # df[columns[8]] = df[columns[8]].apply(check_value_in_list_utilities)
def check_value_in_specific_list(listname, sample):  
    for key, value in enumerate(listname):
        if sample == value:            
            return key
    return -1


# def check_value_in_list_yes_no(sample):
#     for key, value in enumerate(__list_yes_no__):
#         if sample == value:
#             return key
#     return -1

# def check_value_in_list_paved_drive(sample):
#     for key, value in enumerate(__list_paved_drive__):
#         if sample == value:
#             return key
#     return -1

# def check_value_in_list_bsmt_exposure(sample):
#     for key, value in enumerate(__list_bsmt_exposure__):
#         if sample == value:
#             return key
#     return -1

# def check_value_in_list_garage_finish(sample):
#     for key, value in enumerate(__list_garage_finish__):
#         if sample == value:
#             return key
#     return -1

# def check_value_in_list_lot_shape(sample):
#     for key, value in enumerate(__list_lot_shape__):
#         if sample == value:
#             return key
#     return -1

# def check_value_in_list_street(sample):
#     for key, value in enumerate(__list_street__):
#         if sample == value:
#             return key
#     return -1

# def check_value_in_list_alley(sample):
#     for key, value in enumerate(__list_alley__):
#         if sample == value:
#             return key
#     return -1

# def check_value_in_list_land_contour(sample):
#     for key, value in enumerate(__list_land_contour__):
#         if sample == value:
#             return key
#     return -1

# def check_value_in_list_utilities(sample):
#     for key, value in enumerate(__list_utilities__):
#         if sample == value:
#             return key
#     return -1
