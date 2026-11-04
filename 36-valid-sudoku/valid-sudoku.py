class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(len(board)):
            r_seen = set()
            c_seen = set()
            for j in range(len(board[i])):

                if board[i][j] != ".":

                    if board[i][j] in r_seen:
                        return False
                    r_seen.add(board[i][j])
        
                
                if board[j][i] != ".":

                    if board[j][i] in c_seen:
                        return False
                    c_seen.add(board[j][i])

        for i in range(0, 9, 3):
            for q in range(0, 9, 3):
                seen = set()

                for j in range(i, i+3):
                    for p in range(q, q+3):
                        
                        if board[j][p] == ".":
                            continue
                        if board[j][p] in seen:
                            return False
                        
                        seen.add(board[j][p])
        return True
