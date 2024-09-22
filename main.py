from board import boards

class Soduku():
    def __init__(self, board: list[list[int]]) -> None:
        self.board = board
    def validate(self):
        for row in self.board:
            usedNumbers = []
            for cell in row:
                cell = abs(cell)
                if cell in usedNumbers:
                    return False
                if cell != 0:
                    usedNumbers.append(cell)
        
        for row in zip(*self.board):
            usedNumbers = []
            for cell in row:
                cell = abs(cell)
                if cell in usedNumbers:
                    return False
                if cell != 0:
                    usedNumbers.append(cell)
        
        


test = Soduku(boards["invalid"])
print(test.validate())