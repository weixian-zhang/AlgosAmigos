import random
class RandomizedSet:

    def __init__(self):
        self.rset = {}
        

    def insert(self, val: int) -> bool:
        if val in self.rset:
            return False
        
        self.rset[val] = val
        return True

    def remove(self, val: int) -> bool:
        if val in self.rset:
            del self.rset[val]
            return True

        return False

    def getRandom(self) -> int:
        if len(self.rset) > 0:
            randIdx = random.choice(list(self.rset.keys()))
            return self.rset[randIdx]
        return -1
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(1)
param_3 = obj.getRandom()