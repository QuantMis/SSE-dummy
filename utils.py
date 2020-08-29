import json
from pymongo import MongoClient

def configParser(fname):
    with open(fname, "r") as f:
        return json.load(f)
    
def initMongo():
    config = configParser("config.json")
    ip = config['ip']
    username = config['username']
    password = config['password']
    mainDB = config['mainDB']
    authSource = config['authSource']
    try:
        mclient = MongoClient(ip,username=username,password=password,authSource=authSource)[mainDB]
        print("initMongo Succeed")
        return mclient
    except Exception as e:
        print(e)
        print("initMongo Failed")
    
if __name__ == "__main__":
    initMongo()
