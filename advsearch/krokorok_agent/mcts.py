import math
import random
from typing import Tuple


def successors(s):
    successorsList = []

    for move in s.legal_moves():
        successorsList.append((s.next_state(move), move))

    return successorsList


def move_to_go_to_state(s1, s2):  # Retorna a ação para levar de um estado s1 para um estado s2

    for (newS, move) in successors(s1):
        if newS.board.board == s2.board.board:
            return move

    return None  # Caso não exista, retorna None


def find_unexplored_state(node):  # Procura um estado inexplorado que não é um sucessor direto do nodo atual
    unexplored_states = set()
    all_successors = set(successors(node.state))

    for son in node.sons:
        explored_successors = set(successors(son.state))
        unexplored_states.update(all_successors - explored_successors)

    if unexplored_states:
        return (random.choice(list(unexplored_states)))[0]
    else:
        return None  # Caso não encontre nenhum


class Node:
    exploration_coef = 0.7

    def __init__(self, state, father):
        self.sons = []
        self.wins = 0
        self.games = 0
        self.state = state
        self.father = father

    def evaluate(self):  # Seleção de filho preferido
        if self.state is None:
            return float('-inf')
        elif self.games == 0:
            return float('inf')
        else:
            return (self.wins / self.games) + 2 * Node.exploration_coef * math.sqrt(
                (2 * math.log(self.father.games)) / self.games)

    def selection(self):
        while self.sons:  # Enquanto nó não for folha
            best_son = max(self.sons, key=lambda x: x.evaluate())
            self = best_son  # Nó recebe o filho preferido
        return self

    def expansion(self, state):  # Adiciona um novo nó na árvore
        newNode = Node(state, self)
        self.sons.append(newNode)

    def simulation(self, player):  # Simula o resto da partida
        state = self.state  # Use the node's state for simulation

        while not state.is_terminal():
            next_states = successors(state)
            state, _ = random.choice(next_states)

        if state.winner() == player:
            return 1
        elif state.winner() is None:
            return 0.5
        else:
            return 0

    def retropropagation(self, result):  # Retropropaga os resultados
        while self.father != None:
            self.wins += result
            self.games += 1
            self = self.father
        self.wins += result
        self.games += 1


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    The game is not specified, but this is MCTS and should handle any game, since
    their implementation has the same interface.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    root = Node(state, None)

    # Número de iterações fixado = 1000
    iterations = 1000

    player = state.player

    for _ in range(iterations):
        node = root

        node = node.selection()

        legal_moves_list = list(node.state.legal_moves())
        if legal_moves_list:
            random_move = random.choice(legal_moves_list)
            new_state = state.next_state(random_move)
            node.expansion(new_state)
            node = node.sons[-1]
        else:  # Se o nodo é uma folha sem movimentos possíveis
            node = node.father
            unexplored_state = find_unexplored_state(node)
            if unexplored_state:
                node.expansion(unexplored_state)
                node = node.sons[-1]

        simulation_result = node.simulation(player)

        node.retropropagation(simulation_result)

    best_son = max(root.sons, key=lambda x: (x.wins / x.games))
    return move_to_go_to_state(best_son.father.state, best_son.state)
