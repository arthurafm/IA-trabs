import random
from typing import Tuple, Callable, Set


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

    def successors(s):
        successorsSet = []

        for move in s.legal_moves():
            successorsSet.append((s.next_state(move), move))

        return successorsSet

    def MAX(s, alpha, beta, depth):
        if s.is_terminal() or depth == max_depth:
            return eval_func(s, state.player), None

        v = float('-inf')
        a = None

        for (newS, newA) in successors(s):
            newV, _ = MIN(newS, alpha, beta, depth + 1)
            if newV > v:
                v = newV
                a = newA
            alpha = max(alpha, v)
            if alpha >= beta:
                break

        return v, a

    def MIN(s, alpha, beta, depth):
        if s.is_terminal() or depth == max_depth:
            return eval_func(s, state.player), None

        v = float('inf')
        a = None

        for (newS, newA) in successors(s):
            newV, _ = MAX(newS, alpha, beta, depth + 1)
            if newV < v:
                v = newV
                a = newA
            beta = min(beta, v)
            if beta <= alpha:
                break

        return v, a

    value, action = MAX(state, float('-inf'), float('inf'), 0)

    return action
