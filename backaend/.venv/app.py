from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/") 
db = client["mydatabase"]  # Database name
collection = db["users"]   # Collection name

@app.route('/', methods=['POST'])
def add_user():
    return "<p>Hello World!</p>"

@app.route('/register', methods=['GET'])
def register():
    users = list(collection.find({}, {"_id": 0}))  # Excluding _id from response
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
