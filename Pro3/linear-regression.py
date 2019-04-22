
def my-linear-regression(house):

    # RETURN value
    result = dict()

    # Split data-set into trainging (70%) and testing set (30%)
    X_train, X_test, y_train, y_test = train_test_split(Xs, y, test_size=0.3)

    #----------------------------------------------
    #### DEFAULT MODEL
    # training model
    linear = LinearRegression()
    linear.fit(X_train, y_train)

    #evaluating model
    score_trained = linear.score(X_test, y_test)
    result.update({'Base': score_trained})

    #----------------------------------------------
    #### LASSO MODEL
    # L1 regularization
    lasson_linear = Lasso(alpha=1.0)
    lasson_linear.fit(X_train, y_train)

    # evaluating L1 regularized model
    score_lasso_train = lasson_linear.score(X_test, y_test)
    result.update({'Lasson': score_lasso_train})

    #----------------------------------------------
    #### RIDGE MODEL
    # L2 regularization
    ridge_linear = Ridge(alpha = 1.0)
    ridge_linear.fit(X_train, y_train)

    # evaluating L2 regularized model
    score_ridge_trained = ridge_linear.score(X_test, y_test)
    result.update({'Ridge': score_ridge_trained})

    #----------------------------------------------
    return result