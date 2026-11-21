
# https://leetcode.com/problems/encode-and-decode-strings/

from typing import List

class Codec:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        encoded = []
        l = len(strs)
        for i in range(l):

            ascii_str = '-'.join([str(ord(c)) for c in strs[i]]) if strs[i] else 'NUL'
            separator = '_'
            if i != l - 1:
                encoded.append(ascii_str + separator)
            else:
                encoded.append(ascii_str)

        return ''.join(encoded)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        temp = s.split('_')
        decoded = []

        for chars in temp:
            if chars == 'NUL':
                decoded.append("")
                continue
            ascii_chars = chars.split('-')
            chars_decoded = ''.join([chr(int(c)) for c in ascii_chars])
            decoded.append(chars_decoded)
        
        return decoded



dummy_input = ["Hello","World"]
#dummy_input = ["",""]
codec = Codec()
print(codec.decode(codec.encode(dummy_input)))