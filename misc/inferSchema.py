import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:123Gucc1@localhost/pmry")

path = "your_csv_file.csv"  # Replace with your actual CSV file path
df = pd.read_csv(path)
