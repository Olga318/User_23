#Даны значения величины заработной платы заемщиков банка (zp)
# и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Используя математические операции, посчитать коэффициенты линейной регрессии,
# приняв за X заработную плату (то есть, zp - признак), а за
# y - значения скорингового балла (то есть, ks - целевая переменная).
# Произвести расчет как с использованием intercept, так и без.

import numpy as np
import sklearn

x1 = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y1 = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

b1 = (np.mean(x1*y1) - np.mean(x1)*np.mean(y1))/(np.mean(x1**2)-np.mean(x1)**2)
b0 = np.mean(y1) - b1 * np.mean(x1)
print(b1, b0)
print()
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# X = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
# y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
#
# model = LinearRegression()
# s = s.reshape(-1, 1)     # нет установленной функции
# # array([[35],
# #       [45],
# #       [190],
# #       [200],
# #       [40],
# #       [70],
# #       [54],
# #       [150],
# #       [120],
# #       [110]])
#
# regres = model.fit(s, y)
# print(regres.intercept_)
# print(regres.coef_)


x1 = x1.reshape(10, 1)
y1 = y1.reshape(10, 1)
XTX = x1.T.dot(x1)

XTX_inv = np.linalg.inv(XTX)
b = XTX_inv.dot(x1.T).dot(y1)
print(b)
print()

model = LinearRegression(fit_intercept=False)
model.fit(x1, y1)
const = model.intercept_
beta = model.coef_[0]
print(const, beta)




# Посчитать коэффициент линейной регрессии при заработной плате
# (zp), используя градиентный спуск (без intercept).
x1 = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y1 = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
alpha = 1e-6
b1 = 0.1
n = len(x1)
def mse_(b1):
    return np.sum((b1 * x1 -y1)**2) / n
for i in range(100000):
    b1 -= alpha * (2 / n) * np.sum((b1 * x1 - y1) * x1)
    if i % 5000 ==0:
        print(f'iteration = {i}, b1 = {b1}, mse = {mse_(b1)}')
print('y =', b1, '* x')
print()


# Произвести вычисления как в пункте 2, но с вычислением intercept.
# Учесть, что изменение коэффициентов должно производиться на каждом
# шаге одновременно (то есть изменение одного коэффициента
# не должно влиять на изменение другого во время одной итерации).

x1 = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y1 = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
alpha = 5e-6
b1 = 0.1
b0 = 0.1
n = len(x1)
def mse_2(b0, b1):
    return np.sum((b0 + b1 * x1 -y1)**2) / n
for i in range(1000000):
    y_hat = b0 + b1 * x1
    b1 -= alpha * (2 / n) * np.sum((y_hat - y1) * x1)
    b0 -= alpha * (2 / n) * np.sum(y_hat - y1)
    if i % 100000 == 0:
        print(f'iteration = {i}, b0 = {b0}, b1 = {b1}, mse = {mse_2(b0, b1)}')
print(f'y ={b0} + {b1} * x')







