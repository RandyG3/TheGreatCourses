from random import choice

"""
    < Set up the grid with an initial arrangement of letters
    < Set the User's score to zero
    < Set initial values for other variables, such as the number of rounds
"""


def initializegrid(board):
    # Initialize game
    # Initialize grid
    initializegrid(board)
    # Initialize score
    print('Initializing...')
    global score
    score = 0
    # Initialize turn number
    global turn
    turn = 1
    # Initialize Grid by random value
    for i in range(8):
        for j in range(8):
            board[i][j] = choice(['A', 'B', 'C', 'D', 'E'])


def continuegame(current_score, goalscore = 100):
    """
    < If score is greater than goal, return False
    < Otherwise return True
    """
    print('Checking to see if game should continue')
    if current_score >= goalscore:
        return False
    else:
        return True


def drawboard(board):
    # Display the board to the screen
    print('Drawing Board in drawboard func')
    linetodraw = ""
    # Draw some blank lines first
    print("hi")
    print("**-----------------------------------")
    # now draw some rows from 8 down to 1
    for i in range(7, -1, -1):
        # draw each row
        linetodraw = ""
        for j in range(8):
            linetodraw += ' | ' + board[i][j]
        linetodraw += " |"
        print(linetodraw)
        print("**-----------------------------------")
        global score
        print('Current Score: ', score)


def getmove():
    # Get the move from the user
    print('Getting move')
    move = input("enter move: ")
    return move


def update(board, move):
    # Update the board according to move
    print('Updating the board')


def doround(board):
    """
    < Get move from the user
    < Update the game based on that move
    < Show the user the new state of the grid
    """
    # Perform one round of the game
    # Display the current board
    print("Doing one Round")
    drawboard(board)
    # Get move
    move = getmove()
    # Update board
    update(board, move)
    # Update turn number
    global turn
    turn += 1


def convertlettertocol(col):
    if col == 'a':
        return 0
    elif col == 'b':
        return 1
    elif col == 'c':
        return 2
    elif col == 'd':
        return 3
    elif col == 'e':
        return 4
    elif col == 'f':
        return 5
    elif col == 'g':
        return 6
    elif col == 'h':
        return 7
    else:
        # not a valid column!
        return -1


def swappieces(board, move):
    # swap pieces on board according to move
    print("Swapping Pieces")
    # get original position
    origrow = int(move[1])-1
    origcol = convertlettertocol(move[0])

    # Get adjacent position
    if move[2] == 'u':
        newrow = origrow + 1
        newcol = origcol
    elif move[2] == 'd':
        newrow = origrow
        newcol = origcol - 1
    elif move[2] == 'l':
        newrow = origrow
        newcol = origcol - 1
    elif move[2] == 'r':
        newrow = origrow
        newcol = origcol + 1

    # Swap objects into two positions
    temp = board[origrow][origcol]
    board[origrow][origcol] = board[newrow][newcol]
    board[newrow][newcol] = temp


def removepieces(board):
    # Remove 3-in-a-row and 3-in-a-column
    print("remove Pieces")
    # create board to store remove-or-not
    remove = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]

    # Go through rows
    for i in range(8):
        for j in range(6):
            if board[i][j] == board[i][j+1] and board[i][j] == board[i][j+2]:
                # three in a row are the same
                remove[i][j] = 1
                remove[i][j+1] = 1
                remove[i][j+2] = 1

    # Go through columns
    for i in range(8):
        for j in range(6):
            if board[i][j] == board[i+1][j] and board[i][j] == board[i+2][j]:
                # three in a column are the same
                remove[i][j] = 1
                remove[i+1][j] = 1
                remove[i+2][j] = 1

    # Eliminate those marked
    global score
    removed_any = False
    for i in range(8):
        for j in range(8):
            if remove[i][j] == 1:
                board[i][j] = 0
                score += 1
                removed_any = True
    return removed_any


def droppieces(board):
    # drop pieces to fill in blanks
    print("Dropping pieces")
    for j in range(8):
        # Make list of pieces in the column
        listofpieces = []
        for i in range(8):
            if board[i][j] != 0:
                listofpieces.append(board[i][j])
        # Copy that list into column
        for i in range(len(listofpieces[i])):
            board[i][j] = listofpieces[i]
        # Fill in remainder of column with 0s
        for i in range(len(listofpieces), 8):
            board[i][j] = 0


def fillblanks(board):
    # Fill blanks with random pieces
    print("Filling Blanks")
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                board[i][j] = choice(['A', 'B', 'C', 'D', 'E'])


def update(board, move):
    # Update the board according to move
    swappieces(board, move)
    pieces_eliminated = True
    while pieces_eliminated:
        pieces_eliminated - removepieces()
        droppieces(board)
        fillblanks(board)


# Initialize game
"""
< Set up the grid with an initial arrangement of letters
< Set the user's score to zero
< Set any other variables (such as counter for the turn number) to
    initial values
"""
# State main variables
score = 0
turn = 0
goalscore = 100
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

# initializegrid(board)
print(score, goalscore)

# Loop While game not over - Do a round of the game
while continuegame(score, goalscore):
    # Do a round of the game
        doround(board)
