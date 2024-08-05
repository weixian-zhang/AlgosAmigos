class Solution:

    # using binary search to search for "closest smallest" number in lookup romanNums
    def intToRoman(self, num: int) -> str:

        romanNums = {
            1 : 'I',
            4 : 'IV',
            5 : 'V',
            9 : 'IX',
            10 : 'X',
            40 : 'XL',
            50 : 'L',
            90 : 'XC',
            100 : 'C',
            400 : 'CD',
            500 : 'D',
            900 : 'CM',
            1000 : 'M',
        }

        keys = list(romanNums.keys())

        result = []
        
        numStr = str(num)
        disectNum = []
        shiftLeftDec = 1
        for x in range(len(numStr)-1, -1, -1):
            disectNum.append(int(numStr[x]) * shiftLeftDec)
            shiftLeftDec *= 10

        disectNum = disectNum[::-1]

        for x in range(len(disectNum)):
            
            n = disectNum[x]

            while n > 0:
                numLookup = self._binary_search_next_smallest_roman_loopup_num(keys, n)
                romanNum = romanNums[numLookup]
                result.append(romanNum)
                n -= numLookup

        return ''.join(result)

    
    def _binary_search_next_smallest_roman_loopup_num(self, keys, target) -> int:

        low, high = 0, len(keys) - 1


        while low <= high:

            mid = high + low // 2

            if keys[mid] == target:
                return keys[mid]
            
            if target > keys[mid]:
                low = mid + 1
            else:
                # return mid - 1
                high = mid - 1

        return keys[mid]
            
        





s = Solution()
# print(s.intToRoman(3))
# print(s.intToRoman(58))
print(s.intToRoman(1994))
print(s.intToRoman(3999))