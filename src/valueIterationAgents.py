# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
import copy

import mdp, util
from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0

        new_values = copy.deepcopy(self.values)

        for i in range(iterations):
            for state in self.mdp.getStates():
                max_q_value = float('-inf')
                # Para cada ação possível em cada estado, descobre o maior Q-Value possível
                for action in self.mdp.getPossibleActions(state):
                    q_value = self.computeQValueFromValues(state, action)
                    if q_value >= max_q_value:
                        max_q_value = q_value
                # Se não for um estado final, atualiza o vetor de valores/estado
                if not self.mdp.isTerminal(state):
                    new_values[state] = max_q_value
            self.values = copy.deepcopy(new_values)


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        # Recompensa imediata
        reward = self.mdp.getReward(state, None, None)

        # Para todos os estados e probabilidades para a ação dada, calcula o somatório de gamma * probabilidade * valor
        for new_state, probability in self.mdp.getTransitionStatesAndProbs(state, action):
            reward += self.discount * probability * self.values[new_state]

        return reward


    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        chosen_action = None

        # Caso seja final, retorna None
        if not self.mdp.isTerminal(state):
            # Valor máximo inicial é -infinito
            max_value = float('-inf')
            # Computa o Q-Value para todas as ações possíveis e seleciona de maior Q-Value
            for action in self.mdp.getPossibleActions(state):
                value = self.computeQValueFromValues(state, action)
                if value > max_value:
                    max_value = value
                    chosen_action = action

        # Retorna a ação de maior Q-Value
        return chosen_action

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
