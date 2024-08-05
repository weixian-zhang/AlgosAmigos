class Solution:

    # inital solution - cheating by changing to string instead of bit manupulation
    def reverseBits(self, n: int) -> int:
        
        reversedBit = ''.join(list(bin(n)[2:])[::-1])
        reversedBit = reversedBit + ''.join(['0'] * (32 - len(reversedBit)))
        return int(reversedBit, 2)
    
    # using bitwise operation
    def reverseBits(self, n: int) -> int:
        
        reversed = 0
        i = 0

        while i <= 31:
            print(bin(n))

            bit = (n >> i) & 1

            print(bin(n >> i))

            reversed |= (bit << (31 - i))

            print(bin(reversed))

            i += 1

        return reversed


s = Solution()
print(s.reverseBits(11))