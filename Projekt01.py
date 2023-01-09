from pymongo import MongoClient
import json

uri = "mongodb+srv://Mateo:Mateo@projekt1.vmoiu28.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.sample_mflix

#kako uzet prvih sto?
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
    return usernames  # return the list of usernames


#kako uzet prvih sto?
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
    return usernames  # return the list of usernames

#-----------------------------------------------------------------------------
file = open('test1.json')
data = json.load(file)
usernameW(data)
usernameD(data)

usernames_w = usernameW(data)
print(usernames_w)
usernames_d = usernameD(data)
print(usernames_d)

db.users.insert_many([{"username": username} for username in usernames_w])
db.users.insert_many([{"username": username} for username in usernames_d])
        
#app = Flask(__name__)

#if __name__ == '__main__':
#    app.run()
