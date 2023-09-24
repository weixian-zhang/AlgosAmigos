namespace _322.CoinChange;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var s = new Solution();

        int minCoins = s.CoinChange(new int[]{2}, 3);
    }
}

//https://www.youtube.com/watch?v=jgiZlGzXMBw

public class Solution {
    public int CoinChange(int[] coins, int amount) {

        if(amount <= 0)
            return 0;

        if(coins == null || coins.Length == 0)
            return -1;
        
        if(coins.Length == 1)
            if(amount-coins[0] < 0)
                return -1;

        //0,1,2,3,4,5,6,7,8,9,10,11
        int[] minCoinsSubProblem = InitSubCoinProblems(amount);

        minCoinsSubProblem[0] = 0;

        int currentTryUseCoin = 1; //represents use of coin to try [1, 2, 5] coins

        for(int i = 1; i < minCoinsSubProblem.Length; i++)
        {
            int currentSubAmount = i;

            foreach(int coin in coins)
            {   
                int remainer = currentSubAmount - coin;

                if(remainer >= 0)
                {
                    //gets the previously solved coins<->amount sub-problem
                   int prevMinCoins = minCoinsSubProblem[remainer];
                
                   
                   if(prevMinCoins == int.MaxValue)
                        return -1;

                   int currentMinCoinsToUse = prevMinCoins + currentTryUseCoin;

                   //find out next min coin to use remainer
                   minCoinsSubProblem[i] = Math.Min(minCoinsSubProblem[i], currentMinCoinsToUse);
                }
                //example amount is 3 and coin to try is 2, no way coin-2 will addup to 3
                //hence, continue
                else
                    continue;
            }
        }
        
        int minCoinResult = minCoinsSubProblem.Last();
        return minCoinResult == int.MaxValue ? -1 : minCoinResult;
    }

    private int[] InitSubCoinProblems(int amount)
    {
        int lengthOfSubCoinsProblem = amount + 1;
        var r = new List<int>();
        foreach (int x in Enumerable.Range(0, lengthOfSubCoinsProblem))
        {
            r.Add(lengthOfSubCoinsProblem);
        }

        return r.ToArray();
    }
}