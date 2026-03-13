from typing import Literal, TypedDict, Final

# Constants
X: Final = "X"
O: Final = "O"
EMPTY: Final = None

# Player marks in Tic Tac Toe
type PlayerMark = Literal["X", "O"]

# A single cell on the board can be a player mark or None (empty)
type CellValue = PlayerMark | None

# The board is a 3x3 grid (list of lists)
type Board = list[list[CellValue]]

# An action is represented by (row, column) coordinates
type Action = tuple[int, int]

# A TypedDict to represent the state or result of a game
class GameState(TypedDict):
    board: Board
    next_player: PlayerMark
    is_terminal: bool
    winner: PlayerMark | None
