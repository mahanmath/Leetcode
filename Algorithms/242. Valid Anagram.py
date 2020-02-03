class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(s == t):
            return True
        MyHash = {}
        
        for char in s:
            if(char not in MyHash):
                MyHash[char] = 1
            else:
                MyHash[char] += 1
        
        for char in t:
            if(char not in MyHash):
                return False
            else:
                MyHash[char] -= 1
        
        return(all([v == 0 for v in MyHash.values()]))