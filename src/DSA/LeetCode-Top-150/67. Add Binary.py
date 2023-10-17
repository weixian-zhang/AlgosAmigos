class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        numA = int(a, 2)
        numB = int(b, 2)
        
        sumBin = str(bin(numA + numB))[2:]
        
        return sumBin
        

if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('11', '1'))
    print(s.addBinary('1010', '1011'))
    print(s.addBinary('0', '0'))