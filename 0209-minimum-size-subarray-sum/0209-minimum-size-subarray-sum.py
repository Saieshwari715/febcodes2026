class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        l=0
        s=0
        mini=float('inf')
        for r in range(n):
            
            s+=nums[r]
            while s>=target:
                
                mini=min(mini,r-l+1)
                
                s-=nums[l]
                l+=1
        return 0 if mini==float('inf') else mini

        