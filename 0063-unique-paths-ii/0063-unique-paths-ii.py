class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        
        dp = [[0]*c for i in range(r)]
        
        for i in range(c):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1
            else:
                break
        for i in range(r):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[-1][-1]
