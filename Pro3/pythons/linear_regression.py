from cross_validation import cross_validation
from regularization import regression_regularization

def my_linear_regression(X, y, regular=False):

    # RETURN value
    result = dict()

    #----------------------------------------------
    #### DEFAULT NON-STANDARIZE MODEL
    # training model
    linear = LinearRegression()
    n_std_linear = linear.fit(X, y)

    # Evaluating model
    s_std_score_trained = n_std_linear.score(X, y)
    result.update({'Base woStd': s_std_score_trained})

    # Standarize selected features
    ss = StandardScaler()
    Xs = ss.fit_transform(X)

    #----------------------------------------------
    #### DEFAULT MODEL
    # training model
    linear.fit(Xs, y)

    # Evaluating model
    pred = linear.predict(Xs)
    score_trained = linear.score(Xs, y)
    result.update({'Base wStd': score_trained})

    # Cross-validation
    cross_val = cross_validation(linear, Xs, y)
    result.update(cross_val)

    # #----------------------------------------------
    # #### LASSO MODEL
    # # L1 regularization
    # lasson_linear = Lasso(alpha=1.0)
    # lasson_linear.fit(Xs, y)

    # # evaluating L1 regularized model
    # score_lasso_train = lasson_linear.score(Xs, y)
    # result.update({'Lasson': score_lasso_train})

    # #----------------------------------------------
    # #### RIDGE MODEL
    # # L2 regularization
    # ridge_linear = Ridge(alpha = 1.0)
    # ridge_linear.fit(Xs, y)

    # # evaluating L2 regularized model
    # score_ridge_trained = ridge_linear.score(Xs, y)
    # result.update({'Ridge': score_ridge_trained})

    # #----------------------------------------------
    # # Baseline
    # #----------------------------------------------
    # result.update({'Baseline': np.mean(y)})

    if (regular):
        regression_regularization(Xs, y)

    return result