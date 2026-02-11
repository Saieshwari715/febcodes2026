class Solution:
    def reverseVowels(self, s: str) -> str:
        v="aeiouAEIOU"
        a=[]
        for i in s:
            if i in v:
                a.append(i)
        s=list(s)
        i=0
        j=len(a)-1
        while i<len(s):
            if s[i] in v:
                s[i]=a[j]
                j-=1
            i+=1
            
        return "".join(s)
