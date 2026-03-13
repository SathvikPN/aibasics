"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state() -> list[list[str|None]]:
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board: list[list[str|None]]) -> str|None:
    """
    Returns player who has the next turn on a board.
    """
    empty_count = 0
    for row in board:
        empty_count += sum(cell == EMPTY for cell in row)
    
    return X if (empty_count & 1) else O


def actions(board: list[list[str|None]]) -> set[tuple[int,int]]:
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_cells = set()
    for y in range(3):
        for x in range(3):
            if board[y][x] == EMPTY:
                empty_cells.add((y,x))
    return empty_cells


def result(board: list[list[str|None]], action: tuple[int,int]) -> list[list[str|None]]:
    """
    Returns the board that results from making move (i, j) on the board.
    """
    y, x = action
    if y<0 or x<0 or y>2 or x>2:
        raise Exception("action position out of bound")
    if board[y][x] is not EMPTY:
        raise Exception("Invalid action")
    
    # new_board = [row[:] for row in board] # deep copy
    new_board = copy.deepcopy(board)
    new_board[y][x] = player(board)
    return new_board


def winner(board: list[list[str|None]]) -> str|None:
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # row winner if any
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] is not EMPTY:
            return board[i][0]
        
        # column winner if any 
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] is not EMPTY:
            return board[0][i]
        
    # diagonal winner if any 
    if board[1][1] is not EMPTY:
        if (board[0][0] == board[1][1] == board[2][2]) or \
           (board[0][2] == board[1][1] == board[2][0]):
            return board[1][1]
    
    return None


def terminal(board: list[list[str|None]]) -> bool:
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or len(actions(board)) == 0


def utility(board: list[list[str|None]]) -> int:
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_player = winner(board)
    if win_player == X:
        return 1
    if win_player == O:
        return -1
    return 0


def minimax(board: list[list[str|None]]):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None 

    if player(board) == X:
        # wants to maximise endgame
        maxx = -math.inf
        best_action: tuple[int,int]|None = None
        for action in actions(board):
            process_board = result(board, action)
            endgame_value:int = adversarial_search(process_board)
            if endgame_value > maxx:
                maxx = endgame_value
                best_action = action 
                if maxx == 1:
                    break
        return best_action


        
        
            

def adversarial_search(board: list[list[str|None]]) -> int:
    """
    Returns endgame value of board
    """
    if terminal(board):
        return utility(board)
    
    best_action = minimax(board)
    next_board = result(board, best_action)