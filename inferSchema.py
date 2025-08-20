import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:123Gucc1@localhost/pmry")

df = pd.read_csv(path, engine)
