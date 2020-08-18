class TicTacToe:
    def __init__(self):
        self._board = [[' '] * 3 for n in range(3) ]
    
    def __getitem__(self,x):
        return self._board[x]

    def __str__(self):
        temp = ''
        for n in self._board:
            temp += f' {n[0]} | {n[1]} | {n[2]} \n-----------\n'
        temp = temp.rsplit("\n", 2)[0]
        if self._win_check('x'):
            temp += 'X WON'
            return temp

        if self._win_check('o'):
            temp += 'O WON'
            return temp
        return temp
        
    def _win_check(self,mark):
        board = self._board
        #horizontal
        for i in range(3):
            #vertical
            if set([self._board[n][i] for n in range(3)]) == set(mark):
                return True
            #horizontal
            if set(board[i]) == set(mark):
                return True
        #diagonals
        statement =  mark == board[0][0] == board[1][1] == board[2][2] or mark == board[0][2] == board[1][1] == board[2][0]
        return True if statement else False

board = TicTacToe()
while True:
    board[int(input('player 1 enter y:')) - 1][int(input('player 1 enter x:'))  - 1] = 'x'
    board[int(input('player 2 enter y:')) - 1][ int(input('player 2 enter x:'))  - 1] = 'o'
    print(board)
    if board[-3:-1] == 'WON':
        break

