class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1=float('-inf')
        s1=0
        b2=float('-inf')
        s2=0
        for i in prices:
            b1=max(b1,-i)
            s1=max(s1,b1+i)
            b2=max(b2,s1-i)
            s2=max(s2,b2+i)
        return s2

    