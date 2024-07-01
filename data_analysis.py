import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('supermarket_data.csv')

# Function for exploratory data analysis and visualization
def explore_data(df):
    # Display basic information about the dataset
    print("Dataset Information:")
    print(df.info())
    print("\n")

    # Display summary statistics
    print("Summary Statistics:")
    print(df.describe())
    print("\n")

    # Check for missing values
    print("Missing Values:")
    print(df.isnull().sum())
    print("\n")

    # Generate insightful visualizations
    # Plot histograms for numerical features
    numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
    plt.figure(figsize=(15, 10))
    for i, feature in enumerate(numerical_features):
        plt.subplot(len(numerical_features) // 3 + 1, 3, i + 1)
        sns.histplot(df[feature], kde=True)
        plt.title(f'Distribution of {feature}')
    plt.tight_layout()
    plt.show()

    # Calculate the correlation matrix
    correlation_matrix = df.corr()

    # Plot the heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

    # Plot scatter plots for numerical features
    plt.figure(figsize=(15, 10))
    for i, feature in enumerate(numerical_features):
        if i == len(numerical_features) - 1:
            break
        plt.subplot(len(numerical_features) // 3 + 1, 3, i + 1)
        sns.scatterplot(x=df[feature], y=df[numerical_features[i + 1]])
        plt.title(f'{feature} vs {numerical_features[i + 1]}')
    plt.tight_layout()
    plt.show()

    # Plot count of categorical features
    categorical_features = df.select_dtypes(include=['object']).columns
    plt.figure(figsize=(15, 10))
    for i, feature in enumerate(categorical_features):
        plt.subplot(len(categorical_features) // 3 + 1, 3, i + 1)
        sns.countplot(df[feature])
        plt.title(f'Count of {feature}')
        plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Perform exploratory data analysis on the loaded dataset
explore_data(data)

# Example insights based on analysis
insights = """
Insights:
1. The dataset contains a mix of numerical and categorical features.
2. Strong positive correlations are observed between several numerical features.
3. Some categorical features exhibit significant imbalances which could impact analysis.
"""

print(insights)
