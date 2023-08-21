import random
from typing import Tuple

class Node:

    exploration_coef = 0.7

    def __init__(self, state, father):
        self.sons = []
        self.wins = 0
        self.games = 0
        self.state = state
        self.father = father


    def successors(s) -> Set:
        successorsSet = set()

        for move in s.legal_moves():
            successorsSet.add((s.next_state(move), move))

        return successorsSet

    def evaluate(self):
        if self.state is None:
            return float('-inf')
        elif self.games == 0:
            return float('inf')
        else:
            return (self.wins / self.games) + 2*exploration_coef*sqrt((2*math.log(self.father.games))/self.games)


    def selection(node):
        while(node.sons != []):
            prefered_son = Node(None, None)
            for newNode in node.sons:
                if newNode.evaluate() > prefered_son.evaluate():
                    prefered_son = newNode
            node = prefered_son
        return node
    
    
    def expansion(self, state):
        newNode = Node(state, self)
        self.sons.push(newNode)


    def simulation(self, state, player):
        while(!state.is_terminal()):
            state = random.choice(successors(state))
        if state.winner == player:
            return 1
        elif state.winner == None:
            return 0.5
        else:
            return 0


    def retropropag(node, result):
        while (node.father != None):
            node.wins += result
            node.games += 1
            node = node.father
     




def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    The game is not specified, but this is MCTS and should handle any game, since
    their implementation has the same interface.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """



