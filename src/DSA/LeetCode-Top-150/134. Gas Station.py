class Solution:
    
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        pass
    
    # My own greedy algorithm - make a dict of gas / cost to get "weigtage"
    # then sort by highest weightage.
    # ignore weight that is < 1.0
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        
        # calc gas/cost percentage and start with largest percentage
        # will not include weitage below 1
        gasCostWeightage = {}
        
        for x in range(len(gas)):
            if cost[x] == 0:
                gasCostWeightage[x] = gas[x] / 1
            else:
                gasCostWeightage[x] = gas[x] / cost[x]
        
        # sort by highest weightage
        gasCostWeightage = sorted(gasCostWeightage.items(), key= lambda kv: kv[1], reverse=True)
        
        for startIdx in gasCostWeightage:
            
            currIdx = startIdx[0]
            currGas = 0
            
            while True:
                
                nextCircularEndIdx = (currIdx + 1) % len(gas)
                
                currGas = currGas + (gas[currIdx] - cost[currIdx])
                
                # a circular route found
                if nextCircularEndIdx == startIdx[0] and currGas >= 0:
                    return startIdx[0]
                
                if currGas >= 1:
                    currIdx = (currIdx + 1) % (len(gas))   
                else:
                    break
                
        return -1
        
    
    # brute force - time limit exceeded
    # def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        
    #     if len(gas) == 1:
    #         if gas[0] - cost[0] >= 0:
    #             return 0
    #         else:
    #             return -1
        
    #     startIdx = 0
    #     currIdx = 0
        
    #     while startIdx <= len(gas) - 1:
                     
    #         if (gas[startIdx] - cost[startIdx]) < 1:
    #             startIdx += 1
    #             continue
            
    #         currIdx = startIdx
    #         currGas = 0

    #         while currIdx != startIdx or currGas == 0:
                
    #             nextCircularEndIdx = (currIdx + 1) % len(gas)
                
    #             currGas = currGas + (gas[currIdx] - cost[currIdx])
                
    #             # a circular route found
    #             if nextCircularEndIdx == startIdx and currGas >= 0:
    #                 return startIdx
                
    #             if currGas >= 1:
    #                 currIdx = (currIdx + 1) % (len(gas))   
    #             else:
    #                 break
            
    #         startIdx += 1

    #     return -1
            

    

    
s = Solution()
# print(s.canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1]))
# print(s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
#print(s.canCompleteCircuit([2,3,4],[3,4,3]))
#print(s.canCompleteCircuit([3,3,4],[3,4,4]))
#print(s.canCompleteCircuit([4,5,2,6,5,3],[3,2,7,3,2,9]))
# print(s.canCompleteCircuit([3,1,1],[1,2,2]))
# print(s.canCompleteCircuit([4,5,3,1,4],[5,4,3,4,2]))
# print(s.canCompleteCircuit([2],[2]))
print(s.canCompleteCircuit([2,0,1,2,3,4,0],[0,1,0,0,0,0,11]))

