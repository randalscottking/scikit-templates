import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1password@localhost/pmry')

df = pd.read_sql_query(' SELECT * FROM "2013" LIMIT 10', engine)

df.head(10)