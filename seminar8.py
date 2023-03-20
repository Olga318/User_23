#
# 1) Даны значения величины заработной платы заемщиков банка (zp)
# и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий,
# а затем с помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных
# отклонений двух признаков, а затем с использованием функций из библиотек numpy и pandas.

import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

Mzp = zp.mean()
Mks = ks.mean()

cov = ((zp - Mzp)*(ks-Mks)).sum()/(len(ks)-1)
print(cov, zp.var(ddof=1), ks.var(ddof=1))
print()

array1 = np.cov(zp, ks, ddof=1)
print(array1)
print()

array2 = np.corrcoef(zp, ks)
print(array2)
print()


# 2) Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.
import numpy as np
from scipy import stats

values = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
n = values.shape[0]

mean = values.mean()
std = values. std(ddof=1)

# print(n, mean, std)

p = 0.95
alpha = 1 - p

t1 = stats.t.ppf(alpha / 2, df=n - 1)
t2 = stats.t.ppf(1 - alpha / 2, df=n-1)

# print(t1, t2)

print(mean + t1 * std / np.sqrt(n), mean + t2 * std / np.sqrt(n))
print()

# 3) Известно, что рост футболистов в сборной распределен нормально с дисперсией
# генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
# среднее выборочное составляет 174.2.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

p3 = 0.95
n3 = 27
mean3 = 174.2
d3 = 25
std3 = np.sqrt(d3)

alpha3 = 1 - p3
t_1 = stats.norm.ppf(alpha3/2)
t_2 = stats.norm.ppf(1 - alpha3 / 2)

print(mean3 + t_1 * std3 / np.sqrt(n3), mean3 + t_2 * std / np.sqrt(n3))







