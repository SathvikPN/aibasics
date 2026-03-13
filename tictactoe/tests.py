import unittest
from tictactoe import *

class TestInitialState(unittest.TestCase):
    def test_default_grid(self):
        """Should return a 3x3 grid of EMPTY."""
        expected = [[EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(initial_state(), expected)

class TestPlayer(unittest.TestCase):
    def test_empty_board(self):
        """X should start on an empty board."""
        board = initial_state()
        self.assertEqual(player(board), X)

    def test_after_one_move(self):
        """O should move after X has moved."""
        board = [[X, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(player(board), O)

    def test_after_two_moves(self):
        """X should move after O has moved."""
        board = [[X, EMPTY, EMPTY],
                 [EMPTY, O, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(player(board), X)

class TestAction(unittest.TestCase):
    def test_empty_board(self):
        """Empty board should have 9 possible actions."""
        board = initial_state()
        self.assertEqual(len(actions(board)), 9)

    def test_partially_filled_board(self):
        """Filled cells should not be in actions."""
        board = initial_state()
        y, x = 0, 1
        board[y][x] = O
        self.assertNotIn((y, x), actions(board))
        self.assertIn((0, 0), actions(board))
        self.assertEqual(len(actions(board)), 8)

class TestResult(unittest.TestCase):
    def test_making_move(self):
        """Result should place the correct player's mark."""
        board = initial_state()
        action = (1, 1)
        result_board = result(board, action)
        self.assertEqual(result_board[1][1], X)

    def test_result_immutability(self):
        """Result should not mutate the original board."""
        board = initial_state()
        board_copy = [row[:] for row in board]
        action = (1, 1)
        result(board, action)
        self.assertEqual(board, board_copy, "Original board was mutated!")

class TestWinner(unittest.TestCase):
    def test_row_winner(self):
        board = [[X, X, X],
                 [O, O, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(winner(board), X)

    def test_column_winner(self):
        board = [[O, X, EMPTY],
                 [O, X, EMPTY],
                 [O, EMPTY, EMPTY]]
        self.assertEqual(winner(board), O)

    def test_diagonal_winner(self):
        board = [[X, O, EMPTY],
                 [EMPTY, X, O],
                 [EMPTY, EMPTY, X]]
        self.assertEqual(winner(board), X)

    def test_no_winner(self):
        board = [[X, O, X],
                 [X, O, O],
                 [O, X, EMPTY]]
        self.assertIsNone(winner(board))

class TestTerminal(unittest.TestCase):
    def test_not_terminal(self):
        board = initial_state()
        self.assertFalse(terminal(board))

    def test_terminal_full(self):
        board = [[X, O, X],
                 [X, O, O],
                 [O, X, X]]
        self.assertTrue(terminal(board))

    def test_terminal_win(self):
        """Game should be terminal if someone has won, even if not full."""
        board = [[X, X, X],
                 [O, O, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
        self.assertTrue(terminal(board))

class TestUtility(unittest.TestCase):
    def test_x_wins(self):
        board = [[X, X, X],
                 [O, O, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(utility(board), 1)

    def test_o_wins(self):
        board = [[O, O, O],
                 [X, X, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(utility(board), -1)

    def test_tie(self):
        board = [[X, O, X],
                 [X, O, O],
                 [O, X, X]]
        self.assertEqual(utility(board), 0)

if __name__ == '__main__':
    unittest.main()
