import random
from typing import Tuple
from ..tttm.gamestate import GameState
from ..tttm.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'krokorok_agent' com o nome
# do seu agente.


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax para o estado de jogo fornecido.
    :param state: estado para fazer a jogada
    :return: tupla (int, int) com as coordenadas x, y da jogada (lembre-se: 0 é a primeira linha/coluna)
    """

    return minimax_move(state, -1, utility)

def utility(state: GameState, player:str) -> float:
    """
    Retorna a utilidade de um estado (terminal) 
    """

    if state.board.check_loser is None:
        return 0                # segue o jogo
    elif state.board.check_loser is player:
        return -1               # perdeu
    else:
        return 1                # ganhou
