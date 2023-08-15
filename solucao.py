from typing import Iterable, Set, Tuple

import heapq

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """

    def __init__(self, estado: str, pai, acao: str, custo: int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def __eq__(self, other):
        if self.estado != other.estado:
            return False
        return True

    def __hash__(self):
        return hash(self.estado)

    def __lt__(self, other):
        return self.custo < other.custo


def sucessor(estado: str) -> Set[Tuple[str, str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """

    actionList = []

    if estado[6] != '_' and estado[7] != '_' and estado[8] != '_':
        actionList.append('abaixo')
    if estado[0] != '_' and estado[1] != '_' and estado[2] != '_':
        actionList.append('acima')
    if estado[0] != '_' and estado[3] != '_' and estado[6] != '_':
        actionList.append('esquerda')
    if estado[2] != '_' and estado[5] != '_' and estado[8] != '_':
        actionList.append('direita')

    _index = estado.index('_')
    tupla = set()
    for action in actionList:
        charList = list(estado)
        if action == 'abaixo':
            charList[_index], charList[_index + 3] = charList[_index + 3], charList[_index]
        if action == 'acima':
            charList[_index], charList[_index - 3] = charList[_index - 3], charList[_index]
        if action == 'esquerda':
            charList[_index], charList[_index - 1] = charList[_index - 1], charList[_index]
        if action == 'direita':
            charList[_index], charList[_index + 1] = charList[_index + 1], charList[_index]
        newStr = ''
        for char in charList:
            newStr += char
        tupla.add((action, newStr))
    return tupla


def expande(nodo: Nodo) -> Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    sucessors = sucessor(nodo.estado)

    expansion = set()
    for elem in sucessors:
        node = Nodo(elem[1], nodo, elem[0], nodo.custo + 1)
        expansion.add(node)

    return expansion


def astar_hamming(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """

    def somaHamming(CS, ES):  # Current State,  End State

        OOP = 0  # Ouf Of Place

        # OOF qtd
        for x, y in zip(CS, ES):
            if x != y and x != '_':
                OOP += 1

        return OOP

    startNode = Nodo(estado, None, "", 0)  # Node Init
    end = "12345678_"  # End State

    # Priority queues
    visitedNode = set()
    openNode = [startNode]

    while openNode:
        # get the less expensive node
        currentNode = heapq.heappop(openNode)

        # Is it the end state?
        if currentNode.estado == end:
            actionPath = []
            # Backtracks, adding actions to list, until finds starting node
            while currentNode.custo != 0:
                actionPath.insert(0, currentNode.acao)
                currentNode = currentNode.pai
            return actionPath

        if currentNode not in visitedNode:
            visitedNode.add(currentNode)
            successors = expande(currentNode)

            for successor in successors:
                if successor not in visitedNode:
                    successor.custo += somaHamming(successor.estado, end)
                    heapq.heappush(openNode, successor)
    return None


def astar_manhattan(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """

    # substituir a linha abaixo pelo seu codigo
    def distManhattan(CS, ES):
        dist = 0

        for i in range(len(CS)):
            if CS[i] != '_' and CS[i] != ES[i]:
                Xcs, Ycs = divmod(CS.index(CS[i]), 3)
                Xes, Yes = divmod(ES.index(CS[i]), 3)

                dist += abs(Xcs - Xes) + abs(Ycs - Yes)
        return dist

    startNode = Nodo(estado, None, "", 0)  # Node Init
    end = "12345678_"  # end state

    # Priority queues
    openNode = [startNode]
    visitedNode = set()

    while openNode:
        # get the less expensive node
        currentNode = heapq.heappop(openNode)

        # Is it the end state?
        if currentNode.estado == end:
            actionPath = []
            # Backtracks, adding actions to list, until finds starting node
            while currentNode.custo != 0:
                actionPath.insert(0, currentNode.acao)
                currentNode = currentNode.pai
            return actionPath

        if currentNode not in visitedNode:
            visitedNode.add(currentNode)
            successors = expande(currentNode)

            for successor in successors:
                if successor not in visitedNode:
                    successor.custo += distManhattan(successor.estado, end)
                    heapq.heappush(openNode, successor)

    return None


def bfs(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    startNode = Nodo(estado, None, "", 0)  # Node Init
    end = "12345678_"  # end state

    # Priority queues
    openNode = [startNode]
    visitedNode = set()

    while openNode:
        # get the first node
        currentNode = openNode.pop(0)

        # Is it the end state?
        if currentNode.estado == end:
            actionPath = []
            # Backtracks, adding actions to list, until finds starting node
            while currentNode.custo != 0:
                actionPath.insert(0, currentNode.acao)
                currentNode = currentNode.pai
            return actionPath

        if currentNode not in visitedNode:
            visitedNode.add(currentNode)
            successors = expande(currentNode)

            # Adds new nodes through BFS
            for successor in successors:
                if successor not in visitedNode:
                    openNode.append(successor)

    return None


def dfs(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    startNode = Nodo(estado, None, "", 0)  # Node Init
    end = "12345678_"  # end state

    # Priority queues
    openNode = [startNode]
    visitedNode = set()

    while openNode:
        # get the first node
        currentNode = openNode.pop(0)

        # Is it the end state?
        if currentNode.estado == end:
            actionPath = []
            # Backtracks, adding actions to list, until finds starting node
            while currentNode.custo != 0:
                actionPath.insert(0, currentNode.acao)
                currentNode = currentNode.pai
            return actionPath

        if currentNode not in visitedNode:
            visitedNode.add(currentNode)
            successors = expande(currentNode)

            # Adds new nodes through DFS
            for successor in successors:
                if successor not in visitedNode:
                    openNode.insert(0, successor)

    return None


def astar_new_heuristic(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """

    # Foi escolhida a heurística da Distância de Levenshtein

    def distLevenshtein(token1, token2):
        distances = []
        distances_aux = []
        for i in range(len(token1) + 1):
            for j in range(len(token2) + 1):
                distances_aux.append(0)
            distances.append(distances_aux)

        for t1 in range(len(token1) + 1):
            distances[t1][0] = t1

        for t2 in range(len(token2) + 1):
            distances[0][t2] = t2

        a = 0
        b = 0
        c = 0

        for t1 in range(1, len(token1) + 1):
            for t2 in range(1, len(token2) + 1):
                if (token1[t1 - 1] == token2[t2 - 1]):
                    distances[t1][t2] = distances[t1 - 1][t2 - 1]
                else:
                    a = distances[t1][t2 - 1]
                    b = distances[t1 - 1][t2]
                    c = distances[t1 - 1][t2 - 1]

                    if (a <= b and a <= c):
                        distances[t1][t2] = a + 1
                    elif (b <= a and b <= c):
                        distances[t1][t2] = b + 1
                    else:
                        distances[t1][t2] = c + 1

        return distances[len(token1)][len(token2)]


    startNode = Nodo(estado, None, "", 0)  # Node Init
    end = "12345678_"  # End State

    # Priority queues
    visitedNode = set()
    openNode = [startNode]

    while openNode:
        # get the less expensive node
        currentNode = heapq.heappop(openNode)

        # Is it the end state?
        if currentNode.estado == end:
            actionPath = []
            # Backtracks, adding actions to list, until finds starting node
            while currentNode.custo != 0:
                actionPath.insert(0, currentNode.acao)
                currentNode = currentNode.pai
            return actionPath

        if currentNode not in visitedNode:
            visitedNode.add(currentNode)
            successors = expande(currentNode)

            for successor in successors:
                if successor not in visitedNode:
                    successor.custo += distLevenshtein(successor.estado, end)
                    heapq.heappush(openNode, successor)
    return None