import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Cross-Validation-Train-Test-Split-Solutions
def correlation_heat_map(df):
    corrs = df.corr()

    # Set the default matplotlib figure size:
    fig, ax = plt.subplots(figsize=(25,27))

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
# Pair-Plot
def m_pair_plot(df):
    sns.pairplot(df, kind='bar')


#---------------------------------------------------------------------
# Box-Plot
def m_box_plot(df):
    fig = plt.figure(figsize=(26,20))
    ax = fig.gca()

    sns.boxplot(data=df, orient='v',
                    fliersize=8, linewidth=1.5, notch=False,
                    saturation=0.5, ax=ax)

    ax.set_title('DataFrame boxplot\n', fontsize=20)

    plt.show()


#---------------------------------------------------------------------
def plotting_features(x, color='C1'):

    # Pre-caculate:
    features = x.columns
    num_feature = len(features)

    # define number of subplot
    columns = 3
    rows = round(num_feature/columns)

    fig, axes = plt.subplots(rows, columns, figsize=(16,12))
    plt.subplots_adjust(hspace=0.4)
    
    # plotting
    plot_count = 0
    for i in range(rows):
        for j in range(columns):
            if plot_count <= num_feature:
                sns.distplot(x[features[plot_count]],kde=False, ax=axes[i][j], color= color )
            plot_count += 1     
        
    plt.show()


#---------------------------------------------------------------------
def plotting_linear_w_features(x,y,df):

    # Pre-caculate:
    features = x.columns
    num_feature = len(features)

    # define number of subplot
    columns = 2
    rows = round(num_feature/columns)

    # fig, axes = plt.subplots(rows, columns, figsize=(16,12))
    # plt.subplots_adjust(hspace=0.4)
    
    # plotting
    plot_count = 0
    for i in range(rows):
        for j in range(columns):
            if plot_count <= num_feature:
                sns.lmplot(x=features[plot_count], y=y, data=df, col=y, aspect=0.2)
            plot_count += 1     
        
    plt.show()