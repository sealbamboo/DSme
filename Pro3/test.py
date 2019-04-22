import pandas as pd

def test_print():
    return "Hello World"

def mean(list):
    return np.mean(list)

def merge_columns_to_one(df,list_added_columns, new_column_name):
    
    df_result = pd.DataFrame()
    df_temp = df[list_added_columns]
    df_result[str(new_column_name)] = df_temp.sum(axis=1)
    
    return df_result

#---------------------------------------------------------------------
# Generate a mask for the upper triangle
# mask = np.zeros_like(corr, dtype=np.bool)
# mask[np.triu_indices_from(mask)] = True

#---------------------------------------------------------------------
# This function does a pairplot across your variables with the color
# set as the outcome "malignant" class variable
def bcw_pairplotter(df, variables, sample_frac=0.3):
    # sample_frac lets you specify an amount of the data to sample for the plot.
    # this speeds up the function which can take awhile with the full data.
    
    # get the number of rows/data points:
    rows = df.shape[0]
    
    # get downsample indicies for the data, if specified
    if sample_frac < 1.0:
        sample_inds = np.random.choice(list(range(0,rows)), 
                                       size=int(round(rows*sample_frac)), 
                                       replace=False).astype(int)
    
    # make the pairplot for the variables:
    pairs = sns.pairplot(df.iloc[sample_inds, :], 
                         vars=variables, 
                         hue="malignant", 
                         palette=sns.xkcd_palette(['windows blue', 'amber']))

#---------------------------------------------------------------------
# Count frequency of value in list
# from itertools import groupby
# [len(list(group)) for key, group in groupby(a)]


#---------------------------------------------------------------------

def correlation_heat_map(df):
    corrs = df.corr()

    # Set the default matplotlib figure size:
    fig, ax = plt.subplots(figsize=(25,30))

    # Generate a mask for the upper triangle (taken from seaborn example gallery)
    mask = np.zeros_like(corrs, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Plot the heatmap with seaborn.
    # Assign the matplotlib axis the function returns. This will let us resize the labels.
    ax = sns.heatmap(corrs, mask=mask, annot=True)

    # Resize the labels.
    ax.set_xticklabels(ax.xaxis.get_ticklabels(), fontsize=14, rotation=30)
    ax.set_yticklabels(ax.yaxis.get_ticklabels(), fontsize=14, rotation=0)

    # If you put plt.show() at the bottom, it prevents those useless printouts from matplotlib.
    plt.show()
    


#---------------------------------------------------------------------
def plotting_features_vs_target(features, df, x, y):
    # define number of subplot
    num_feature = len(features)
    f, axes = plt.subplots(1, num_feature, sharey=True)

    # plotting
    for i in range(0, num_feature):
        print("-i: ", i,"\n")
        axes[i].scatter(x[features[i]], y)
        axes[i].set_title(features[i])

    plt.show()

def plotting_features(features,df, xAxis, yAxis):
        # Count features
        n_features = len(features)

        # Calulate rows
        n_rows = round(n_features/4)

        # Create subplots
        fig, ax = plt.subplots(n_rows, 4, figsize=(17,14), sharey=True)

        # Plotting
        i_row = 1
        for i_ in range(0, n_features):
                if i_//4 == 0:
                        df.plot(x = yAxis,
                                kind='bar', figsize=fig, subplots=True,
                                ax = ax[i_row, i_], orient='v', color='b')
                else:
                        i_row += 1

        plt.show()