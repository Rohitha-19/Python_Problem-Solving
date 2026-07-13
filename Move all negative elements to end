class Solution:
    def segregateElements(self, arr):
        # code here
        temp = []
        # Add positive and zero elements first
        for i in arr:
            if i >= 0:
                temp.append(i)
        # Add negative elements
        for i in arr:
            if i < 0:
                temp.append(i)
        # Copy back to original array
        for i in range(len(arr)):
            arr[i] = temp[i]
