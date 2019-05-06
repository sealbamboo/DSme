from linear_regression import my_linear_regression, my_linear_regression_w_test
import seaborn as sns

#### GLOBAL
__list_quality__ = ['NA','Po','Fa','TA','Gd','Ex']
__list_regex__ = [
        "(^Roof)",
        "(^Exterior)",
        "(Qu)(al)?",
        "(Cond$)",
        "(QC$)"
    ]
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
    # Apply Regex to search the approximate "Qual/Cond/QC" columns
    # THEN return an metrics which contains all colums name
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

    # Most "convertable" columns have same range quality
    # "__list_quality" will be applied. 
    for key, value in enumerate(__list_quality__):
        if value == sample:
            return key

    return -1       


# ---------------------------------------------------
### STATIC
### GET & CONVERT RENOVATE-ABLE LIST TO NUMBERICS
# ---------------------------------------------------
def turn_renovated_qc_into_num(df):
    list_target = list()

    # Target list will be Qual & Cond metrics
    for i_ in range(2,5):
        list_target += get_metrics_col(df,__list_regex__[i_])

    # Iterate through DataFrame
    for value in list_target:
        # If value is matched __this_renovate_group__
        if is_this_renovate_group(value):
                # Features are not have same scale as "__list_quality__"
                df[value] = df[value].apply(lambda row: check_value_in_specific_list(get_this_renovate_group(value),row))
        else:
                df[value] = df[value].apply(get_qual_score)
 

# ---------------------------------------------------
### STATIC
### CONVERTABLE LIST TO NUMBERICS
### Notes: df_renovate
# ---------------------------------------------------
__this_renovate_group__ = dict({
                                'Electrical' : ['NA','Mix','FuseP','FuseF','FuseA','SBrkr'],
                                'Heating': ['NA','Floor','GasA','GasW','Gasv','OthW','Wall']
                            })

def is_this_renovate_group(sample):
        for key, value in __this_renovate_group__.items():
                if sample is key:
                        return True
        return False

def get_this_renovate_group(sample_key):
        return __this_renovate_group__[sample_key]



# ---------------------------------------------------
### STATIC
### CONVERTABLE LIST TO NUMBERICS
### Notes: df_convertable
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
                            'Utilities': ['NA','ELO','NoSeWa','NoSeWr','AllPub'],
                            'LandSlope': ['NA','Sev','Mod','Gtl'],
                            'Fence': ['NA','MnWw','GdWo','MnPrv','GdPrv']
                            })

def exchange_convertable_list(df):
    columns = df.columns

    for key, value in enumerate(columns):
        df[value] = df[value].apply(lambda row: check_value_in_specific_list(__this_group_functions[value],row))

def check_value_in_specific_list(listname, sample):  
    for key, value in enumerate(listname):
        if sample == value:            
            return key
    return -1
