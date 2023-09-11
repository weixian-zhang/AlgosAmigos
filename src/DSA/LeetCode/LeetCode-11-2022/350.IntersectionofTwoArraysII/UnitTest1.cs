namespace _350.IntersectionofTwoArraysII;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        int[] nums1 = new int[] { 4,9,5};
        int[] nums2 = new int[] { 9,4,9,8,4};

        var s = new Solution();

        int[] r = s.Intersect(nums1, nums2);
    }
    
}

public class Solution {
    public int[] Intersect(int[] nums1, int[] nums2) 
    {
        var setNums1 = new HashSet<int>(nums1);
        var setNums2 = new HashSet<int>(nums2);

        var intersectingNums = setNums1.Intersect(setNums2).ToDictionary<int,int>(x => x);

        //no intersecting numbers return empty array
        if(intersectingNums == null)
            return new int[]{};
        
        var result = new List<int>();

         foreach (int key in intersectingNums.Keys)
         {
            var nums1IntersectingNumCount = nums1.Count(x => x == key);
            var nums2IntersectingNumCount = nums2.Count(x => x == key);
            int interNumCountBothArray = (nums1IntersectingNumCount + nums2IntersectingNumCount);

            int addCount = 0;

            //always take the lower count
            if(nums1IntersectingNumCount >= nums2IntersectingNumCount)
            {
                addCount = nums2IntersectingNumCount;
            }
            else
                 addCount= nums1IntersectingNumCount;

            foreach(int x in Enumerable.Range(0, addCount))
            {
                result.Add(key);
            }
        }

        return result.ToArray();
    }
}