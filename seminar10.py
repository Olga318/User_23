# Провести дисперсионный анализ для определения того, есть ли
# различия среднего роста среди взрослых футболистов,
# хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

y1 = np.array([173, 175, 180, 178, 177, 185, 183, 182])
y2 = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
y3 = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

k = 3
n = len(y1)+len(y2)+len(y3)
print(n)
y1_mean = np.mean(y1)
print("Средний рост футболистов ", y1_mean)
y2_mean = np.mean(y2)
print("Средний рост хоккеистов ", y2_mean)
y3_mean = np.mean(y3)
print("Средний рост штангистов ", y3_mean)

#total = np.array([y1,y2,y3])

total = np.array([[173, 175, 180, 178, 177, 185, 183, 182,
        177, 179, 180, 188, 177, 172, 171, 184, 180,
        172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]])
y_total_mean = np.mean(total)
print("Средний рост всех спортсменов  ", y_total_mean)

S_total = np.sum((total - y_total_mean)**2)
print(S_total)
S_f = np.sum((y1_mean - y_total_mean)**2)*len(y1) \
      + np.sum((y2_mean - y_total_mean)**2)*len(y2) \
      + np.sum((y3_mean - y_total_mean)**2)*len(y3)
print(S_f)

S_ost = np.sum((y1-y1_mean)**2)+np.sum((y2-y2_mean)**2)+np.sum((y3-y3_mean)**2)
print(S_ost)

D_f = S_f / (k-1)
print("Дисперсия факторная ", D_f)
D_ost = S_ost / (n-k)
print("Дисперсия остаточная ", D_ost)

F_n = D_f/D_ost
print(F_n)


f = stats.f_oneway(y1,y2,y3)
print(f)
print("Табличное значение  ", 3.38)

#наблюдаемое значение больше табличного,
# следовательно выявлены статистически значимые значения.

