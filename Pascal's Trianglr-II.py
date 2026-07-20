#LEETCODE PROBLEM

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
 
Constraints:
0 <= rowIndex <= 33

#Program
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        value = 1

        for k in range(1, rowIndex + 1):
            value = value * (rowIndex - k + 1) // k
            row.append(value)

        return row

Time Complexity:
O(n) 

#Output:
rowIndex = 3
[1, 3, 3, 1]

#Approach:

Initialize the row with 1.
Use the binomial coefficient formula to calculate each next element from the previous one.
Append each computed value to the list.
Return the completed row.

Time Complexity: O(n)
Space Complexity: O(1) (excluding the output list)
