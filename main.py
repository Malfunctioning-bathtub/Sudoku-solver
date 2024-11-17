from board import boards

class Sudoku():
    def __init__(self, board: list[list[int]]) -> None:
        self.board = board
    def validate(self):
        for row in self.board:
            if len(set(abs(i) for i in row if i != 0)) != len([abs(i) for i in row if i != 0]):
                return False
        
        for column in zip(*self.board):
            if len(set(abs(i) for i in column if i != 0)) != len([abs(i) for i in column if i != 0]):
                return False
        
        for xbox in range(3):
            for ybox in range(3):
                subbox = [i[xbox*3:(xbox+1)*3] for i in self.board[ybox*3:(ybox+1)*3]]
                values = [abs(i) for i in sum(subbox, []) if i != 0]
                if len(set(values)) != len(values):
                    return False
        
        return True

test = Sudoku(boards["easiest"])
# print(test.validate())

def solve(sudoku):
    linboard = [cell for row in sudoku.board for cell in row]
    focus = 0
    direction = 1

    print(linboard)

    # while focus <= len(linboard):
    #     elif lineditboard[focus] < 0:
    #         lineditboard


print(solve(test))