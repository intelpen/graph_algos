"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
"""

class Solution:
    def getSquare(self, board: List[List[str]], row_num, col_num) -> List[str]:
        return [x for row in board[row_num * 3:(row_num + 1) * 3]
                for x in row[col_num * 3:(col_num + 1) * 3]
                ]

    def getRow(self, board: List[List[str]], row_num) -> List[str]:
        return board[row_num]

    def getColumn(self, board: List[List[str]], col_num) -> List[str]:
        return [row[col_num] for row in board]

    def verifyDistinct(self, row: List[str]) -> bool:
        row = [x for x in row if x != "."]
        return len(row) == len(set(row))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row must contain the digits 1-9 without repetition.
        for row in board:
            if self.verifyDistinct(row) is False:
                return False
        # Each column must contain the digits 1-9 without repetition.
        for col_num in range(len(board[0])):
            if self.verifyDistinct(self.getColumn(board, col_num)) is False:
                return False
        # Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        for row_num in range(3):
            for col_num in range(3):
                if self.verifyDistinct(self.getSquare(board, row_num, col_num)) is False:
                    return False
        return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solution = Solution()
    print(solution.isValidSudoku(board))