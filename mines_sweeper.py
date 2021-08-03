from typing import List


class Solution:
    def get_adjacent_mines(self, board, x, y):
        number_of_mines = 0
        for r in range(x-1, x+2):
            for c in range(y-1, y+2):
                if r >=0 and r < len(board) and c >= 0 and c < len(board[r]) and board[r][c] == 'M':
                    number_of_mines += 1
        return number_of_mines
        
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        if not board:
            return []
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            number_of_mines = self.get_adjacent_mines(board, x, y)
            if number_of_mines:
                board[x][y] = str(number_of_mines)
            else:
                board[x][y] = 'B'
                for r in range(x-1, x+2):
                    for c in range(y-1, y+2):
                        if r >=0 and r < len(board) and c >= 0 and c < len(board[r]) and board[r][c] != 'B':
                            self.updateBoard(board, [r, c])
        return board

if __name__ == '__main__':
    board = [
        ["E","E","E","E","E"],
        ["E","E","M","E","E"],
        ["E","E","E","E","E"],
        ["E","E","E","E","E"]]
    click = [3,0]
    s = Solution()
    print(s.updateBoard(board=board, click=click))
