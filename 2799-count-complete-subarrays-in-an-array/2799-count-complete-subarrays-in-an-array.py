class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n=set(nums)
        l=0
        dic={}
        c=0
        for r in range(len(nums)):
            if nums[r] in dic:
                dic[nums[r]]+=1
            else:
                dic[nums[r]]=1
            
            while len(dic)==len(n):
                c+=len(nums)-r
                dic[nums[l]]-=1
                if dic[nums[l]]==0:
                    del dic[nums[l]]
                l+=1
        return c


        