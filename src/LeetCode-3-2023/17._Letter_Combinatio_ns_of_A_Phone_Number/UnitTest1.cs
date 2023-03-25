namespace _17._Letter_Combinatio_ns_of_A_Phone_Number;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var s = new Solution();

        var combo = s.LetterCombinations("234");
    }
}


public class Solution {

    private List<string> result = new List<string>();

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
    public IList<string> LetterCombinations(string digits) {
        
        if (digits == "") {
            return new List<string>();
        }

        if (digits.Length == 1) {
            int num = int.Parse(digits);
            return phone[num];
        }

        var combinations = new List<string>();

        int sourceNum = (int)Char.GetNumericValue(digits[0]);
        List<string> source =  phone[sourceNum];

        Backtrack(0, digits,  combinations);

        return result;
        
    }

    private void Backtrack(int index, string digits,  List<string> combinations)
    {
        if (combinations.Count == digits.Length) {
            string combo = string.Join("", combinations);
            result.Add(combo);
            return;
        }
        

        char nextDigit = digits[index];
        int nextDigitNum = (int)Char.GetNumericValue(nextDigit);
        List<string> toCombineLetters =  phone[nextDigitNum];

        foreach(string letter in toCombineLetters)
        {   
            combinations.Add(letter);

            Backtrack(index + 1, digits, combinations);

            //remove last letter so that next iteration will use the next new letter in letter-set
            combinations.RemoveAt(combinations.Count - 1);
        }
    }
}


//misunderstood combinations to be alternative digits combination
public class Solution1 {

    private Dictionary<int, List<string>> phone = new Dictionary<int, List<string>>();

    public Solution1()
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
            if(i + 1 == digits.Length)
            {
                break;
            }

            int sourceNum = (int)Char.GetNumericValue(digits[i]);
            int combineNum = (int)Char.GetNumericValue(digits[i + 1]);

            source = phone[sourceNum];
            toCombine = phone[combineNum];

            Backtrack(source, toCombine, result, result);
        }

        return result;
        
    }

    private void Backtrack(List<string> source, List<string> toCombine, List<string> result, List<string> combinations)
    {
        //base case

        //recurse case
        foreach(string src in source)
        {
            foreach(string tc in toCombine)
            {
                combinations.Add(src + tc);
            }
        }
    }
}