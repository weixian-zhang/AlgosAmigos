

from main import Solution

def test_find_unique_paths_in_matrix_3_by_2():
    solution = Solution()
    
    paths = solution.uniquePaths(m=3, n=2)
    
    assert paths == 3
    
def test_find_unique_paths_in_matrix_3_by_7():
    solution = Solution()
    
    paths = solution.uniquePaths(m=3, n=7)
    
    assert paths == 28