from random import choice

board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]


def initializegrid(board):
    # Initialize game
    # Initialize grid
    # Initializegrid(board)
    # Iniialize score
    # print('Initializing...')
    global score
    score = 0
    # Initialize turn number
    global turn
    turn = 1
    # Initialize Grid by random value
    for i in range(8):
        for j in range(8):
            board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])


def drawboard(board):
    # Display the board to the screen
    print('Drawing Board')
    linetodraw = ""
    # Draw some blank lines first
    print("\n\n\n")
    print("-----------------------------------")
    # now draw some rows from 8 down to 1
    for i in range(7, -1, -1):
        # draw each row
        linetodraw = ""
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw += " |"
        print(linetodraw)
        print("-----------------------------------")


initializegrid(board)
drawboard(board)
