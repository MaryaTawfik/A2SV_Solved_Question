class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat=[[0]*len(matrix) for _ in range(len(matrix))]
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                mat[j][len(matrix) -i-1] = matrix[i][j]
        # return mat
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                matrix[i][j] = mat[i][j]
        return matrix
