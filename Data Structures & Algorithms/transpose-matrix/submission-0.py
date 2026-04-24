class Solution:
    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        outer = [0] * cols
        for i in range(cols):
            inner = [0] * rows
            for j in range(rows):
                inner[j] = matrix[j][i]
            outer[i] = inner
        return outer  