from datetime import datetime

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache = {}
        self._timeTracker = {}

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
         
        val = self._cache[key]
        self._timeTracker[key] = datetime.now() # update time to latest when key is "used"
        return val

    def put(self, key: int, value: int) -> None:
        
        if key in self._cache:
            self._cache[key] = value
            self._timeTracker[key] = datetime.now()
            return
        
        if key not in self._cache and len(self._cache) + 1 > self.capacity:
            self.eviction()
            self._cache[key] = value
            self._timeTracker[key] = datetime.now()
        # key is not in cache and capacity is not reached yet
        else:
            self._cache[key] = value
            self._timeTracker[key] = datetime.now()
        
    
    def eviction(self):
        oldestKey = self.get_oldest_key()
        
        if oldestKey in self._cache and oldestKey in self._timeTracker:
            self._cache.pop(oldestKey)
            self._timeTracker.pop(oldestKey)
    
    def get_oldest_key(self):
        key = min(self._timeTracker, key=self._timeTracker.get)
        return key

if __name__ == '__main__':

    
    lru = None
    result = []
    actions = ["LRUCache","put","put","put","put","get","get"]
    kvs = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
    
    for idx in range(0, len(actions)):
        action = actions[idx]
        kv = kvs[idx]
        
        if action == "LRUCache":
            lru = LRUCache(kv[0])
        elif action == "put":
            key = kv[0]
            val = kv[1]
            lru.put(key,val)
        elif action == "get":
            key = kv[0]
            result.append(lru.get(key))
            
    print(result)
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)