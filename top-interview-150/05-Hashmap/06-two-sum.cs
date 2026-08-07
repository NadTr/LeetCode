public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> numMap = new Dictionary<int, int>();
        int num1, num2;
        for(int i = 0; i < nums.Length; i++)
        {
            num1 = nums[i];
            num2 = target -  num1;
            if(numMap.ContainsKey(num2))
            {
                return [i, numMap[num2]];
            }
            else
            {
                numMap[num1] = i;
            }
        }
        return [];
    }
}