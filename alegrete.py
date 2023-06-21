import numpy as np


def compute_mse(b, w, data):
    square_error = 0
    for case in data:
        predicted_result = b + w*case[0]
        square_error += pow(case[1] - predicted_result, 2)
    mse = square_error / (data.size / 2)
    return mse


def step_gradient(b, w, data, alpha):
    derivative_w = 0
    derivative_b = 0
    for case in data:
        derivative_w += (b + w*case[0] - case[1]) * case[0]
        derivative_b += b + w*case[0] - case[1]
    derivative_w *= (2/(data.size / 2))
    derivative_b *= (2 / (data.size / 2))
    w = w - alpha*derivative_w
    b = b - alpha*derivative_b
    return b, w


def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    raise NotImplementedError  # substituir pelo seu codigo
