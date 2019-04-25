from cross_validation import cross_validation

def my_linear_regression(X, y):

    # RETURN value
    result = dict()

    # Standarize selected features
    ss = StandardScaler()
    Xs = ss.fit_transform(X)

    #----------------------------------------------
    #### DEFAULT MODEL
    # training model
    linear = LinearRegression()
    linear.fit(Xs, y)

    # Evaluating model
    pred = linear.predict(Xs)
    score_trained = linear.score(Xs, y)
    result.update({'Base': score_trained})

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

    return result