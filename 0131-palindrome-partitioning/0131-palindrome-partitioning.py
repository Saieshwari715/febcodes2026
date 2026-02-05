class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[]
        path=[]
        def ispal(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def bt(st):
            if st==len(s):
                res.append(path[:])
                return
            for end in range(st,len(s)):
                if ispal(st,end):
                    path.append(s[st:end+1])
                    bt(end+1)
                    path.pop()
        bt(0)
        return res

            

