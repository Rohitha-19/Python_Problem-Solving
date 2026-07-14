class Solution:
    def replaceWithRank(self, arr):
        temp = []

        # Store value and its original index
        for i in range(len(arr)):
            temp.append((arr[i], i))

        # Sort according to value
        temp.sort()

        # Replace elements with their rank
        for rank in range(len(temp)):
            value, index = temp[rank]
            arr[index] = rank
