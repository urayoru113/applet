import sqlite3
import pandas as pd

conn = sqlite3.connect('voicetube.db')
df = pd.read_sql_query('SELECT * FROM Sound_Euphonium', conn)
df.to_csv('Sound_Euphonium.csv', index=False, sep='\t')