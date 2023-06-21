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
    new_b = b
    new_w = w
    list_b = []
    list_w = []
    for i in range(num_iterations):
        new_b, new_w = step_gradient(new_b, new_w, data, alpha)
        list_b.append(new_b)
        list_w.append(new_w)
    return list_b, list_w
