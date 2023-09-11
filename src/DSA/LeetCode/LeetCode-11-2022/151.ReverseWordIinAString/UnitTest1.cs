namespace _151.ReverseWordsInAString;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        string test1 = "the sky is blue";
        string test2 = "  hello world  ";
        string test3 = "a good   example";

        var solution = new Solution();

        string r1 = solution.ReverseWords(test1);

        string r2 = solution.ReverseWords(test2);

        string r3 = solution.ReverseWords(test3);

        Assert.True(r1 == "blue is sky the");
        Assert.True(r2 == "world hello");
        Assert.True(r3 == "example good a");
    }
}


public class Solution {
    public string ReverseWords(string s) {
        
        //split by spaces
        var spaceSplitted = s.Split(" ");

        //take elements that does not contain space
        var noSpace = spaceSplitted.Where(x => x != "").ToList();

        
        //reverse order
        noSpace.Reverse();

        string result = string.Join(" ", noSpace);

        return result;
        
    }
}