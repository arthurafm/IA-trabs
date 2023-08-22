import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

EVAL_TEMPLATE = [
    [20, -3, 11, 8, 8, 11, -3, 20],
    [-3, -7, -4, 1, 1, -4, -7, -3],
    [11, -4, 2, 2, 2, 2, -4, 11],
    [8, 1, 2, -3, -3, 2, 1, 8],
    [8, 1, 2, -3, -3, 2, 1, 8],
    [11, -4, 2, 2, 2, 2, -4, 11],
    [-3, -7, -4, 1, 1, -4, -7, -3],
    [20, -3, 11, 8, 8, 11, -3, 20]
]

def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # Adota-se profundidade máxima de 4
    return minimax_move(state, 4, evaluate_custom)


# É adotada uma heurística de máscara customizada
def evaluate_custom(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    valuePlayer = 0
    valueOpponent = 0
    board = state.get_board().tiles
    
    for i in range(8):
        for j in range(8):
            if board[i][j] == player:
                valuePlayer += EVAL_TEMPLATE[i][j]
            elif board[i][j] == Board.opponent(player):
                valueOpponent += EVAL_TEMPLATE[i][j]

    return valuePlayer - valueOpponent
