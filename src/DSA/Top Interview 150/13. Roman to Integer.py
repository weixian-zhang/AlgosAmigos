class Solution:
    def romanToInt(self, s: str) -> int:
        
        sum = 0
        
        symbolMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        
        i = 0
        
        while i < len(s):
            
            twoSymbols = s[i:i+2]
            
            if twoSymbols in symbolMap:
                sum += symbolMap[twoSymbols]
                i += 2
            else:
                oneSymbol = s[i]
                sum += symbolMap[oneSymbol]
                i += 1
                
        return sum
    
    
if __name__ == '__main__':
    s = Solution()
    
    s.romanToInt('MCMXCIV')
    s.romanToInt('LVIII')
    s.romanToInt('III')