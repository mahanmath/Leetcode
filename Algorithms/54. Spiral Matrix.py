class Solution:
    def __init__(self):
        self.out = []
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if(matrix):
            self.out += matrix.pop(0)
            self.spiralOrder(list(zip(*matrix))[::-1])
        return self.out
