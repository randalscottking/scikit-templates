from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://postgres:123Gucc1@localhost/pmry')

df = pd.read_sql_query(' SELECT * FROM "2013" LIMIT 10', engine)

df.head(10)