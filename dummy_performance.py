from utils import *
from datetime import datetime
import random
import time


timeframe = 3600 # every one hour
class dummy_performance:
    def __init__(self):
        print("initiate dummy performance")
        self.mongo = initMongo()
        self.collection = self.mongo.statistic.find_one({'tag':'dummy_performance'})
        self.run()
    
    def run(self):
        current = datetime.fromtimestamp(int(time.time())).strftime('%H:%M:%S') 
        random_inc1 = random.uniform(-5,5)
        random_inc2 = random.uniform(-5,10)
        timestamps = self.collection['timestamp']
        performance_strategy1 = self.collection['strategy1']
        performance_strategy2 = self.collection['strategy2']  
        # update timestamp
        timestamps.append(current)

        # update performance_strategy1
        latest_1 = performance_strategy1[-1]
        new_1 = latest_1 + random_inc1
        performance_strategy1.append(round(new_1,2))

        # update performance_strategy2
        latest_2 = performance_strategy2[-1]
        new_2 = latest_2 + random_inc2
        performance_strategy2.append(round(new_2,2))

        data = {
            'timestamp':timestamps,
            'strategy1':performance_strategy1,
            'strategy2':performance_strategy2
        }
        
        self.mongo.statistic.find_one_and_update({'tag':'dummy_performance'},{'$set':data})
        print("insertion done")
        return    

if __name__ == "__main__":
    while True:
        dummy_performance()
        time.sleep(timeframe)
