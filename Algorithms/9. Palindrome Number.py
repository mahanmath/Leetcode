class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        y = x
        s = 0
        while(x):
            s = 10*s + (x%10)
            x = x//10
        
        return(y == s)