"""
Tic Tac Toe Player
"""

import math
import copy

try:
    from .ttt_types import X, O, EMPTY, Board, Action, PlayerMark, GameState
except (ImportError, ValueError):
    from ttt_types import X, O, EMPTY, Board, Action, PlayerMark, GameState


def initial_state() -> Board:
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board: Board) -> PlayerMark:
    """
    Returns player who has the next turn on a board.
    """
    empty_count = 0
    for row in board:
        empty_count += sum(cell == EMPTY for cell in row)
    
    return X if (empty_count & 1) else O


def actions(board: Board) -> set[Action]:
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_cells = set()
    for y in range(3):
        for x in range(3):
            if board[y][x] == EMPTY:
                empty_cells.add((y,x))
    return empty_cells


def result(board: Board, action: Action) -> Board:
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


def winner(board: Board) -> PlayerMark | None:
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


def terminal(board: Board) -> bool:
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or len(actions(board)) == 0


def utility(board: Board) -> int:
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_player = winner(board)
    if win_player == X:
        return 1
    if win_player == O:
        return -1
    return 0


def minimax(board: Board) -> Action | None:
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None 

    if player(board) == X:
        # wants to maximise endgame score
        max_score = -math.inf
        best_action: tuple[int,int]|None = None
        for action in actions(board):
            next_board = result(board, action)
            endgame_value:int = adversarial_search(next_board)
            if endgame_value > max_score:
                max_score = endgame_value
                best_action = action 
                if max_score == 1:
                    break
        return best_action

    if player(board) == O:
        # wants to maximise endgame score
        min_score = math.inf
        best_action: tuple[int,int]|None = None
        for action in actions(board):
            next_board = result(board, action)
            endgame_value:int = adversarial_search(next_board)
            if endgame_value < min_score:
                min_score = endgame_value
                best_action = action 
                if min_score == -1:
                    break
        return best_action

        
        
            

def adversarial_search(board: Board) -> int:
    """
    Returns endgame value of board simulating optimal play from both players
    """
    if terminal(board):
        return utility(board)
    
    if player(board) == X:
        max_score = -math.inf 
        for action in actions(board):
            next_board = result(board, action)
            score = adversarial_search(next_board)
            if score > max_score:
                max_score = score 
                if score == 1:
                    break
        return int(max_score)
    
    if player(board) == O:
        min_score = math.inf 
        for action in actions(board):
            next_board = result(board, action)
            score = adversarial_search(next_board)
            if score < min_score:
                min_score = score 
                if score == -1:
                    break
        return int(min_score)      

    raise Exception("Invalid path for tictactoe rules")  
