
# Runtime: 29 ms, faster than 96.93% of Python3 online submissions for Add Binary.
# Memory Usage: 16.5 MB, less than 64.90% of Python3 online submissions for Add Binary.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a,2) + int(b,2)))[2:]
        
        

if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('11', '1'))
    print(s.addBinary('1010', '1011'))
    print(s.addBinary('0', '0'))