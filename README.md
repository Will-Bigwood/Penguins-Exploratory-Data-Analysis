# Penguins Exploratory Data Analysis
A breif exploratory analysis of the 'penguins_size' dataset using Python to process and visualise the data
### Introduction
The dataset is related to Penguin research and has information on Penguin's species, habitat, gender, and size. In this report I have conducted an exploratory data analysis on the dataset and provided a description of my findings accompanied by visualisations in a report.
### Getting Started
To run the code you will need to have Python installed on your device, as well as pandas, numpy, matplotlib and seaborn Python libraries.
Ensure the penguins_size.csv file is in the same directory as the Python file when you run the code otherwise you will encounter an error.
### Usage
Running the code will clean the dataset and produce all the visualisations seen in the analysis report. For example the snippet of code below produces a count plot to show the total number of each penguin species observed on each of the three islands in the dataset.
```python
# Create a figure with three subplots (one for each island)
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
# Iterate through the unique island names and create a subplot for each one
islands = penguins_df['island'].unique()
for i, species in enumerate(islands):
    ax = axes[i]
    # Filter the data for the current island
    species_data = penguins_df[penguins_df['island'] == species]    
    # Create a countplot for species distribution on the current island
    sns.countplot(data=species_data, x='species', ax=ax)
    ax.set_title(f'Species Distribution at {species}')
    ax.set_xlabel('Species')
    ax.set_ylabel('Count')
plt.tight_layout()
plt.show()
```
<img width="1097" alt="Screen Shot 2023-11-10 at 13 01 38" src="https://github.com/Will-Bigwood/Penguins-Exploratory-Data-Analysis/assets/134322954/ccb69f86-41f4-4e9d-81c8-2fcb380cc418">

### Findings
Producing visualisations provided greater insight into the differences between the species of Penguins. The three species  were compared with regard to their location, and the size measurements of their flippers and culmens. These differences were explored and discussed in the report.
