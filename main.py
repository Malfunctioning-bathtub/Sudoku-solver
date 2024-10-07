from board import boards

class Soduku():
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

test = Soduku(boards["easiest"])
print(test.validate())

