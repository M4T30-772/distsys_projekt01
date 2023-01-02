#import flask
import json

usernameFinder= 'username = \''
file = open('test1.json')
data = json.load(file)
for i in data:
    if(i['content']):
        z = i['content']
        singleContent = z.find(usernameFinder)
        usernameStart = singleContent+len(usernameFinder)
        completeUsername = z[usernameStart:].partition("'")[0]
        print(completeUsername)
        
#app = Flask(__name__)

#if __name__ == '__main__':
#    app.run()
