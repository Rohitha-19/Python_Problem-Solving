#Missing Numbers (LEETCODE)
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

#PROGRAM/CODE

#Sum Approach (Optimal):
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual
#OUTPUT:
Input: nums =[3,0,1]
Output: 2
---

#XOR Approach:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i ^ nums[i]
        return missing
---

#Sorting Approach:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
---

#Hash Set Approach:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in s:
                return i
              
#Time Complexity:
Approach | Time |	Space	
Sum Formula:	O(n)	O(1)	
XOR:	O(n)	O(1)	
Sorting:	O(n log n)	O(1)
Hash Set:	O(n)	O(n)
