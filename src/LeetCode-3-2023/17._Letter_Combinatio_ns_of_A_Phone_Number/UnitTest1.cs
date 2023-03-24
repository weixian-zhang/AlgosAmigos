namespace _17._Letter_Combinatio_ns_of_A_Phone_Number;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {

    }
}


public class Solution {

    private Dictionary<int, List<string>> phone = new Dictionary<int, List<string>>();

    public Solution()
    {
        phone.Add(2, new List<string>() { {"a" }, {"b"}, {"c"} });
        phone.Add(3, new List<string>() { {"d" }, {"e"}, {"f"} });
        phone.Add(4, new List<string>() { {"g" }, {"h"}, {"i"} });
        phone.Add(5 , new List<string>() { {"j" }, {"k"}, {"l"} });
        phone.Add(6, new List<string>() { {"m" }, {"n"}, {"o"} });
        phone.Add(7, new List<string>() { {"p" }, {"q"}, {"r"}, "s" });
        phone.Add(8, new List<string>() { {"t" }, {"u"}, {"v"} });
        phone.Add(9, new List<string>() { {"w" }, {"x"}, {"y"}, {"z"} });
    }
    
    // https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
    
    public IList<string> LetterCombinations(string digits) 
    {
        if (digits == "") {
            return new List<string>();
        }

        if (digits.Length == 1) {
            int num = int.Parse(digits);
            return phone[num];
        }

        var result = new List<string>();
        var source = new List<string>();
        var toCombine = new List<string>();
        
        for(int i = 0; i < digits.Length; i++)
        {
            if(i + 1 <= digits.Length)
            {
                int sourceNum = i;
                int combineNum = i + 1;

                source = phone[sourceNum];
                toCombine = phone[combineNum];

                Backtrack(source, toCombine, result, new List<string>());
            }
        }

        return result;
        
    }

    private void Backtrack(List<string> source, List<string> toCombine, List<string> result, List<string> combinations)
    {
        //base case

        //recurse case
    }
}