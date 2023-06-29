IA-trab1

Integrantes do grupo
Arthur Alves Ferreira Melo - 00333985

Carlos Negri - 00333174

Thiago Parisotto Dias - 00313306

Yasmin Katerine Beer Zebrowski - 00277765

Turma 

Rede Neural de Uma Camada
Para as funções desenvolvidas, foram setados os valores:
-b = 1.16
-w = -3.45
-alpha = 0.01
-num_iterations = 10000

Mudanças nos valores de b e w não são percebidas pelo resultado, convergindo sempre para o mesmo valor.
Reduções em alpha mudam levemente o resultado, valores abaixo de 0.01 tem um EQM maior por 7*10^-15. Já aumentos em alpha fazem com que a rede neural divirja a partir de 0.012.
Mudanças em num_iterations não alteram o resultado em fatores mais relevantes que a ordem 10^15.

O erro quadrático médio ótimo obtido por tais configurações é 8.527708190982557

Tensorflow/Keras

Características dos datasets
Quantas classes, quantas amostras e qual o tamanho das imagens (altura x largura x canais de cor)?

MNIST
O conjunto de dados contém 60.000 imagens de treinamento e 10.000 imagens de teste, todas em preto e branco, com 28x28 pixels.

FASHION MNIST
O conjunto de dados contém 70.000 imagens em escala de cinza de 28x28 pixels de produtos de moda de 10 categorias, provenientes de um conjunto de dados de imagens de artigos da Zalando, com 7.000 imagens por categoria. O conjunto de treinamento consiste em 60.000 imagens e o conjunto de teste consiste em 10.000 imagens.

CIFAR10
Este conjunto de dados é composto por 60.000 imagens coloridas de 32x32 pixels em 10 classes, com 6.000 imagens por classe. Há 50.000 imagens de treinamento e 10.000 imagens de teste. 

CIFAR100
Este conjunto de dados é composto por 60.000 imagens coloridas de 32x32 pixels em 100 classes, com 600 imagens por classe. Por classe, há 500 imagens de treinamento e 100 imagens de teste.


Conclusões considerando as seguintes questões

1) Em quais datasets um perceptron simples (sem convolução e sem camadas ocultas) obtém uma acurácia acima de 80%?

Apenas MNIST, embora Fashion MNIST quase chegue em 80%.

MNIST
Loss: 239.5882 - Accuracy: 0.8882

Fashion MNIST
Loss: 1429.0972 - Accuracy: 0.7943

CIFAR10
Loss: 106239.5547 - Accuracy: 0.1586

CIFAR100
Loss: nan - Accuracy: 0.0100

2) Qual a acurácia máxima obtida no CIFAR-10? Qual modificação teve maior impacto positivo? Qual o maior desafio/dificuldade?

Acurácia máxima obtida foi 39,87%.
Adição de duas convoluções 2D com ativação sigmóide, mais MaxPool2D e duas camadas ocultas Dense aumentou a acurácia (0.3987) e diminuiu o loss (1.6561). Alterando o número de neurônios de 5 para 10 não alterou significativamente os resultados. Alterando a ativação para relu, obtivemos acurácia de 0.3346 e 1.6963 de perda, ou seja, também não foi significativamente melhor. Logo, aumentar o número de neurônios e usar ativação sigmóide foram os impactos positivos que observamos.

3) Foi possível obter mais de 60% de acurácia no CIFAR-100? Qual modificação teve maior impacto positivo? Qual o maior desafio/dificuldade?

Acurácia máxima obtida foi 1%, e sem modificar o número máximo de neurônios não conseguimos nenhum resultado diferente. A perda não é um número.


4) Quais fatores (tanto das próprias redes quanto dos dados) levam as redes neurais a melhorarem o desempenho? E quais fatores tornam o desempenho pior?
