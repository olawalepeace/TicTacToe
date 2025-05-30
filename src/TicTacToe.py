class TicTacToe:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.players = {"Player1": 'X', "Player2": 'O'}
        self.active_player = "Player1"
        self.turn = 0

    def play_move(self, row_index, column_index):
        self.increment_turn_count()
        active_player = self.get_active_player()
        board = self.get_board()
        player_symbol = self.return_player_symbol(active_player)

        if self.is_move_valid(row_index, column_index):
            board[row_index][column_index] = player_symbol
            self.next_game_turn()
        else:
            raise Exception("Invalid Move")

    def next_game_turn(self):
        active_player = self.active_player
        turn = self.get_current_turn()
        if turn < 9:
            new_active_player = 'Player2' if active_player == 'Player1' else 'Player1'
            self.set_active_player(new_active_player)
        return

    def show_board_state(self):
        for each_row in self.board:
            for each_cell in each_row:
                print(f"|{each_cell}", end="")
            print("|")
        print("\n")
        return

    def print_active_player(self):
        print(self.active_player)
        return

    def check_end_of_game(self):
        # Game ends when a player wins or turn is 9
        there_is_a_winner = False
        turn = self.get_current_turn()
        players = self.get_players()

        # This logic checks for diagonal wins on the board
        if ((self.board[0][0] == self.board[1][1] == self.board[2][2])
                or (self.board[0][2] == self.board[1][1] == self.board[2][0])):
            there_is_a_winner = True
            player_symbol = self.board[1][1]
        else:
            # This logic checks for horizontal and vertical wins on  the board
            for i in range(3):
                if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                    there_is_a_winner = True
                    player_symbol = self.board[i][0]
                    break

                elif self.board[0][i] == self.board[1][i] == self.board[2][i]:
                    there_is_a_winner = True
                    player_symbol = self.board[0][i]
                    break

        if there_is_a_winner:
            for player_name, character in players.items():
                if character == player_symbol:
                    return f"{player_name} wins"
        elif turn == 9:
            return "Draw"
        return

    def determine_cell_occupant(self, cell_index):
        board = self.get_board()
        x, y = cell_index
        return board[x][y]

    def set_active_player(self, new_active_player):
        self.active_player = new_active_player
        return

    def increment_turn_count(self):
        self.turn += 1
        return

    def get_active_player(self):
        return self.active_player

    def get_players(self):
        return self.players

    def get_board(self):
        return self.board

    def return_player_symbol(self, active_player):
        players = self.get_players()
        player_symbol = players.get(active_player)
        return player_symbol

    def get_current_turn(self):
        return self.turn

    def is_move_valid(self, row, column):
        cell_exists = True
        if (0 > row > 2) or (0 > column > 2):
            cell_exists = False
        cell_is_empty = self.board[row][column] == ' '
        # because move is valid when cell exists and is empty
        return cell_exists and cell_is_empty
