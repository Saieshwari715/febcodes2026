class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''n=len(s)
        ml=0
        for i in range(n):
            mf=0
            freq=[0]*26
            for j in range(i,n):
                idx=ord(s[j])-ord('A')
                freq[idx]+=1
                mf=max(mf,freq[idx])
                if(j-i+1)-mf<=k:
                    ml=max(ml,j-i+1)
        return ml'''
        n=len(s)
        ml=0
        mf=0
        l=0
        freq={}
        for r in range(n):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            mf=max(mf,freq[s[r]])
            while (r-l+1)-mf>k:
                freq[s[l]]-=1
                l+=1
            ml=max(ml,r-l+1)
        return ml


            
            