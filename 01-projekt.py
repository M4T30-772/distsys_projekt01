from pymongo import MongoClient
from flask import Flask, jsonify
import asyncio
import aiofiles
import json
import random
import string
uri = "mongodb+srv://Mateo:Mateo@projekt1.vmoiu28.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.sample_mflix

#2 zad - sprema u database sva imena gdje username pocinje sa w
def usernameW(data):
    usernameFinder = 'username = \''
    usernames = []
    for i in data:
        if i['content']:
            z = i['content']
            singleContent = z.find(usernameFinder)
            if singleContent != -1:
                usernameStart = singleContent + len(usernameFinder)
                completeUsername = z[usernameStart:].partition("'")[0]
                if completeUsername[0] == 'w':
                    usernames.append(completeUsername)
    return usernames  

#3 zad - sprema u database sva imena gdje username pocinje sa d
def usernameD(data):
    usernameFinder = 'username = \''
    usernames = []
    for i in data:
        if i['content']:
            z = i['content']
            singleContent = z.find(usernameFinder)
            if singleContent != -1:
                usernameStart = singleContent + len(usernameFinder)
                completeUsername = z[usernameStart:].partition("'")[0]
                if completeUsername[0] == 'd':
                    usernames.append(completeUsername)
    return usernames  

file = open('file-000000000040.json')
data = json.load(file)
usernameW(data)
usernameD(data)

usernames_w = usernameW(data)
print(usernames_w) 
usernames_d = usernameD(data)
print(usernames_d)

data_exists = db.users.count_documents({}) > 0
if not data_exists:
    file = open('file-000000000040.json')
    data = json.load(file)
    usernames_w = usernameW(data)
    usernames_d = usernameD(data)
    all_usernames = usernames_w + usernames_d
    db.users.insert_many([{"username": username} for username in all_usernames])
    
def get_link(data):
    linkFinder = 'github \''
    links = []
    for i in data:
        if i['content']:
            z = i['content']
            singleContent = z.find(linkFinder)
            if singleContent != -1:
                usernameStart = singleContent + len(linkFinder)
                completeUsername = z[usernameStart:].partition("'")[0]
                if completeUsername[0] == 'd':
                    links.append(completeUsername)
    return links
        
app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return 'test'

@app.route('/main', methods=['GET'])
def get_link():
    data = json.load(open('file-000000000040.json'))
    link = get_link(data)
    return jsonify(link)

@app.route('/usernameW', methods=['GET'])
def get_usernames_w():
    data = json.load(open('file-000000000040.json'))
    usernames = usernameW(data)
    return jsonify(usernames)

@app.route('/usernameD', methods=['GET'])
def get_usernames_d():
    data = json.load(open('file-000000000040.json'))
    usernames = usernameD(data)
    return jsonify(usernames)
#zad 4
@app.route('/gatherData', methods=['GET'])
async def gather_data():
    usernames_w = await usernameW()
    usernames_d = await usernameD()
    all_usernames = usernames_w + usernames_d
    if len(all_usernames) > 10:
        await create_files(all_usernames)
    return jsonify(all_usernames)
async def create_files(usernames):
    for username in usernames:
        file_name = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        with open(f'{file_name}.txt', 'w') as f:
            f.write(username)
if __name__ == '__main__':
    app.run(debug=True)
db.users.insert_many([{"username": username} for username in usernames_w])
db.users.insert_many([{"username": username} for username in usernames_d])