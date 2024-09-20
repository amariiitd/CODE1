# Tic-Tac-Toe game in Python

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if the player has won
def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    
    return False

# Function to check if the board is full (a tie)
def check_tie(board):
    return all([cell != " " for row in board for cell in row])

# Main function to play Tic-Tac-Toe
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 Tic-Tac-Toe board
    players = ["X", "O"]  # Two players, X and O
    current_player = 0  # Index of the current player (0 = X, 1 = O)
    
    while True:
        print_board(board)
        row = int(input(f"Player {players[current_player]}, enter the row (0-2): "))
        col = int(input(f"Player {players[current_player]}, enter the column (0-2): "))
        
        # Check if the chosen cell is valid
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move, try again.")
            continue
        
        # Place the player's move on the board
        board[row][col] = players[current_player]
        
        # Check if the player won
        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        
        # Check if the game is a tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch to the other player
        current_player = 1 - current_player

play_tic_tac_toe()
