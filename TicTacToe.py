class TicTacToe:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.players = {"Player1": 'X', "Player2": 'O'}
        self.active_player = "Player1"
        self.turn = 1

    def play_move(self, row_index, column_index):
        active_player = self.get_active_player()
        board = self.get_board()
        player_symbol = self.get_player_symbol(active_player)

        if self.is_move_valid(row_index, column_index):
            board[row_index][column_index] = player_symbol
            print(f"Remarks:{self.check_end_of_game(active_player)}")
            self.next_game_turn()
        else:
            raise Exception("Invalid Move")

    def next_game_turn(self):
        active_player = self.active_player
        self.set_next_turn()
        turn = self.get_current_turn()
        if turn<=9:
            if active_player == "Player2":
                new_active_player = "Player1"
            else:
                new_active_player = "Player2"

            self.set_active_player(new_active_player)
        return

    def show_board_state(self):
        for each_row in self.board:
            for each_cell in each_row:
                print(f"|{each_cell}", end="")
            print("|")
        print("\n")
        return

    def show_active_player(self):
        print(self.active_player)
        return

    def check_end_of_game(self, player):
        # Game ends when a player wins or turn is 9
        player_wins = False
        player_symbol = self.players.get(player)

        # This logic checks for horizontal and vertical wins on  the board
        for i in range(3):
            if ((self.board[i][0] == self.board[i][1] == self.board[i][2] == player_symbol)
                    or (self.board[0][i] == self.board[1][i] == self.board[2][i] == player_symbol)):
                player_wins = True
                break

        # This logic checks for diagonal wins on the board
        if ((self.board[0][0] == self.board[1][1] == self.board[2][2] == player_symbol)
                or (self.board[0][2] == self.board[1][1] == self.board[2][0] == player_symbol)):
            player_wins = True

        if player_wins:
            return f"{player} wins"
        elif self.turn == 9:
            return f"Draw"
        return

    def set_active_player(self, new_active_player):
        self.active_player = new_active_player
        return

    def set_next_turn(self):
        turn =self.turn
        turn += 1
        self.turn = turn
        return

    def get_active_player(self):
        active_player = self.active_player
        return active_player

    def get_players(self):
        players = self.players
        return players

    def get_board(self):
        board = self.board
        return board

    def get_player_symbol(self, active_player):
        players = self.get_players()
        player_symbol = players.get(active_player)
        return player_symbol

    def get_current_turn(self):
        turn = self.turn
        return turn

    def is_move_valid(self, row, column):
        cell_exists = True
        if (0 > row > 2) or (0 > column > 2):
            cell_exists = False
        cell_is_empty = self.board[row][column] == ' '
        # because move is valid when cell exists and is empty
        return cell_exists and cell_is_empty