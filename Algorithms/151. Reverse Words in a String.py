class Solution:
    def reverseWords(self, s: str) -> str:
        if(not s.split()):
            return ""
        return "".join(map(lambda x: x+' ', list(s.split())[:0:-1]))+s.split()[0]
