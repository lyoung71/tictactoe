board = {
    "top-L": ' ', "top-M": " ", "top-R": " ",
    "mid-L": " ", "mid-M": " ", "mid-R": " ",
    "low-L": " ", "low-M": " ", "low-R": " "
    }


def printBoard(board):
    print()
    print(board["top-L"] + '|' + board["top-M"] + '|' + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + '|' + board["mid-M"] + '|' + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + '|' + board["low-M"] + '|' + board["low-R"])
    print()


def tictactoe(board):
    turn = "x"
    for i in range(9):
        printBoard(board)
        print("Turn: " + turn + ". Make a move.")
        move = input()
        while move not in board.keys():
            move = input("Please enter a valid move ")
        board[move] = turn
        # if x wins
        if board["top-L"] == "x" and board["top-M"] == "x" and board["top-R"] \
                == "x":
            printBoard(board)
            return "x wins!"
        elif board["mid-L"] == "x" and board["mid-M"] == "x" and board["mid-R"] \
                == "x":
            printBoard(board)
            return "x wins!"
        elif board["low-L"] == "x" and board["low-M"] == "x" and board["low-R"] \
                == "x":
            printBoard(board)
            return "x wins!"
        elif board["top-L"] == "x" and board["mid-M"] == "x" and board["low-R"] \
                == "x":
            printBoard(board)
            return "x wins!"
        elif board["low-L"] == "x" and board["mid-M"] == "x" and board["top-R"] \
                == "x":
            printBoard(board)
            return "x wins!"
        elif board["top-L"] == "x" and board["mid-L"] == "x" and board["low-L"] \
                == "x":
            printBoard(board)
            return "x wins!"
        elif board["top-M"] == "x" and board["mid-M"] == "x" and board["low-M"] \
                == "x":
            printBoard(board)
            return "x wins!"
        elif board["top-R"] == "x" and board["mid-R"] == "x" and board["low-R"] \
                == "x":
            printBoard(board)
            return "x wins!"
        # o wins
        if board["top-L"] == "o" and board["top-M"] == "o" and board["top-R"] \
                == "o":
            printBoard(board)
            return "o wins!"
        elif board["mid-L"] == "o" and board["mid-M"] == "o" and board["mid-R"] \
                == "o":
            printBoard(board)
            return "o wins!"
        elif board["low-L"] == "o" and board["low-M"] == "o" and board["low-R"] \
                == "o":
            printBoard(board)
            return "o wins!"
        elif board["top-L"] == "o" and board["mid-M"] == "o" and board["low-R"] \
                == "o":
            printBoard(board)
            return "o wins!"
        elif board["low-L"] == "o" and board["mid-M"] == "o" and board["top-R"] \
                == "o":
            printBoard(board)
            return "o wins!"
        elif board["top-L"] == "o" and board["mid-L"] == "o" and board["low-L"] \
                == "o":
            printBoard(board)
            return "o wins!"
        elif board["top-M"] == "o" and board["mid-M"] == "o" and board["low-M"] \
                == "o":
            printBoard(board)
            return "o wins!"
        elif board["top-R"] == "o" and board["mid-R"] == "o" and board["low-R"] \
                == "o":
            printBoard(board)
            return "o wins!"

        if turn == "x":
            turn = "o"
        else:
            turn = "x"


print(tictactoe(board))
