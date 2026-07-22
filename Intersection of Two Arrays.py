#Intersection of Two Arrays - LEETCODE

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
  
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

#Program/Code:
  class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

#Explanation:
Convert both arrays into sets to remove duplicates, then use the set intersection (&) operator to find common unique elements. Finally, convert the resulting set back into a list.

#Time Complexity:
Time Complexity: O(n + m)
Space Complexity: O(n + m)
