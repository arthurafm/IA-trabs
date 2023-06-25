# IA-trab1

1. Rede neural de uma camada -> Arthur, Thiago
2. Tensorflow/Keras -> Carlos, Yasmin

TP1: https://colab.research.google.com/drive/1oa2sTWlHfHeJNQpv_Ajrr1RADIAxjMIu?usp=sharing

Resultados Tensorflow Docs
https://docs.google.com/document/d/1hkGwCSpr8FMLddkcG_TNUVa3YwbxMDg2bbHlIo9phNQ/edit?usp=sharing

## Tensorflow/Keras

### Características dos datasets
Quantas classes, quantas amostras e qual o tamanho das imagens (altura x largura x canais de cor)?

#### MNIST
O conjunto de dados contém 60.000 imagens de treinamento e 10.000 imagens de teste, todas em preto e branco, com 28x28 pixels.

tf.keras.layers.Conv2D(16, (3,3), activation='sigmoid', input_shape=(28, 28, 1)),
tf.keras.layers.MaxPool2D((2,2), ),
tf.keras.layers.Flatten(input_shape=(28,28)),    
tf.keras.layers.Dense(10, activation=tf.nn.softmax),


#### FASHION MNIST
O conjunto de dados contém 70.000 imagens em escala de cinza de 28x28 pixels de produtos de moda de 10 categorias, provenientes de um conjunto de dados de imagens de artigos da Zalando, com 7.000 imagens por categoria. O conjunto de treinamento consiste em 60.000 imagens e o conjunto de teste consiste em 10.000 imagens.

tf.keras.layers.Conv2D(16, (3,3), activation='sigmoid', input_shape=(28, 28, 1)),
tf.keras.layers.MaxPool2D((2,2), ),
tf.keras.layers.Flatten(input_shape=(28,28)),        
tf.keras.layers.Dense(10, activation='relu'),     
tf.keras.layers.Dense(10, activation='relu'),    
 tf.keras.layers.Dense(10, activation='relu'),     
tf.keras.layers.Dense(10, activation=tf.nn.softmax) 

3 camadas ocultas com ativação relu

#### CIFAR10
Este conjunto de dados é composto por 60.000 imagens coloridas de 32x32 pixels em 10 classes, com 6.000 imagens por classe. Há 50.000 imagens de treinamento e 10.000 imagens de teste.

tf.keras.layers.Conv2D(10, (3,3), activation='sigmoid', input_shape=(32, 32, 3)),
tf.keras.layers.MaxPool2D((2,2), ),
tf.keras.layers.Conv2D(10, (3,3), activation='sigmoid', input_shape=(32, 32, 3)),
tf.keras.layers.MaxPool2D((2,2), ),
tf.keras.layers.Flatten(input_shape=(32,32,3)),       
tf.keras.layers.Dense(10, activation='relu'),     
tf.keras.layers.Dense(10, activation=tf.nn.softmax) 


#### CIFAR100
Este conjunto de dados é composto por 60.000 imagens coloridas de 32x32 pixels em 100 classes, com 600 imagens por classe. Por classe, há 500 imagens de treinamento e 100 imagens de teste.


tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(32, 32, 3)),
tf.keras.layers.MaxPool2D((2,2), ),
tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(32, 32, 3)),
tf.keras.layers.MaxPool2D((2,2), ),
tf.keras.layers.Conv2D(128, (3,3), activation='relu', input_shape=(32, 32, 3)),
tf.keras.layers.MaxPool2D((2,2), ),
tf.keras.layers.Flatten(input_shape=(32,32,3)),       
tf.keras.layers.Dense(256, activation='relu'),    
tf.keras.layers.Dense(10, activation=tf.nn.softmax),



### Conclusões considerando as seguintes questões

##### _1) Em quais datasets um perceptron simples (sem convolução e sem camadas ocultas) obtém uma acurácia acima de 80%?_

Apenas **MNIST**, embora Fashion MNIST quase chegue em 80%.

MNIST
Loss: 239.5882 - Accuracy: 0.8882

Fashion MNIST
Loss: 1429.0972 - Accuracy: 0.7943

CIFAR10
Loss: 106239.5547 - Accuracy: 0.1586

CIFAR100
Loss: nan - Accuracy: 0.0100

#### _2) Qual a acurácia máxima obtida no CIFAR-10? Qual modificação teve maior impacto positivo? Qual o maior desafio/dificuldade?_

Acurácia máxima obtida foi 39,87%.
Adição de duas convoluções 2D com ativação sigmóide, mais MaxPool2D e duas camadas ocultas Dense aumentou a acurácia (0.3987) e diminuiu o loss (1.6561). Alterando o número de neurônios de 5 para 10 não alterou significativamente os resultados. Alterando a ativação para relu, obtivemos acurácia de 0.3346 e 1.6963 de perda, ou seja, também não foi significativamente melhor. Logo, aumentar o número de neurônios e usar ativação sigmóide foram os impactos positivos que observamos.

#### _3) Foi possível obter mais de 60% de acurácia no CIFAR-100? Qual modificação teve maior impacto positivo? Qual o maior desafio/dificuldade?_

Acurácia máxima obtida foi 1%, e sem modificar o número máximo de neurônios não conseguimos nenhum resultado diferente. A perda não é um número.


#### _4) Quais fatores (tanto das próprias redes quanto dos dados) levam as redes neurais a melhorarem o desempenho? E quais fatores tornam o desempenho pior?_
