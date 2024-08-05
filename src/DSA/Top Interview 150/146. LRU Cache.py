from datetime import datetime
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self._timetracker = {} # { key: datetimenow }
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self._timetracker[key] = datetime.now()
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self._add_to_cache(key, value)
        else:
            if len(self.cache) >= self.capacity:
                self._evict_least_used_item()  
                self._add_to_cache(key, value)
            else:
                self._add_to_cache(key, value)
            
    def _add_to_cache(self, key: int, value: int):
        self.cache[key] = value
        self._timetracker[key] =  datetime.now()
    
    def _evict_least_used_item(self):
        key_to_evict = self._get_least_used_item()
        del self.cache[key_to_evict]
        del self._timetracker[key_to_evict]
    
    def _get_least_used_item(self):
        longestDuration = min(self._timetracker.values())
        
        for k, v in self._timetracker.items():
            if v == longestDuration:
                return k


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    
    #["LRUCache","get","put","get","put","put","get","get"]
    # [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
    
    lRUCache.get(2)
    lRUCache.put(2, 6)
    lRUCache.get(1); 
       
    lRUCache.put(1, 5)
    lRUCache.put(1, 2)
    lRUCache.get(1)
    lRUCache.get(2)