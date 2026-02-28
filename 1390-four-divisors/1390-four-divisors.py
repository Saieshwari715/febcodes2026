from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        s1=0
        for i in nums:
            d=[]
            s=0
            for j in range(1, int(i**0.5)+1):   # FIXED LOOP
                if i%j==0:
                    d.append(j)
                    s+=j

                    if j != i//j:
                        d.append(i//j)
                        s+=i//j

                    if len(d)>4:
                        break

            if len(d)==4:
                s1+=s
        return s1