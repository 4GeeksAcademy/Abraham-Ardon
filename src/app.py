from utils import db_connect
engine = db_connect()

# your code here
import pandas as pd

# Load the dataset
df = pd.read_csv("medical_insurance_cost.csv")

# Preview the first few rows
print(df.head())
print(df.info())  # Check column types and missing values
