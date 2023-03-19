
# Выбрать тест и проверить, есть  ли различия между выборками:
# 1 )  Даны две  независимые выборки. Не соблюдается условие нормальности
# x1  380,420, 290
# y1 140,360,200,900
import numpy as np
import scipy.stats as stats

x1 = np.array([380,420,290])
y1 = np.array([140,360,200,900])
a1=stats.mannwhitneyu(x1, y1)
print(a1)
# H0 Статистически значимых различий нет
print()


# Сделайте вывод по результатам, полученным с помощью функции
# 2 ) Исследовалось влияние препарата на уровень давления пациентов.
# Сначала измерялось давление до приема препарата, потом через 10 минут
# и через 30 минут. Есть ли статистически значимые различия?
# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150,  130, 135
# 3е измерение через 30 минут: 130, 130, 120, 130, 125

x2 = np.array([150, 160, 165, 145, 155])
y2 = np.array([140, 155, 150,  130, 135])
z2 = np.array([130, 130, 120, 130, 125])

a2 = stats.friedmanchisquare(x2, y2, z2)
print(a2)
# H1  Выявлены статистические различия
print()

# 3 ) Сравните 1 и 2 е измерения, предполагая,
# что 3го измерения через 30 минут не было.

a3 = stats.wilcoxon(x2, y2)
print(a3)
# H0   Статистически значимых различий нет
print()


# 4) Даны 3 группы  учеников плавания.
# В 1 группе время на дистанцию 50 м составляют:
# 56, 60, 62, 55, 71, 67, 59, 58, 64, 67
# Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
# Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54
x4 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
y4 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
z4 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

a4 = stats.kruskal(x4, y4, z4)
print(a4)
#  H0   Статистически значимых различий нет
print()


# 5) Заявляется, что партия изготавливается со средним арифметическим 2,5 см.
# Проверить данную гипотезу, если известно, что размеры изделий подчинены
# нормальному закону распределения. Объем выборки 10, уровень статистической
# значимости 5%
# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34

alpha2 = 0.05
n = 10
mu = 2.5
# 5
# H0: mu = 2.5
# H1: mu != 2.5

samples = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
sigma = samples.std(ddof=1)
x_mean = samples.mean()

t1 = stats.t.ppf(alpha2 / 2, df=n-1)
t2 = stats.t.ppf(1-alpha2 / 2, df=n-1)
print(t1, t2)

t_em = (x_mean-mu)/(sigma/np.sqrt(n))
print(t_em)

# H0   Статистически значимых различий нет