
# https://www.geeksforgeeks.org/print-all-pairs-with-given-sum/
# Given an array of integers, and a number ‘sum’, print all pairs in the array whose sum is equal to ‘sum’.

class Solution():
    
    # my solution
    def printPairs(self, arr: list[int], sum):

        def arr_find(num):
            try:
                return arr.index(num)
            except:
                return -1

        result = []
        diffMap = {}
        
        for x in arr:
            diff = sum - x
            idx = arr_find(diff)
            if idx != -1:
               result.append(tuple((x, arr[idx])))

        print(list(result))

    
    # geek for geek solution
    def printPairs(self, arr, n, sum):
 
        # Store counts of all elements
        # in a dictionary
        mydict = dict()
    
        # Traverse through all the elements
        for i in range(n):
    
            # Search if a pair can be
            # formed with arr[i]
            temp = sum - arr[i]
    
            if temp in mydict:
                count = mydict[temp]
                for j in range(count):
                    print("(", temp, ", ", arr[i],
                        ")", sep="", end='\n')
    
            if arr[i] in mydict:
                mydict[arr[i]] += 1
            else:
                mydict[arr[i]] = 1

            




s = Solution()
# print(s.printPairs([1, 5, 7, -1, 5], 6))

arr = [1, 5, 7, -1, 5]
print(s.printPairs(arr,len(arr), 6))