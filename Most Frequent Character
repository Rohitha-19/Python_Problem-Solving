class Solution:
    def getMaxOccuringChar(self, s):
        # code here
        freq = {}
        # Count frequency of each character
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        # Find the maximum occurring character
        ans = ''
        maxi = 0
        for ch in sorted(freq):
            if freq[ch] > maxi:
                maxi = freq[ch]
                ans = ch
        return ans
