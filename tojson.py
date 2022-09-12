import pandas as pd
from IPython.display import HTML
str1 = input("> ")
df = pd.read_json(f"./JSONs/{str1}.json")
print(df)
result = df.to_html()
print(result)