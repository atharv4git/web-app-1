import json
import pymongo
import pandas as pd


client = pymongo.MongoClient("mongodb+srv://akayyy:dDYBUUITDo0XSIJ2@test1.fez9nhg.mongodb.net/?retryWrites=true&w=majority")
db = client["web-application"]
col = db["telusko"]
x = col.find_one()
j1 = json.load(x)
df = pd.read_json(j1)
print(df)
# df = pd.read_json("JSONs/telusko.json")
# df2 = df[['vids','vid_id','title']]
# print(df2)