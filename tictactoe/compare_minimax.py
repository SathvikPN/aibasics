import tictactoe
import math

print("Starting comparison...")

def compare_performance():
    board = tictactoe.initial_state()
    
    print(f"{'Game State':<30} | {'MiniMax Nodes':<15} | {'Alpha-Beta Nodes':<15} | {'Reduction %':<12}")
    print("-" * 80)
    
    # 1. Empty Board
    tictactoe.minimax(board)
    nodes_mm_empty = tictactoe.get_explored_nodes()
    
    tictactoe.minimax_alpha_beta(board)
    nodes_ab_empty = tictactoe.get_explored_nodes()
    
    reduction_empty = (1 - nodes_ab_empty / nodes_mm_empty) * 100
    print(f"{'Empty Board':<30} | {nodes_mm_empty:<15} | {nodes_ab_empty:<15} | {reduction_empty:.1f}%")
    
    # 2. Board with one move (X at center)
    board[1][1] = 'X'
    tictactoe.minimax(board)
    nodes_mm_1 = tictactoe.get_explored_nodes()
    
    tictactoe.minimax_alpha_beta(board)
    nodes_ab_1 = tictactoe.get_explored_nodes()
    
    reduction_1 = (1 - nodes_ab_1 / nodes_mm_1) * 100
    print(f"{'X at (1,1)':<30} | {nodes_mm_1:<15} | {nodes_ab_1:<15} | {reduction_1:.1f}%")

    # 3. Board with two moves (X center, O corner)
    board[0][0] = 'O'
    tictactoe.minimax(board)
    nodes_mm_2 = tictactoe.get_explored_nodes()
    
    tictactoe.minimax_alpha_beta(board)
    nodes_ab_2 = tictactoe.get_explored_nodes()
    
    reduction_2 = (1 - nodes_ab_2 / nodes_mm_2) * 100
    print(f"{'X (1,1), O (0,0)':<30} | {nodes_mm_2:<15} | {nodes_ab_2:<15} | {reduction_2:.1f}%")

if __name__ == "__main__":
    compare_performance()
