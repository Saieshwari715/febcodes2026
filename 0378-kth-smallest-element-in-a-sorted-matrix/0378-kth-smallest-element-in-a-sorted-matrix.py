class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        a=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                a.append(matrix[i][j])
                a.sort()
        return a[k-1]



        