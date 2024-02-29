import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
df_2015 = pd.read_csv('2015.csv')
df_2016 = pd.read_csv('2016.csv')
df_2017 = pd.read_csv('2017.csv')
df_2018 = pd.read_csv('2018.csv')
df_2019 = pd.read_csv('2019.csv')

# Rename columns to have consistent column names across all datasets
df_2016.rename(columns={'Economy (GDP per Capita)': 'GDP per capita',
                        'Health (Life Expectancy)': 'Healthy life expectancy',
                        'Trust (Government Corruption)': 'Perceptions of corruption'}, inplace=True)

df_2017.rename(columns={'Happiness.Rank': 'Happiness Rank',
                        'Happiness.Score': 'Happiness Score',
                        'Economy..GDP.per.Capita.': 'GDP per capita',
                        'Health..Life.Expectancy.': 'Healthy life expectancy',
                        'Trust..Government.Corruption.': 'Perceptions of corruption'}, inplace=True)

# For 2018 and 2019, the columns are already consistent with our requirements

# Add a 'Year' column to each DataFrame
df_2015['Year'] = 2015
df_2016['Year'] = 2016
df_2017['Year'] = 2017
df_2018['Year'] = 2018
df_2019['Year'] = 2019

# Concatenate all DataFrames into a single DataFrame
df = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019], ignore_index=True)

# Display the first few rows of the combined DataFrame
print(df.head())

# Trends Over Time: Visualize how happiness scores have changed over time for different countries
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Year', y='Happiness Score', hue='Country or region')
plt.title('Trends in Happiness Scores Over Time')
plt.xlabel('Year')
plt.ylabel('Happiness Score')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Correlation Analysis: Determine relationships between happiness scores and other variables
correlation_matrix = df[['Happiness Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
plt.title('Correlation Matrix')
plt.show()

factors = ['GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']

plt.figure(figsize=(18, 12))
for i, factor in enumerate(factors, 1):
    plt.subplot(2, 3, i)
    sns.scatterplot(data=df, x=factor, y='Happiness Score', alpha=0.7)
    plt.title(f'Happiness Score vs {factor}')
    plt.xlabel(factor)
    plt.ylabel('Happiness Score')
plt.show()

avg_happiness_by_region = df.groupby('Region')['Happiness Score'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(x=avg_happiness_by_region.values, y=avg_happiness_by_region.index, hue = avg_happiness_by_region.index , legend = False, palette='viridis')
plt.title('Average Happiness Score by Region')
plt.xlabel('Average Happiness Score')
plt.ylabel('Region')
plt.show()

# Correlation between Trust in Government and Happiness Score
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Perceptions of corruption', y='Happiness Score', alpha=0.7)
plt.title('Happiness Score vs Trust in Government')
plt.xlabel('Trust in Government')
plt.ylabel('Happiness Score')
plt.show()
