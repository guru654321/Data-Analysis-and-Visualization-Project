import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic supermarket data
num_records = 50000

# Generate random data
data = {
    'customer_id': np.arange(1, num_records + 1),
    'age': np.random.randint(18, 80, num_records),
    'gender': np.random.choice(['Male', 'Female'], num_records),
    'product_category': np.random.choice(['Grocery', 'Clothing', 'Electronics'], num_records),
    'amount_spent': np.random.normal(100, 50, num_records)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('supermarket_data.csv', index=False)

print(f"Sample supermarket dataset with {num_records} records generated and saved as supermarket_data.csv")
