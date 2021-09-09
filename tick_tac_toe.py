class GameBoard:
    def __init__(self):
        self.values = [str(i) for i in range(1, 10)]


    def show(self):
        self.board = '\n'
        for i in range(1,10):
            if i % 3 != 0:
                self.board += self.values[i-1] + ' | '
            else:
                self.board += self.values[i-1] + '\n'
                if i !=9:
                    self.board += ('-' * 10) + '\n'
        self.board += '\n'
        print(self.board, end='\r')

    def update(self, value, location):
        if location <= 9:
            if self.values[location - 1].isnumeric():
                self.values[location - 1] = value
                
            else:
                print('This space has already been chosen. Please choose another space.')
        else:
            print('Please enter a number that is on the board.')

    def reset(self):
        print('Game Board has been reset.')
        self.__init__()

class Game:
    def __init__(self, GameBoard):
        self.Board = GameBoard
        self.game_status = True
        print('Welcome to Tick Tac Toe!')
        input('Press [Enter] to start')
        self.Board.show()
    
    def game_over(self):
        replay = input('Play Again? (Y/N)')
        if replay.lower() == 'y':
            self.Board.reset()
            self.Board.show()
            self.game_status = True
        
    def check_game_end(self):
        # check for 3 in rows
        for i in range(0, 9, 3):
            if self.Board.values[i] == self.Board.values[i+1] == self.Board.values[i+2]:
                print(f'Game Over! {self.Board.values[i]} won!')
                self.game_status = False
                self.game_over()

        # check for 3 in cols
        for i in range(3):
            if self.Board.values[i] == self.Board.values[i+3] == self.Board.values[i+6]:
                print(f'Game Over! {self.Board.values[i]} won!')
                self.game_status = False
                self.game_over()
         
        # check for 3 diagnal
        if self.Board.values[0] == self.Board.values[4] == self.Board.values[8]:
            print(f'Game Over! {self.Board.values[0]} won!')
            self.game_status = False
            self.game_over()

        if self.Board.values[2] == self.Board.values[4] == self.Board.values[6]:
            print(f'Game Over! {self.Board.values[2]} won!')
            self.game_status = False
            self.game_over()

        # check if no spaces left
        if not any([value.isnumeric() for value in self.Board.values]):
            print('Game Tied! No spaces left.')
            self.game_status = False
            self.game_over()

    def turn(self, player_symbol, player_choice):
        if self.game_status:
            self.Board.update(player_symbol, player_choice)
            self.Board.show()
            self.check_game_end()
        
    

Board = GameBoard()
TickTacToe = Game(Board)
while TickTacToe.game_status:
    player_input = input('Choose a space:')
    TickTacToe.turn('X', int(player_input))

        


