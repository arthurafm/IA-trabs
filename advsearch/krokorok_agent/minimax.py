import random
from typing import Tuple, Callable


def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    def MAX(state, alpha, beta, depth):
        if state.is_terminal() or depth == max_depth:
            return eval_func(state, state.player)
        v = float('-inf')
        a = None

        for (newS, newA) in state.legal_moves():
            newV, x = MIN(newS, alpha, beta, depth + 1)
            if newV > v:
                v = newV
                a = newA
            alpha = max(alpha, v)
            if alpha >= beta:
                break

        return v, a

    def MIN(state, alpha, beta, depth):
        if state.is_terminal() or depth == max_depth:
            return eval_func(state, state.player)

        v = float('inf')
        a = None

        for (newS, newA) in state.legal_moves():
            newV, x = MAX(state, alpha, beta, depth + 1)
            if newV < v:
                v = newV
                a = newA
            beta = min(beta, v)
            if beta <= alpha:
                break

        return v, a

    depth = 0
    v, a = MAX(state, float('-inf'), float('inf'), depth)
    return a
