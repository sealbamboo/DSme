from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

def cross_validation(linear, X,y):

    # RETURN value
    result = dict()

    # Global Variable
    CV = 10

    #----------------------------------------------
    #### TRAIN TEST SPLIT
    # Split data-set into trainging (80%) and testing set (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Fit linear with X_train & y_train & its score
    linear.fit(X_train, y_train)

    yhat = linear.predict(X_test)
    tts_train_score = linear.score(X_train, y_train)
    tts_test_score = linear.score(X_test, y_test)

    result.update(
        {'TTS-Train': tts_train_score,'TTS-Test': tts_test_score})

    print("Train-split-test (Test) score: ", tts_test_score)
    print("Train-split-test (Train) score: ", tts_train_score)
    print("-----------------------------------------------------")
    print("\n")

    #----------------------------------------------
    #### K-FOLD CROSS-VALIDATION DEMONSTRATION
    # K-Fold Cross Validation Score
    linreg_scores = cross_val_score(linear, X, y, cv=CV)

    print("K-Fold Cross-validated scores: \n")
    print("Score Mean: ", np.mean(linreg_scores))

    # Make cross validated predictions on the test sets
    predictions = cross_val_predict(linear, X, y, cv = CV)
    plt.scatter(y, predictions)

    # Manual calculate the R2
    R2 = metrics.r2_score(y, predictions)

    result.update(
        {'KF-CV score': linreg_scores,'KF-CV Mean score': np.mean(linreg_scores),'R2 score': R2})

    print("Cross-Predicted R2: ", R2)
    print("-----------------------------------------------------")
    print("\n")

    return result