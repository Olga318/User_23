
# Даны значения зарплат из выборки выпускников:100,80, 75, 77, 89, 33,
# 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов
# наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение, смещенную
# и несмещенную оценки дисперсий для данной выборки.


a =[100,80,75,77,89,33,45,25,65,17,30,24,57,55,70,75,65,84,90,150]

mean = sum(a)/len(a)
print("Математическое ожидание -", mean)
s2m = sum((i - mean)**2 for i in a)/len(a)
print("Смещенная выборочная дисперсия = ", s2m)
s2n = sum((i - mean)**2 for i in a)/(len(a)-1)
print("Несмещенная выборочная дисперсия = ", s2n)
print("Стандартное отклонение -", s2m**0.5)
print()

#В первом ящике находится 8 мячей, из которых 5 - белые.
# Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
# Какова вероятность того, что 3 мяча белые?

A1 = 8
B1 = 5
A2 = 12
B2 = 5
k1 = 2
k2 = 4

# (ББ*ББББ)

p1 = (B1/A1)*((B1-1)/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((B2-2)/(A2-2))*((B2-3)/(A2-3))
result_1 = p1

# (ББ*БББЧ)
p2 = (B1/A1)*((B1-1)/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((B2-2)/(A2-2))*((A2-B2)/(A2-3))
# (ББ*ББЧБ)
p3 = (B1/A1)*((B1-1)/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((A2-B2)/(A2-2))*((B2-2)/(A2-3))
# (ББ*БЧББ)
p4 = (B1/A1)*((B1-1)/(A1-1)) * (B2/A2)*((A2-B2)/(A2-1))*((B2-1)/(A2-2))*((B2-2)/(A2-3))
# (ББ*ЧБББ)
p5 = (B1/A1)*((B1-1)/(A1-1)) * (A2-B2)/A2 * (B2/(A2-1))*((B2-1)/(A2-2))*((B2-2)/(A2-3))

# (БЧ*ББББ)
p6 = (B1/A1)*((A1-B1)/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((B2-2)/(A2-2))*((B2-3)/(A2-3))
# (БЧ*БББЧ)
p7 = (B1/A1)*((A1-B1)/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((B2-2)/(A2-2))*((A2-B2)/(A2-3))
# (БЧ*ББЧБ)
p8 = (B1/A1)*((A1-B1)/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((A2-B2)/(A2-2))*((B2-2)/(A2-3))
# (БЧ*БЧББ)
p9 = (B1/A1)*((A1-B1)/(A1-1)) * (B2/A2)*((A2-B2)/(A2-1))*((B2-1)/(A2-2))*((B2-2)/(A2-3))
# (БЧ*ЧБББ)
p10 = (B1/A1)*((A1-B1)/(A1-1)) * (A2-B2)/A2 * (B2/(A2-1))*((B2-1)/(A2-2))*((B2-2)/(A2-3))

# (ЧБ*ББББ)
p11 = ((A1-B1)/A1)*(B1/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((B2-2)/(A2-2))*((B2-3)/(A2-3))
# (ЧБ*БББЧ)
p12 = ((A1-B1)/A1)*(B1/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((B2-2)/(A2-2))*((A2-B2)/(A2-3))
# (ЧБ*ББЧБ)
p13 = ((A1-B1)/A1)*(B1/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((A2-B2)/(A2-2))*((B2-2)/(A2-3))
# (ЧБ*БЧББ)
p14 = ((A1-B1)/A1)*(B1/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((A2-B2)/(A2-2))*((B2-2)/(A2-3))
# (ЧБ*ЧБББ)
p15 = ((A1-B1)/A1)*(B1/(A1-1)) * (A2-B2)/A2 * (B2/(A2-1))*((B2-1)/(A2-2))*((B2-2)/(A2-3))


# (ЧЧ*ББББ)
p16 = ((A1-B1)/A1) * (((A1-B1)-1)/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((B2-2)/(A2-2))*((B2-3)/(A2-3))
# (ЧЧ*БББЧ)
p17 = ((A1-B1)/A1) * (((A1-B1)-1)/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((B2-2)/(A2-2))*((A2-B2)/(A2-3))
# (ЧЧ*ББЧБ)
p18 = ((A1-B1)/A1) * (((A1-B1)-1)/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((A2-B2)/(A2-2))*((B2-2)/(A2-3))
# (ЧЧ*БЧББ)
p19 = ((A1-B1)/A1) * (((A1-B1)-1)/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))*((A2-B2)/(A2-2))*((B2-2)/(A2-3))
# (ЧЧ*ЧБББ)
p20 = ((A1-B1)/A1) * (((A1-B1)-1)/(A1-1)) * (A2-B2)/A2 * (B2/(A2-1))*((B2-1)/(A2-2))*((B2-2)/(A2-3))


result_2 = p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12+p13+p14+p15+p16+p17+p18+p19+p20

print(f'Вероятность что 3 мяча белые = {result_2*100 :.2f}%')
print()



# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
# Вероятность попадания для первого спортсмена равна 0.9,
# для второго — 0.8, для третьего — 0.6.
# Найти вероятность того, что выстрел произведен: a). первым спортсменом
# б). вторым спортсменом в). третьим спортсменом.

X1 = 0.9
X2 = 0.8
X3 = 0.6

P1 = (X1*1)/(X1*1+X2*1+X3*1)
P2 = (X2*1)/(X1*1+X2*1+X3*1)
P3 = (X3*1)/(X1*1+X2*1+X3*1)

print(f"Вероятность попадания первым спортсменом = {P1*100 :.2f}%")
print(f"Вероятность попадания вторым спортсменом  = {P2*100 :.2f}%")
print(f"Вероятность попадания третьим спортсменом  = {P3*100 :.2f}%")
print()


# В университет на факультеты A и B поступило равное количество студентов,
# а на факультет C студентов поступило столько же, сколько на A и B вместе.
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7, а для студента
# факультета C - 0.9. Студент сдал первую сессию.
# Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?

m1 = 0.25
m2 = 0.25
m3 = 0.5

y1 = 0.8
y2 = 0.7
y3 = 0.9


P4 = (y1*m1)/((m1*y1)+(m2*y2)+(m3*y3))
P5 = (y2*m2)/((m1*y1)+(m2*y2)+(m3*y3))
P6 = (y3*m3)/((m1*y1)+(m2*y2)+(m3*y3))
print(f"Вероятность, что сдавший студент с факультета А  = {P4*100 :.2f}%")
print(f"Вероятность, что сдавший студент с факультета В  = {P5*100 :.2f}%")
print(f"Вероятность, что сдавший студент с факультета С  = {P6*100 :.2f}%")
print()



# Устройство состоит из трех деталей. Для первой детали вероятность выйти из
# строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25.
# Какова вероятность того, что в первый месяц выйдут из строя: а). все детали
# б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?


n1 = 0.1
n2 = 0.2
n3 = 0.25

PN0 = n1*n2*n3

PN1 = n1*n2*(1-n3)
PN2 = n1*(1-n2)*n3
PN3 = (1-n1)*n2*n3

PN4 = n1*(1-n2)*(1-n3)
PN5 = (1-n1)*n2*(1-n3)
PN6 = (1-n1)*(1-n2)*n3



PH1 = PN1+PN2+PN3     #только 2 детали выдут из строя
PH2 = PN1+PN2+PN3+PN4+PN5+PN6+PN0  # хотябы одна деталь
PH3 = PN1+PN2+PN3+PN4+PN5+PN6  # от одной до двух деталей

print(f"Вероятность, что все три детали выйдут из строя  = {PN0*100 :.2f}%")
print(f"Вероятность, что любые две детали выйдут из строя  = {PH1*100 :.2f}%")
print(f"Вероятность, что хотя бы одна деталь выйдет из строя  = {PH2*100 :.2f}%")
print(f"Вероятность, что выйдут из строя от одной до двух  = {PH3*100 :.2f}%")




