class Solution:
    def frequencyCount(self, arr):
        #  code here
        N= len(arr)
        result= [0] * N
        for num in arr:
            if 1 <= num <= N:
                result[num - 1] += 1
        for i in range(N):
            arr[i]=result[i]
        return arr
            
