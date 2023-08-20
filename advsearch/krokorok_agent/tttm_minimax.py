from typing import Tuple
# Absoluto -> Teste nesse arquivo
from advsearch.tttm.gamestate import GameState
from advsearch.tttm.board import Board
from minimax import minimax_move
# Relativo -> Teste no arquivo-teste
# from ..tttm.gamestate import GameState
# from ..tttm.board import Board
# from .minimax import minimax_move



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


if __name__ == '__main__':
    board = Board()
    state = GameState(board, 'B')

    # configura a funcao minimax pra receber o estado, profundidade ilimitada e a funcao de utilidade definida no agente
    move = minimax_move(state, -1, utility)
    print(move)
