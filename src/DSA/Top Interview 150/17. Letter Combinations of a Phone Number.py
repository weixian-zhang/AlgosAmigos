class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        if not digits:
            return []
    
        numCharMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
                   }

        if len(digits) == 1:
             return numCharMap[digits]
        
        result = []
        chars = []

        for x in digits:
            chars.append(numCharMap[x])

        self.backtrack(0, chars.copy(), [], result, len(digits))

        return result

    def backtrack(self, idx: int, chars: list[str], combo: list[str], result: list[str], lenOfCombo: int):
            
            # base cases
            if len(combo) == lenOfCombo:
                 result.append(''.join(x for x in combo.copy()))
                 return

            for c in chars[idx]:

                combo.append(c)

                self.backtrack(idx + 1, chars, combo, result, lenOfCombo)

                combo.pop()

           


s = Solution()
print(s.letterCombinations('23'))
print(s.letterCombinations('234'))