class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1]!=1:
            return False
        dp={stone:[] for stone in stones}
        dp[0].append(0)
        for stone in stones:
            for j in dp[stone]:
                for step in ((j-1,j,j+1)):
                    if step>0 and step+stone in dp:
                        if step not in dp[step+stone]:
                            dp[step+stone].append(step)
        if len(dp[stones[-1]])>0:
            return True
        else:
            return False
