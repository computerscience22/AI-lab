def solveNQueens(n):
    def backtrack(column):
        if column == n:
            solutions.append(generateBoard(placement))
            return
        
        for row in range(n):
            if is_valid(column, row):
                placement[column] = row
                backtrack(column + 1)
                placement[column] = -1
    
    def is_valid(column, row):
        for prev_col in range(column):
            prev_row = placement[prev_col]
            if prev_row == row or abs(prev_row - row) == abs(prev_col - column):
                return False
        return True
    
    def generateBoard(placement):
        board = []
        for row in range(n):
            board_row = ['.' for _ in range(n)]
            if 0 <= placement[row] < n:
                board_row[placement[row]] = 'Q'
            board.append(''.join(board_row))
        return board
    
    placement = [-1] * n
    solutions = []
    backtrack(0)
    return solutions

if __name__ == "__main__":
    n = 12
    result = solveNQueens(n)
    print(f"Found {len(result)} solutions for {n}-Queens problem:")
    for idx, solution in enumerate(result, 1):
        print(f"Solution {idx}:")
        for row in solution:
            print(row)
        print()