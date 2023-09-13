# https://www.youtube.com/watch?v=mGfK-j9gAQA

class KnapsackSolution:
    
    def get_highest_profit(self, items=[(3,6), (2,8), (4,7)], capacity = 8):
        
        max_profit = 0
        
        def _backtrack(items, current_capacity, current_profit):
            
            if len(items) == 0 or current_capacity == 0:
                return current_profit
            
            for item in items:
                
                item_weight = item[0]
                item_profit = item[1]
                
                if current_capacity - item_weight > 0:
                    pass
                
                       
        
        items_with_highest_profit = _backtrack(items, capacity, 0)
        
        return items_with_highest_profit
    


if __name__ == '__main__':
    
    ks = KnapsackSolution()
    
    r = ks.get_highest_profit()
    
    print(r)