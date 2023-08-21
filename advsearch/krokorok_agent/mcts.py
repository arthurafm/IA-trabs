import random
from typing import Tuple

def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    The game is not specified, but this is MCTS and should handle any game, since
    their implementation has the same interface.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo retorna uma jogada ilegal
    # Remova-o e coloque a sua implementacao do MCTS

class Node:

    def __init__(self):
        self.sons = []
        self.wins = 0
        self.games = 0
        self.state = None


    def evaluate(self, state):

    
    def successors(s) -> Set:
        successorsSet = set()
        for move in s.legal_moves():
            successorsSet.add((s.next_state(move), move))
        return successorsSet


    def selection(self, state):
        while(!state.is_terminal()):
            prefered_son = None
            for(newS, newA) in successors(state):
                if self.evaluate(newS) > self.evaluate(prefered_son):
                    prefered_son = newS
            state = prefered_son
        return state
    
    
    def expansion:


    def simulation(self, state, player):
        while(!state.is_terminal()):
            state = random.choice(successors(state))
        if state.winner == player:
            return 1
        else:
            return 0


    def retropropag:
    
     




