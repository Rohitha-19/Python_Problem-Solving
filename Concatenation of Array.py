#Concatenation of Array - LEETCODE
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

#Explanation
What is the question asking?
nums = [1, 2, 1]
The question says:
Create a new array ans such that:
 - First half is nums
 - Second half is also nums

nums = [1,2,1]
First copy  -> [1,2,1]
Second copy -> [1,2,1]
Final answer: [1,2,1,1,2,1]

#Program/Code
Method 1 (Simplest - Python): Python allows concatenating lists using +.

class Solution:
    def getConcatenation(self, nums):
        return nums + nums

Method 2 (Using a Loop): Create an empty array and append each element twice.

class Solution:
    def getConcatenation(self, nums):
        ans = []
        # First copy
        for num in nums:
            ans.append(num)
        # Second copy
        for num in nums:
            ans.append(num)
        return ans

Method 3 (Using Indexes)

class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans

Output: [1,2,1,1,2,1]
Complexity: O(n)
