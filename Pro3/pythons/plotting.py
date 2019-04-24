# Create subplots
fix, ax = plt.subplots(4,4, figsize=(17,14))
plt.subplots_adjust(hspace=0.2)

# Create a list of drugs to iterate over the subplots
drug_name = list(drug_percent_use.columns)[2:]

# Loop for creating subplots for each drug
plot_count = 0
for i in range(4):
    for j in range(4):
        if plot_count < 13:
            sns.barplot(x=drug_percent_use['sample_age'], y=drug_percent_use[drug_name[plot_count]],
                        orient='v', ax=ax[i][j], color='c')
        plot_count += 1        




# Create subplots
fix, ax = plt.subplots(4,4, figsize=(17,14))
plt.subplots_adjust(hspace=0.2)

# Create a list of drugs to iterate over the subplots
drug_name = list(drug_median_use.columns)[2:]

# Loop for creating subplots for each drug
plot_count = 0
for i in range(4):
    for j in range(4):
        if plot_count < 13:
            sns.barplot(x=drug_median_use['sample_age'], y=drug_median_use[drug_name[plot_count]],
                        orient='v', ax=ax[i][j], color='C2')
        plot_count += 1


# Cross-Validation-Train-Test-Split-Solutions
def correlation_heat_map(df):
    corrs = df.corr()

    # Set the default matplotlib figure size:
    fig, ax = plt.subplots(figsize=(11,7))

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