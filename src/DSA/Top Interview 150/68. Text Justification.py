from typing import List

# Runtime: 29 ms, faster than 95.18% of Python3 online submissions for Text Justification.
# Memory Usage: 16.7 MB, less than 67.99% of Python3 online submissions for Text Justification.
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        result = []
        multiline = []

        line = []
        wordCount = 0

        # split word into multiline
        for w in words:

            if (wordCount + len(w)) <= maxWidth:
                
                line.append(w)
                line.append(' ')
            else:
                line.pop()  # remove last ''
                multiline.append(line)

                #reset tracking variables
                line = []
                wordCount = 0

                line.append(w)
                line.append(' ')

            wordCount += len(w) + 1

        if line:
            line.pop()  # remove last ''
            multiline.append(line)

            
        for idx, w in enumerate(multiline):
            # last line
            if idx == len(multiline) - 1:
                result.append(self.left_right_justify_word(w, maxWidth, leftJustify=True))
                break
            
            result.append(self.left_right_justify_word(w, maxWidth))

        return result
    
    def make_spaces(self, numOfSpaces: int,):
        return ''.join([' '] * numOfSpaces)

    # align word left and right in each line
    def left_right_justify_word(self, word: str, maxWidth: int, leftJustify = False):
        
        numOfSpaceToFill = maxWidth - len(''.join(word))

        # last line or single word
        if leftJustify or len(word) == 1:
            newWord = ''.join(word)  + self.make_spaces(numOfSpaceToFill)
            return newWord

        idx = 0
        while numOfSpaceToFill != 0:
            
            for idx in range(len(word)):
                if word[idx].strip() == '':
                    word[idx] += ' '
                    numOfSpaceToFill -= 1

                if numOfSpaceToFill == 0:
                    break
                
                if idx == len(word) - 1:
                    idx = 0
                    break
                
                idx += 1

        return ''.join(word).rstrip()
    

s = Solution()
print(s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
20))

# ["Science  is  what we",
#  "understand      well",
#  "enough to explain to",
#  "a  computer.  Art is",
#  "everything  else  we",
#  "do                  "]

# print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
# print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))

 



                
