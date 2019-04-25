# # Create subplots
# fix, ax = plt.subplots(4,4, figsize=(17,14))
# plt.subplots_adjust(hspace=0.2)

# # Create a list of drugs to iterate over the subplots
# drug_name = list(drug_percent_use.columns)[2:]

# # Loop for creating subplots for each drug
# plot_count = 0
# for i in range(4):
#     for j in range(4):
#         if plot_count < 13:
#             sns.barplot(x=drug_percent_use['sample_age'], y=drug_percent_use[drug_name[plot_count]],
#                         orient='v', ax=ax[i][j], color='c')
#         plot_count += 1        




# # Create subplots
# fix, ax = plt.subplots(4,4, figsize=(17,14))
# plt.subplots_adjust(hspace=0.2)

# # Create a list of drugs to iterate over the subplots
# drug_name = list(drug_median_use.columns)[2:]

# # Loop for creating subplots for each drug
# plot_count = 0
# for i in range(4):
#     for j in range(4):
#         if plot_count < 13:
#             sns.barplot(x=drug_median_use['sample_age'], y=drug_median_use[drug_name[plot_count]],
#                         orient='v', ax=ax[i][j], color='C2')
#         plot_count += 1


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
def my_pair_plot_4_sale_price(df,x):
    sns.pairplot(df, x_vars=x, y_vars=['SalePrice'],size=4,kind='reg');


#---------------------------------------------------------------------
def plotting_features_vs_target(features, x, y):
    # define number of subplot
    columns = 3
    num_feature = len(features)
    rows = round(num_feature/columns)

    f, axes = plt.subplots(rows, columns, figsize=(17,14))
    plt.subplots_adjust(hspace=0.2, wspace=0.7)

    # plotting
    # for i in range(0, num_feature):
        # print("-i: ", i,"\n")
        # axes[i].scatter(x[features[i]], y)
        # axes[i].set_title(features[i])
    plot_count = 0
    for i in range(4):
        for j in range(4):
            if plot_count < num_feature:
                sns.barplot(x=x[features[i]], y=y, orient='v', ax=axes[i][j], color='c')
            plot_count += 1     
        
    plt.show()