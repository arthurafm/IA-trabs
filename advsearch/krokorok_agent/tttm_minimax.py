from typing import Tuple
from ..tttm.gamestate import GameState
from ..tttm.board import Board
from .minimax import minimax_move



def make_move(state: GameState) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax para o estado de jogo fornecido.
    :param state: estado para fazer a jogada
    :return: tupla (int, int) com as coordenadas x, y da jogada (lembre-se: 0 é a primeira linha/coluna)
    """

    return minimax_move(state, -1, utility)

def utility(state: GameState, player:str) -> float: # Passou o teste!
    """
    Retorna a utilidade de um estado (terminal) 
    """

    winner = state.winner()

    if winner is None:
        return 0                 # segue o jogo
    elif winner == player:
        return 1                 # ganhou
    else:
        return -1                # perdeu
