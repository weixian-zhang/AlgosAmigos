class Solution:
    def countKeyChanges(self, s: str) -> int:

        kc = 0

        for i in range (len(s)):
            if i + 1 <= len(s) - 1:

                if s[i].lower() != s[i + 1].lower():
                    kc += 1
        
        return kc
    

s = Solution()

print(s.countKeyChanges('mDVD'))
print(s.countKeyChanges('aAbBcC'))
print(s.countKeyChanges('AaAaAaaA'))