from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://postgres:123Gucc1@localhost/pmry')

df = pd.read_csv(path, engine)

