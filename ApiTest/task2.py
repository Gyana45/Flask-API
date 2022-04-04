"""waf to fetch a data from mongodb table"""
from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

url = "mongodb+srv://test:test@apitaskcluster.glebc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(url)
db = client['api_DB']
col = db['api_col']


@app.route("/insert_one", methods=['POST'])
def insert_one():
    if request.method == 'POST':
        record = request.json['record']

        col.insert_one(record)

        return jsonify("Successfully inserted")


@app.route("/fetchall", methods=['GET'])
def fetchall():
    data = col.find()
    l = []
    for i in data:
        l.append(i)
    return str(l)


if __name__ == "__main__":
    app.run(port=51211)
"""
---insert_one
{
    "record":{"companyName": "iNeuron",
         "product": "Affordable AI",
         "courseOffered": "Deep Learning for Computer Vision",
         "name" : ["Gyana","pradhan",5121],
         "record_dict" :{"name" :"sudhanshu" , "mail_id" : "sudhanshu@fadfsaf.ai","ph_number" :543535}}
}         

----fetchall

[{'_id': ObjectId('624ab469c98c2438da40ba20'), 'companyName': 'iNeuron', 'product': 'Affordable AI', 'courseOffered':
'Deep Learning for Computer Vision', 'name': ['Gyana', 'pradhan', 5121], 'record_dict': {'name': 'sudhanshu', 'mail_id':
'sudhanshu@fadfsaf.ai', 'ph_number': 543535}}]

"""
