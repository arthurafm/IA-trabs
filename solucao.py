from typing import Iterable, Set, Tuple


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
        isEstadoEqual = self.estado == other.estado
        isPaiEqual = self.pai == other.pai
        isAcaoEqual = self.acao == other.acao
        isCustoEqual = self.custo == other.custo
        return isEstadoEqual and isPaiEqual and isAcaoEqual and isCustoEqual

    def __hash__(self):
        return hash((self.estado, self.pai, self.acao, self.custo))


def sucessor(estado:str)->Set[Tuple[str,str]]:
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

    def somaHamming(CS, ES):            #Cuerrent State,  End State
    
        OOP = 0     #Ouf Of Place
        
        # OOF qtd
        for x, y in zip(CS, ES):
            if x != y and x != '_':
                OOP += 1
        
        return OOP

    CS = estado                         #Current State
    startNode = Nodo(CS, None, None, 0)     #Node Init
    end = "12345678_"          #end state

    # Priority queues
    openNode = [startNode]
    closedNode = set()

    while openNode:
        # get the less expensive node
        currentNode = min(openNode, key=lambda node: node.custo + somaHamming(node.estado, end))

        # Is it the end state?
        if currentNode.estado == end:
            return currentNode.acao
        else:
            openNode.remove(currentNode)
            closedNode.add(currentNode.estado)

            successors = expande(currentNode)

            for successor in successors:
                existing_node = next((node for node in openNode if node.estado == successor.estado), None)
                if existing_node:
                    if successor.custo < existing_node.custo:
                        openNode.remove(existing_node)
                        openNode.append(successor)
                else:
                    openNode.append(successor)

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

    CS = estado                         # Current State
    startNode = Nodo(CS, None, None, 0)  # Node Init
    end = "12345678_"          # end state

    # Priority queues
    openNode = [startNode]
    closedNode = set()

    while openNode:
        # get the less expensive node
        currentNode = min(openNode, key=lambda node: node.custo + distManhattan(node.estado, end))

        # Is it the end state?
        if currentNode.estado == end:
            return currentNode.acao
        else:
            openNode.remove(currentNode)
            closedNode.add(currentNode.estado)

            successors = expande(currentNode)

            for successor in successors:
                existing_node = next((node for node in openNode if node.estado == successor.estado), None)
                if existing_node:
                    if successor.custo < existing_node.custo:
                        openNode.remove(existing_node)
                        openNode.append(successor)
                else:
                    openNode.append(successor)

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
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def dfs(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_new_heuristic(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
