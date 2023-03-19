
#1) Известно, что генеральная совокупность распределена нормально
# со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания a
# с надежностью 0.95, если выборочная средняя M = 80,
# а объем выборки n = 256.

import scipy.stats as stats
import numpy as np

sig = 16
n = 256
p = 0.95
M = 80
al = 1-p

z1 = stats.norm.ppf(al/2)
z2 = stats.norm.ppf(1-al/2)
print(z1,z2)

a = M + z1*sig/np.sqrt(n)
b = M + z2*sig/np.sqrt(n)
print("Доверительный интервал для оценки математического ожидания от", a,"до",b)
print('*********************')



# 2) В результате 10 независимых измерений некоторой величины X,
# выполненных с одинаковой точностью, получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону
# распределения вероятностей, оценить истинное значение величины X
# при помощи доверительного интервала, покрывающего это
# значение с доверительной вероятностью 0,95.

x2 = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
p2 = 0.95
al2 = 1-p2



X = x2.mean()
sig2 = x2.std(ddof=1)
n2 = x2.shape[0]
print("Среднее арифметическое ", X)
print("Средне квадратическое  ", sig2)
print("Количество выборок ", n2)

t1 = stats.t.ppf(al2/2, df=n2-1)
t2 = stats.t.ppf(1-al2/2, df=n2-1)
print("Критические значения  ", t1,t2)

a2 = X + t1*sig2/np.sqrt(n2)
b2 = X + t2*sig2/np.sqrt(n2)

print("Доверительный интервал для оценки X от", a2,"до",b2)
print('*********************')



# 3) Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для
# разности среднего роста родителей и детей.


x3 = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
y3 = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
p = 0.95
al3 = 1-p
n3 = x3.shape[0]
m3 = y3.shape[0]
x3_mean = x3.mean()
y3_mean = y3.mean()
print("Средние значения по выборкам", x3_mean, y3_mean)
d1 = x3.var(ddof=0)
d2 = y3.var(ddof=0)
print("Дисперсия по выборкам равна ", d1,d2)
D = (d1+d2)/2
print("Обьединенная дисперсия ", D)
s_delta = np.sqrt(D/n3+D/m3)
print("средняя ошибка равна  ", s_delta)

t3 = stats.t.ppf(al3/2, df=2*(n3-1))
t4 = stats.t.ppf(1-al3/2, df=2*(n3-1))
print("Критические значения  ", t3,t4)

left = (x3.mean()-y3.mean())+t3 * s_delta
right = x3.mean()-y3.mean()+t4 * s_delta
print("Доверительный интервал  ", left, right)
