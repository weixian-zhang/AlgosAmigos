# https://www.youtube.com/watch?v=mGfK-j9gAQA

class KnapsackSolution:
    
    def get_highest_profit(self, items=[(1,300), (20,10), (3,6),(2,8),(4,7)], capacity=8):
        
        max_profit = 0
        knapsack = []
        includedItemProfit = 0
        excludedSkipItemProfit = 0
        memoization = [x for x in range(len(items))]
        
        for idx in range(len(memoization)):
            memoization[idx] = [-1 for x in range(capacity)]
        
        def _recurse(capacity, itemIdx, result):
            nonlocal memoization
            """processing last item to first
            """
            
            
            
            current_item = items[itemIdx]
            itemWeight = current_item[0]
            itemProfit = current_item[1]
            
            if memoization[idx][capacity-1] != -1:
                return memoization[idx][itemWeight]
            
            if itemIdx == -1 or capacity <= 0:
                result = 0
            
            # skip item is item is bigger than capacity
            elif itemWeight > capacity:
                
                result = _recurse(capacity, itemIdx - 1, result)
            
            else:
                reducedCapacity = capacity - itemWeight
                
                includeFirstItemProfit = itemProfit + _recurse(reducedCapacity, itemIdx - 1, result)
                
                excludeFirstItemProfit =_recurse(capacity, itemIdx - 1, result)
                
                result = max(includeFirstItemProfit, excludeFirstItemProfit)
                
                memoization[idx][capacity-1] = result #max(itemProfit + _recurse(reducedCapacity, itemIdx - 1), _recurse(capacity, itemIdx - 1))
            
            return result
                
        
        items_with_highest_profit = _recurse(capacity, len(items) - 1, 0)
        
        return items_with_highest_profit
        
                    

import pytest
class TestKnapsack:
    
    @pytest.mark.parametrize("items, capacity, expected", [
        ([(3,6), (2,8), (4,7)], 8, 15),
        ([(4,18), (1,3), (4,9)], 5, 21),
        ([(1,300), (20,10), (3,6),(2,8),(4,7)], 5, 318)
        ])
    def test_get_max_profit(self, items, capacity, expected):
        print(items)
        ks = KnapsackSolution()
        r = ks.get_highest_profit(items,  capacity) 
        
        assert r == expected
    
    
        
        
    


if __name__ == '__main__':
    
    ks = KnapsackSolution()
    
    r = ks.get_highest_profit()
    
    print(r)