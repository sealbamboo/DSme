from sklearn.linear_model import LinearRegression

from plotting import plotting_features
from linear_regression import my_linear_regression, my_linear_regression_w_test

def let_perform(df_pre_num, df_post_num):
    # Origin Plotting
    plotting_features(df_pre_num)

    # Log tranform
    df_pre_num = np.log(df_pre_num.copy() + 1)
    # log_pre_sales = np.log(df['SalePrice']+1)
    plotting_features(df_pre_num, color='C2')

    # Pre-Linear-Regression
    df_pre_backup = df_pre_num.copy()
    y = df_pre_num['SalePrice'].values
    df_pre_num.drop(labels=['SalePrice'],axis=1, inplace=True)
    X = df_pre_num.copy()

    # Linear-Regression
    linear_scores = my_linear_regression(X, y, True)

    # Test on Linear-Regression
    y_test = df_post_num['SalePrice'].values
    df_post_num.drop(labels=['SalePrice'],axis=1, inplace=True)
    X_test = df_post_num.copy()

    # Out score
    linear_scores_w_test = my_linear_regression_w_test(X, y,X_test, y_test)    
    print(linear_scores_w_test)

    return linear_scores