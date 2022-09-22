namespace BoyerMoorePatternSearch;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        string toSearch = "This is just a test, yet another test";
        string pattern = "test";

        var bm = new BoyerMoorePatternSearch();
        var r = bm.Search(toSearch, pattern);
    }

    public class BoyerMoorePatternSearch
    {
        // match pattern to SearchText start from last character of pattern

        //if last char matches, continue to find match from right-left, 2nd-last char, 3rd last char
            //if char not match, lookup BatchMatchIndexOffsetTable to find a offset to shift
            //shift pattern forward by offset

        //continue match pattern last-char with SearchText

        BatchMatchIndexOffsetTable _badMatchIndexOffsetTable = new BatchMatchIndexOffsetTable();
        
        public List<PatternMatchResult> Search(string textToSearch, string pattern)
        {
            _badMatchIndexOffsetTable.Init(pattern);

            var result = new List<PatternMatchResult>();

            int lengthToSearch = textToSearch.Length - pattern.Length;
            int skipTo = 0;
            
            for(int textToSearchStartIndex = 0; textToSearchStartIndex <= lengthToSearch; textToSearchStartIndex += skipTo)
            {
                //inner loop only use for matching text to pattern
                for(int patternIndex = pattern.Length - 1; patternIndex >= 0; patternIndex--)
                {
                    int matchCharBackwardsIndex = textToSearchStartIndex + patternIndex; 
                    
                    char currentSearchChar = textToSearch[matchCharBackwardsIndex];
                    char currentPatternChar = pattern[patternIndex];

                    if(currentPatternChar== currentSearchChar)
                    {
                        //found a match from comparing pattern right-left, hence patternIndex is --
                        //0 means all [t] [s] [e] [t] matches
                        if(patternIndex == 0)
                        {
                            int startIndex = textToSearchStartIndex;
                            int endIndex = textToSearchStartIndex + (pattern.Length - 1);
                            result.Add(new PatternMatchResult(startIndex, endIndex));
                        }
                        else
                            continue;
                    }
                    //get index offset to shift
                    else
                    {
                        skipTo = _badMatchIndexOffsetTable.GetOffsetIndexToShift(currentSearchChar);
                        break;

                        //-1 is to prevent extra +1 when outer for loop does textToSearchStartIndex++
                        //without -1 textToSearchStartIndex will skip an extra character
                        //textToSearchStartIndex += skipTo - 1;   
                        
                    }
                }
            }

            return result;
        }
        
    }

    public class PatternMatchResult
    {
        public PatternMatchResult(int startIndex, int endIndex)
        {
            StartIndex = startIndex;
            EndIndex = endIndex;
        }
        public int StartIndex { get; set; }
        public int EndIndex { get; set; }
    }


    public class BatchMatchIndexOffsetTable
    {
        private Dictionary<char,int> _badMatchTable = new Dictionary<char, int>();

        int _patternLength = 0;

        public void Init(string pattern)
        {
            _patternLength = pattern.Length;

            //index {length of pattern} - {index of char} - 1
            for(int i = 0; i < pattern.Length - 1; i++)
            {
                char patternChar = pattern[i];
                int badMatchIndexValue = (pattern.Length - i) - 1;

                _badMatchTable[patternChar] = badMatchIndexValue; //will update index offset if same char found
            }
        }

        public int GetOffsetIndexToShift(char toSearchChar)
        {
            int tosearchMatchCharIndexToShift = 0;
            if(!_badMatchTable.TryGetValue(toSearchChar, out tosearchMatchCharIndexToShift))
            {
                return _patternLength;
            }

            return tosearchMatchCharIndexToShift;
        }
    }
}