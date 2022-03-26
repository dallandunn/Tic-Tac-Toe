class Board
    attr_reader :board

    def initialize
        @board = (1...10).to_a
        print_board
    end

    private

    def print_board
        for index in (1...@board.length + 1) do
            if index % 3 != 0
              print "#{@board[index - 1]} | " 
            elsif index != 9
              print "#{@board[index - 1]} \n"
              print "---------- \n" 
            else 
                print "#{@board[index - 1]} \n"
                puts ""
            end
        end
    end

    public

    def update_board(index, symbol)
        if index > @board.length - 1
            puts "Error: selection not on board."
        else
            @board[index] = symbol
            print_board
        end
    end

    def reset
        @board = (1...10).to_a
        puts "Board Reset \n \n"
        print_board
    end
end

class Game
    def initialize(game_board)
        @winner = false
        @game_board = game_board
        puts "Welcome to Tic-Tac-Toe!"
        print "Press [Enter] to start."
        gets.chomp
        puts "How many players?"
        @num_players = 0

        while @num_players > 2 || @num_players <= 0
            @num_players = gets.chomp.to_i
            if @num_players > 2 || @num_players <= 0
                print "This game can only be played with 1 or 2 players. Try again:"
            end
        end

        if @num_players == 2
            puts "Player 1 will be X's and Player 2 will be O's."
        else
            puts "Player 1 will be X's and the computer will be O's."
        end
    end

    private

    def player_turn(player_num, symbol)
        puts "Player #{player_num}: Choose a space on the board"
        selectiion = 0

        while not selectiion.between?(1, 9)
            selectiion = gets.chomp.to_i

            if not selectiion.between?(1, 9)
                print "Please choose a number on the board. Try again:"
            elsif not @game_board.board.include?(selectiion)
                print "This spot is taken. Try again:"
                selectiion = 0
            end
        end

        @game_board.update_board(selectiion - 1, symbol)
        check_for_winner
    end

    def computer_turn(symbol)
        puts "Computer's Turn..."
        selectiion = 0

        while not selectiion.between?(1, 9)
            selectiion = rand(1...9)
            if not @game_board.board.include?(selectiion)
                selectiion = 0
            end
        end

        @game_board.update_board(selectiion - 1, symbol)
        check_for_winner
    end


    def check_for_winner
        # check of 3 in a row horizontally
        for i in (0...9).step(3)
            if @game_board.board[i] == @game_board.board[i + 1] && @game_board.board[i] == @game_board.board[i + 2]
                puts "Three #{@game_board.board[i]}'s in a row!"
                @winner = true
            end
        end
        # check for 3 in a row vertically
        for i in (0...2)
            if @game_board.board[i] == @game_board.board[i + 3] && @game_board.board[i] == @game_board.board[i + 6]
                puts "Three #{@game_board.board[i]}'s in a row!"
                @winner = true
            end
        end
        # check for 3 in a row diagnally
        if @game_board.board[0] == @game_board.board[4] && @game_board.board[0] == @game_board.board[8]
            puts "Three #{@game_board.board[0]}'s in a row!"
            @winner = true
        end

        if @game_board.board[2] == @game_board.board[4] && @game_board.board[2] == @game_board.board[6]
            puts "Three #{@game_board.board[0]}'s in a row!"
            @winner = true
        end

        #check if there are no more spaces left
        if @game_board.board.none? {|spaces| spaces.is_a? Integer}
            puts "There are no spaces left. It is a tie."
            @winner = true
        end
    end

    public

    def play
        while not @winner
            if @num_players == 2
                player_turn(1, "X")
                player_turn(2, "O")
            else
                player_turn(1, "X")
                computer_turn("O")
            end
        end
        puts "Game Over. Thanks for Playing!"
    end
end

for i in (0...9).step(3)
    puts i
end

ttt_board = Board.new()
tic_tac_toe = Game.new(ttt_board)
tic_tac_toe.play