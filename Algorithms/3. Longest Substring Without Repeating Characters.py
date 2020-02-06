class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        if(len(s) == 0): return 0
        maxLen = 1
        length = len(s)
        i, j = 0, 0
        while (j + 1 < length):
            while(j+1 < length and s.find(s[j+1], i, j+1) == -1):
                j += 1
            maxLen = max([maxLen, j - i + 1])
            if(j+1 < length):
                i, j = s.find(s[j+1], i, j+1) + 1, j + 1
        return maxLen
