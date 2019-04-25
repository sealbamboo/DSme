
def regression-regularization(X, y):
    #---------------------------------------------
    # RidgeCV
    #----------------------------------------------
    # optimal value for Ridge regression alpha using RidgeCV
    ridge_alphas = np.logspace(0, 5, 200)

    optimal_ridge = RidgeCV(alphas=ridge_alphas, cv=10)
    optimal_ridge.fit(Xs, y)

    print("Ridge Alpha: ", optimal_ridge.alpha_)

    # Cross-validate the Ridge regression
    ridge = Ridge(alpha=optimal_ridge.alpha_)

    ridge_scores = cross_val_score(ridge, Xs, y, cv=10)

    print(ridge_scores)
    print("RidgeCV Mean: ", np.mean(ridge_scores))
    print("-----------------------------------------------------")
    print("\n")

    #----------------------------------------------
    # LassoCV
    #----------------------------------------------
    # Optimal value for Lasso regression alpha using LassoCV
    optimal_lasso = LassoCV(n_alphas=500, cv=10, verbose=1)
    optimal_lasso.fit(Xs, y)

    print("Lasso Alpha: ",optimal_lasso.alpha_)

    # Cross-validate the Lasso regression
    lasso = Lasso(alpha=optimal_lasso.alpha_)

    lasso_scores = cross_val_score(lasso, Xs, y, cv=10)

    print(lasso_scores)
    print("LassoCV Mean: ", np.mean(lasso_scores))
    print("-----------------------------------------------------")
    print("\n")


    #----------------------------------------------
    # ElasticNetCV
    #----------------------------------------------
    # Optimal value for Elastic Net regression alpha using ElasticNetCV
    l1_ratios = np.linspace(0.01, 1.0, 25)

    optimal_enet = ElasticNetCV(l1_ratio=l1_ratios, n_alphas=100, cv=10,
                                verbose=1)
    optimal_enet.fit(Xs, y)

    print("ElasticNet Alpha: ",optimal_enet.alpha_)
    print(optimal_enet.l1_ratio_)

    # Cross-validate the ElasticNet with L1_ratio
    enet = ElasticNet(alpha=optimal_enet.alpha_, l1_ratio=optimal_enet.l1_ratio_)

    enet_scores = cross_val_score(enet, Xs, y, cv=10)

    print(enet_scores)
    print("ElasticCV Mean: ", np.mean(enet_scores))
    print("-----------------------------------------------------")
    print("\n")