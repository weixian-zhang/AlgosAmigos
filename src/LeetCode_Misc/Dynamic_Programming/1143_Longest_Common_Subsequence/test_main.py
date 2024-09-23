

import pytest
from main import Solution


text1_1 = 'abc'
text1_2 = 'abcde'

text2_1 = 'abc'
text2_2 = 'ace'

@pytest.mark.parametrize('text1', [text1_1, text1_2])
@pytest.mark.parametrize('text2', [text2_1, text2_2])
def test_longest_subsequence(text1, text2):
    s=  Solution()
    result = s.longestCommonSubsequence(text1, text2)
    
    assert result == 3
    