class Board

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
        puts "Board Reset"
        print_board
    end
end

new_board = Board.new()