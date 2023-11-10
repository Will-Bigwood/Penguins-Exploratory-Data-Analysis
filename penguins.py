# --- IMPORT LIBRARIES ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- FUNCTIONS ---
# Check the data types of columns in the Penguins dataframe, and print them to the console
def check_columns_data_types(columns):
    for col in columns:
        data_type = penguins_df[col].dtype
        print(f"The data type of the '{col}' column is: {data_type}")
    print()

# Create and display a distribution histogram for a specific column for each unique species
def create_histogram(column_name, title_prefix):
    # Create a figure with three subplots
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    # Get unique species in the data
    species = penguins_df['species'].unique()
    
    # Iterate through unique species
    for i, specie in enumerate(species):
        ax = axes[i]
        # Filter the data for the current species
        species_data = penguins_df[penguins_df['species'] == specie]
        # Create a histogram for the specified column
        ax.hist(species_data[column_name], bins=20, alpha=0.7)
        # Set subplot title and labels
        ax.set_title(f'{title_prefix} for {specie}')
        ax.set_xlabel(f'{column_name.replace("_", " ").title()}')
        ax.set_ylabel('Frequency')
    # Adjust subplot layout and display the plot
    plt.tight_layout()
    plt.show()

# Create and show a pie chart for sex distribution
def create_pie_chart(data, title):
    sex_distribution = data['sex'].value_counts()
    plt.figure(figsize=(8, 8))
    colors = ['#66ff66', '#009900']
    labels = sex_distribution.index
    plt.pie(sex_distribution, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, pctdistance=0.85)
    plt.title(title)
    plt.axis('equal')
    plt.show()


# --- DATA CLEANING ---
# Load the data from the csv file into a pandas dataframe
penguins_df = pd.read_csv('penguins_size.csv')

# Remove any duplicate rows of data in the pengions dataframe
penguins_df = penguins_df.drop_duplicates()

# Remove all rows where any column contains 'NA'
penguins_df = penguins_df.dropna()

# Remove the row where the data in the 'sex' column is incorectly formatted
penguins_df = penguins_df[penguins_df['sex']!= '.']

# Check the data type of the numeric columns
columns_to_check = ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']
check_columns_data_types(columns_to_check)

# Change the data type for values in the 'flipper_length_mm' and 'body_mass_g' columns to type:int64
columns_to_change = ['flipper_length_mm', 'body_mass_g']
for col in columns_to_change:
    penguins_df[col] = penguins_df[col].astype(np.int64)
# Double check the data type of the changed columns
check_columns_data_types(columns_to_change)

# --- DATA VISUALISATIONS ---
# Create a bar chart for species distribution
species_counts = penguins_df['species'].value_counts()
plt.figure(figsize=(8, 5))
bars = plt.bar(species_counts.index, species_counts.values)
plt.xlabel('Species')
plt.ylabel('Count')
plt.title('Distribution of Penguin Species')
# Add count labels to the bars
for bar, count in zip(bars, species_counts.values):
    plt.text(bar.get_x() + bar.get_width() / 2 - 0.05, bar.get_height() + 10, str(count), fontsize=12)
plt.show()

# Create a countplot for species distribution on each unique island in the data
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

# Create distribution histograms for physical measurements
# Loop through the measurements list and create histograms for each measurement column
measurements = ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']
for col in measurements:
    plt.figure(figsize=(8, 5))
    sns.histplot(penguins_df[col], kde=True)
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {col}')
    plt.show()

# Create a histogram for the distribution of each measurement accross each unique species
create_histogram('body_mass_g', 'Body Mass Distribution')
create_histogram('culmen_length_mm', 'Culmen Length Distribution')
create_histogram('culmen_depth_mm', 'Culmen Depth Distribution')
create_histogram('flipper_length_mm', 'Flipper Length Distribution')

# Create a bar chart to show the average value of each measurement
# Create a list of columns to calculate averages for
measurements_to_average = ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm']
# Initialize a dictionary to store average values for each column
average_values = {}
# Calculate the average for each column and store it in the dictionary
for col in measurements_to_average:
    average_values[col] = penguins_df.groupby('species')[col].mean()
# Create a grouped bar chart for average values
fig, ax = plt.subplots(figsize=(10, 6))
# Set the number of bars dynamically based on the number of unique species
num_bars = len(penguins_df['species'].unique())
bar_width = 0.2
index = range(num_bars)
# Create bars for each column
for i, col in enumerate(measurements_to_average):
    avg = average_values[col]
    # Adjust the x-axis positions to center the bars
    x_positions = [x + i * bar_width - (num_bars / 2) * bar_width for x in index]
    plt.bar(x_positions, avg, width=bar_width, label=col)
plt.xlabel('Species')
plt.ylabel('Average Value')
plt.title('Average Size Measurements by Species')
plt.xticks([x for x in index], penguins_df['species'].unique())
plt.legend()
plt.tight_layout()
plt.show()

# Create a bar chart to show the average body mass of each species
average_body_mass = penguins_df.groupby('species')['body_mass_g'].mean()
plt.figure(figsize=(8, 5))
plt.bar(average_body_mass.index, average_body_mass.values)
plt.xlabel('Species')
plt.ylabel('Average Body Mass (g)')
plt.title('Average Body Mass by Species')
plt.xticks(rotation=45)
plt.show()

# Create correlation matrix for measurements columns
# Select columns of interest
measurements_cols = penguins_df[['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']]
# Plot correlation matrix
plt.figure()
corr_coeff_matrx = measurements_cols.corr()
sns.heatmap(corr_coeff_matrx, annot=True)
plt.show()

# Create sex distribution pie charts for each species
species_lst = ['Adelie', 'Chinstrap', 'Gentoo']
for species in species_lst:
    species_data = penguins_df[penguins_df['species'] == species]
    create_pie_chart(species_data, f'Sex Distribution of the {species} species')

# Create sex distribution pie charts for each island
island_lst = ['Torgersen', 'Biscoe', 'Dream']
for island in island_lst:
    island_data = penguins_df[penguins_df['island'] == island]
    create_pie_chart(island_data, f'Sex Distribution on {island} Island')