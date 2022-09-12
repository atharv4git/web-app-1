import pandas as pd
import pymysql
from sqlalchemy import create_engine

df = pd.read_csv("CSVs/main_csv3.csv")
db_conn = create_engine('mysql+pymysql://root:pass@localhost:3306/taskdb')
df.to_sql(name="krish_naik_table",con=db_conn,index=False)