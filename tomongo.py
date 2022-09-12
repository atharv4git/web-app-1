import pymongo
import json
import pandas as pd


# client = pymongo.MongoClient("mongodb+srv://akayyy:dDYBUUITDo0XSIJ2@test1.fez9nhg.mongodb.net/?retryWrites=true&w=majority")
# l = list()
# db = client["web-application"]
# col = db["channel-details-krishnaik"]
# for i in col.find({}):
#     l.append(i)
#
#
# # for i in range(1,len(l[0])):
# #     for j in l:
# #         print(j)
# df = pd.DataFrame()
# l2 = list()
# c1 = 0
# for i in l:
#     df = pd.DataFrame(i.items())
#     l2.append(df)
#     print(l2[c1])
#     c1 += 1
password = "indore11"
client = pymongo.MongoClient(f"mongodb+srv://hiteshwadhwani1403:{password}@ineuron.xskip.mongodb.net/?retryWrites=true&w=majority")
db = client["web-application"]

def find_data(collection_name):
    client_conn = client
    db = client_conn['youtube-scrapper']
    mycol = db[collection_name]
    data = mycol.find({})
    return data

l = list()
for i in find_data("krish_naik"):
    l.append(i)

print(l)