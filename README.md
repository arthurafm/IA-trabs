# IA-trab1

## Integrantes do grupo
- Arthur Alves Ferreira Melo - 00333985

- Carlos Negri - 00333174

- Thiago Parisotto Dias - 00313306

- Yasmin Katerine Beer Zebrowski - 00277765

Turma A

## Bibliotecas
Foram utilizadas as seguintes bibliotecas padrões do Python: random, typing e math.

## Avaliação da poda alfa-beta no Tic-Tac-Toe Misere

### Minimax vs Random Player
Foram realizadas 25 partidas entre o Minimax e o Random Player e o resultado foram 13 vitórias para o Minimax e 12 empates.

Portanto, pode-se concluir que o Minimax sempre ganha do Random Player.

### Minimax vs Minimax
Foram realizadas 25 partidas entre o Minimax e o Minimax e o resultado foram 25 empates.

Portanto, pode-se concluir que o Minimax sempre empata com o Minimax.

### Minimax vs Jogadas Perfeitas
Foram realizadas 10 partidas entre o Minimax e as Jogadas Perfeitas do GamesmanUni e o resultado foram 10 empates.

Portanto, pode-se concluir que o Minimax sempre empata com as Jogadas Perfeitas

## Função customizada do Othello
A heurística customizada adotada foi uma heurística de máscara criada por Kartik Kukreja, disponível neste [link](https://github.com/kartikkukreja/blog-codes/blob/master/src/Heuristic%20Function%20for%20Reversi%20(Othello).cpp).

## Critério de parada no Minimax do Othello
Foi adotada um critério de parada com profundidade máxima fixa, de 5 para a heurística do Count e do Mask, e de 4 para a heurística customizada.

## Avaliação da poda alfa-beta no Othello

### Count vs Mask
Foram realizadas 5 partidas entre a heurística do Count vs a heurística do Mask e o resultado foram 5 vitórias do Count, todas por 37 a 27.

Foram realizadas 5 partidas entre a heurística do Mask vs a heurística do Count e o resultado foram 5 vitórias do Count, todas por 38 a 26.

### Count vs Custom
Foram realizadas 5 partidas entre a heurística do Count vs a heurística do Custom o resultado foram 5 vitórias do Custom, todas por 45 a 19.

Foram realizadas 5 partidas entre a heurística do Custom vs a heurística do Count o resultado foram 5 vitórias do Custom, todas por 45 a 19.

### Mask vs Custom
Foram realizadas 5 partidas entre a heurística do Mask vs a heurística do Custom o resultado foram 5 vitórias do Mask, todas por 35 a 29.

Foram realizadas 5 partidas entre a heurística do Custom vs a heurística do Mask o resultado foram 5 vitórias do Custom, todas por 33 a 31.

## Implementação escolhida para o torneio
Para o torneio, foi escolhida a heurística customizada padrão, do jeito no qual foi implementada.

## Feedback

Houve algumas confusões em relação a certas características do algorítimo MinMax.

O uso de IA auxilia somente em algumas situações. Em muitas das vezes a IA recomendava algorítmos errados ou diferentes do objetivo, ela não encontrava os problemas no código ou corrigia coisas que não estavam erradas. No geral, notamos que a IA é uma forte ferramenta auxiliar no desenvolvimento, mas ainda não substitui um desenvolvedor humano.

A documentação sobre as classes já implementadas como GameState e Board poderiam ser melhoradas, a fim de facilitar o processo de entendimento inicial do código.
