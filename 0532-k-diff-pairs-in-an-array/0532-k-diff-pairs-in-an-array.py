class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        seen=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
               
                if i!=j and abs(nums[i]-nums[j])==k:
                    p=tuple(sorted([nums[i],nums[j]]))
                    seen.add(p)

        return len(seen)

        