class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c=0
        d={'a':0,'b':0,'c':0}
        l=0
        for r in range(len(s)):
            d[s[r]]+=1
            while d['a']>0 and d['b']>0 and d['c']>0:
                c+=len(s)-r
                d[s[l]]-=1
                l+=1
        return c
        