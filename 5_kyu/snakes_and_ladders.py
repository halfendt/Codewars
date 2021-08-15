class SnakesLadders():
    """
    Snakes and Ladders Kata
    https://www.codewars.com/kata/587136ba2eefcb92a9000027/
    """
    def __init__(self):
        self.board_dict = {2:38, 7:14, 8:31, 15:26, 16:6, 21:42, 28:84, 36:44, 46:25, 49:11, 51:67,
                           62:19, 64:60, 71:91, 74:53, 78:98, 87:94, 89:68, 92:88, 95:75, 99:80}
        self.square1 = 0
        self.square2 = 0
        self.playernew = 1
        self.playerold = 2
    
    def _set_square1(self, square1):
        self.square1 = square1
    
    def _set_square2(self, square2):
        self.square2 = square2

    def _get_player(self):
        return self.playernew
    
    def _set_player(self, playerold, playernew):
        self.playerold = playerold
        self.playernew = playernew

    def play(self, die1, die2):
        if self.square1 == 100: return "Game over!"
        if self.square2 == 100: return "Game over!"
        
        player = self._get_player()
        
        if player == 1:
            die = die1 + die2 + self.square1
            if die in self.board_dict.keys():
                square1 = self.board_dict[die]
            else:
                square1 = die
            self._set_square1(square1)

            if die1 == die2:
                self._set_player(1, 1)
            else:
                self._set_player(1, 2)
            if square1 > 100:
                square1 = 100 - (square1-100)
                if square1 in self.board_dict.keys():
                    square1 = self.board_dict[square1]
                self._set_square1(square1)
            if square1 == 100:
                return f'Player {self.playerold} Wins!'
            else:
                return f'Player {self.playerold} is on square {square1}'

        else:
            die = die1 + die2 + self.square2
            if die in self.board_dict.keys():
                square2 = self.board_dict[die] 
            else:
                square2 = die
            self._set_square2(square2)

            if die1 == die2:
                self._set_player(2, 2)
            else:
                self._set_player(2, 1)
            if square2 > 100:
                square2 = 100 - (square2-100)
                if square2 in self.board_dict.keys():
                    square2 = self.board_dict[square2]
                self._set_square2(square2)
                
            if square2 == 100:
                return f'Player {self.playerold} Wins!'
            else:
                return f'Player {self.playerold} is on square {square2}'