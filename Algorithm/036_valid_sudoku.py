# https://leetcode.com/problems/valid-sudoku/description/

board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def løsning(board):
    rader = board
    kolonner = [[linje[i] for linje in board] for i in range(len(board[0]))] 
    kvadranter = [
        board[0][0:3]+board[1][0:3]+board[2][0:3],
        board[3][0:3]+board[4][0:3]+board[5][0:3],
        board[6][0:3]+board[7][0:3]+board[8][0:3],
        board[0][3:6]+board[1][3:6]+board[2][3:6],
        board[3][3:6]+board[4][3:6]+board[5][3:6],
        board[6][3:6]+board[7][3:6]+board[8][3:6],
        board[0][6:9]+board[1][6:9]+board[2][6:9],
        board[3][6:9]+board[4][6:9]+board[5][6:9],
        board[6][6:9]+board[7][6:9]+board[8][6:9],
    ] 

    for l in [rader, kolonner, kvadranter]:
        for boks_1_9 in l:
            fylte_felter = [e for e in boks_1_9 if e != '.']
            
            if len(set(fylte_felter)) < len(fylte_felter):
                return False
    return True

print(løsning(board))