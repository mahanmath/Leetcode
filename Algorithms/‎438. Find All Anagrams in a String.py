class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        Lp = len(p)
        Ls = len(s)
        
        if(Ls < Lp): return []
        
        from collections import Counter
        ans=[]
        refSet = Counter(p)
        MySet = Counter(s[:Lp])
        if(MySet == refSet):
                ans.append(0)
        for i in range(1, Ls - Lp + 1):
            #print(MySet, Counter({s[i + Lp - 1]: 1}))
            MySet += Counter({s[i + Lp - 1]: 1})
            MySet -= Counter({s[i - 1]: 1})
            if(MySet == refSet):
                ans.append(i)
            
        return ans