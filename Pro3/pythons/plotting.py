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