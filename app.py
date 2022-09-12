from flask import Flask, render_template, request, jsonify, make_response, send_file, Response
from flask_cors import CORS,cross_origin
import pymongo
import pandas as pd
from IPython.display import HTML
import csv
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
@cross_origin()
def index():
    return render_template("index.html")



@app.route('/success', methods=["POST", "GET"])
def html_table():
    cname = request.form.get("cname")
    cname = cname.replace(" ","_")
    df = pd.read_json(f"./JSONs/{cname}.json")
    tables = df.values.tolist()
    return render_template("results.html",  tables=tables)


if __name__ == '__main__':
    app.run()