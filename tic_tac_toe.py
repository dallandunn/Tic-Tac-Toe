import random
import time

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
        self.values[location - 1] = value

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
        self.results = {'X':0, 'O':0, 'Ties':0}
        self.num_games = 0
    
    def print_stats(self):
        for winner, num_wins in self.results.items():
            if winner == 'X' or winner == 'O':
                print(f'Number of {winner} wins: {num_wins}, Win%: {round(100 * num_wins/self.num_games,2)}%')
            else:
                print(f'Number of {winner}: {num_wins}, Tie%: {round(100 * num_wins/self.num_games, 2)}%')

    
    def game_over(self):
        replay = input('Play Again? (Y/N)')
        if replay.lower() == 'y':
            self.Board.reset()
            self.Board.show()
            self.game_status = True
        else:
            print('Thanks for playing!')
            self.print_stats()
            quit()
    
    def track_wins(self, winner):
        self.num_games += 1
        self.results[winner] += 1

    def check_game_end(self):
        # check for 3 in rows
        for i in range(0, 9, 3):
            if self.Board.values[i] == self.Board.values[i+1] == self.Board.values[i+2]:
                print(f'Game Over! {self.Board.values[i]} won!')
                self.track_wins(self.Board.values[i])
                self.game_status = False
                self.game_over()

        # check for 3 in cols
        for i in range(3):
            if self.Board.values[i] == self.Board.values[i+3] == self.Board.values[i+6]:
                print(f'Game Over! {self.Board.values[i]} won!')
                self.track_wins(self.Board.values[i])
                self.game_status = False
                self.game_over()
         
        # check for 3 diagnal
        if self.Board.values[0] == self.Board.values[4] == self.Board.values[8]:
            print(f'Game Over! {self.Board.values[0]} won!')
            self.track_wins(self.Board.values[0])
            self.game_status = False
            self.game_over()

        if self.Board.values[2] == self.Board.values[4] == self.Board.values[6]:
            print(f'Game Over! {self.Board.values[2]} won!')
            self.track_wins(self.Board.values[2])
            self.game_status = False
            self.game_over()

        # check if no spaces left
        if not any([value.isnumeric() for value in self.Board.values]):
            print('Game Tied! No spaces left.')
            self.track_wins('Ties')
            self.game_status = False
            self.game_over()

    def turn(self, player_symbol, player_choice):
        if self.game_status:
            self.Board.update(player_symbol, player_choice)
            self.Board.show()
            self.check_game_end()
        
    def player_turn(self, player_symbol):
        player_input = ''
        print(f'Player {player_symbol} turn')
        # ensure that player input is an acceptable value
        while player_input not in range(1, 10):
            player_input = input('Choose a space: ')
            if player_input.isnumeric():
                if int(player_input) > 0 and int(player_input) < 10:
                    try:
                        if self.Board.values[int(player_input) - 1].isnumeric():
                            self.turn(player_symbol, int(player_input))
                            break
                        else:
                           print('This space has already been chosen. Please choose another space.') 
                           
                    except IndexError:
                        print('Please enter a number between 1 and 9.')
                else:
                    print('Please enter a number between 1 and 9.')
            else:
                print('Please enter a number.')
    
    def play(self, player1_symbol='X', player2_symbol='O'):
        # set up number of players
        num_players = ''
        while num_players != 1 and num_players != 2:
            num_players = input('How many players?')
            try:
                num_players = int(num_players)
                if num_players > 2 or num_players < 1:
                    print('This game can only be played with 1 or 2 players.')
            except:
                print('Please enter either 1 or 2.')

        # for 1 player 
        if num_players == 1:
            while self.game_status:
                # player turn
                try:
                    self.player_turn(player1_symbol)
                except:
                    break

                # CPU turn
                try:
                    print('CPU turn...')
                    time.sleep(1.5)
                    
                    # find all spaces that are not taken and randomly choose one of those spaces
                    available_spaces = [space for space in self.Board.values if space.isnumeric()]
                    cpu_choice = random.choice(available_spaces)

                    self.turn(player2_symbol, int(cpu_choice))
                except:
                    break
        
        # for 2 players
        elif num_players == 2:
            while self.game_status:
                # player 1 turn
                self.player_turn(player1_symbol)

                # player 2 turn
                self.player_turn(player2_symbol)

Board = GameBoard()
TicTacToe = Game(Board)
TicTacToe.play()

