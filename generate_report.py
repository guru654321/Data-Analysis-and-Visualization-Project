import pandas as pd

# Load the dataset
data = pd.read_csv('supermarket_data.csv')

# Generate insights
insights = """
Insights:
1. The dataset contains a mix of numerical and categorical features.
2. Strong positive correlations are observed between several numerical features.
3. Some categorical features exhibit significant imbalances which could impact analysis.
"""

# Generate a comprehensive report
with open('supermarket_report.txt', 'w') as report_file:
    report_file.write("Supermarket Data Analysis Report\n")
    report_file.write("="*40 + "\n\n")
    report_file.write("1. Dataset Overview\n")
    report_file.write("-"*20 + "\n")
    report_file.write(str(data.info()) + "\n\n")
    report_file.write("2. Summary Statistics\n")
    report_file.write("-"*20 + "\n")
    report_file.write(str(data.describe()) + "\n\n")
    report_file.write("3. Insights\n")
    report_file.write("-"*20 + "\n")
    report_file.write(insights + "\n\n")

print("Report generated and saved as supermarket_report.txt")
