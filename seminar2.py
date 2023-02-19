# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз.
# Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

import math as m

n = 100  #  number_test
p = 0.8  #  odds_event
k = 85   #  number_event_

random_discrete_P100= (m.factorial(n)/(m.factorial(k)*m.factorial(n-k))) * p**k * (1-p)**(100-k)

print(f'Вероятность меткости стрелка  = {random_discrete_P100*100 :.2f}%')
print()


# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
# Какова вероятность, что ни одна из них не перегорит в первый день?
# Какова вероятность, что перегорят ровно две?

p2 = 0.0004
n2 = 5000
m1 = 0
m2 = 2

lamb = p2*n2

odds_event_1 = (lamb**m1/m.factorial(m1))* 2.72**-lamb

odds_event_2 = (lamb**m2/m.factorial(m2))* 2.72**-lamb

print(f'Вероятность, что ни одна лампочка не перегорит в первый день = {odds_event_1*100 :.2f}%')
print(f'Вероятность, что перегорят ровно две лампочки = {odds_event_2*100 :.2f}%')
print()


# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

n3 = 144
k3 = 70

random_discrete_3 = (m.factorial(n3)/(m.factorial(k3)*m.factorial(n3-k3)))* 0.5**k3 * 0.5**(n3-k3)

print(f'Вероятность что орел выпадет 70 раз = {random_discrete_3*100 :.2f}%')
print()



# В первом ящике находится 10 мячей, из которых 7 - белые.
# Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча.
# Какова вероятность того, что все мячи белые?
# Какова вероятность того,что ровно два мяча белые?
# Какова вероятность того, что хотя бы один мяч белый?


A1 = 10
B1 = 7
A2 = 11
B2 = 9
k1 = 2
k2 = 2

#  (ББ*ББ)
P1 = (B1/A1)*((B1-1)/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))
result_1 = P1

# (ББ*ЧЧ)
q1 = (B1/A1)*((B1-1)/(A1-1)) * ((A2-B2)/A2)*(((A2-B2)-1)/(A2-1))
# (БЧ*БЧ)
q2 = (B1/A1)*((A1-B1)/(A1-1)) * (B2/A2)*((A2-B2)/(A2-1))
# (ЧБ*ЧБ)
q3 = ((A1-B1)/A1)*(B1/(A1-1)) * ((A2-B2)/A2)*(B2/(A2-1))
# (ЧБ*БЧ)
q4 = ((A1-B1)/A1)*(B1/(A1-1)) * (B2/A2)*((A2-B2)/(A2-1))
# (БЧ*ЧБ)
q5 = (B1/A1)*((A1-B1)/(A1-1)) * ((A2-B2)/A2)*(B2/(A2-1))
# (ЧЧ*ББ)
q6 = ((A1-B1)/A1) * (((A1-B1)-1)/(A1-1)) * (B2/A2)*((B2-1)/(A2-1))
result_2 = q1+q2+q3+q4+q5+q6


# (БЧ*ЧЧ)
w1 = (B1/A1)*((A1-B1)/(A1-1)) * ((A2-B2)/A2)*(((A2-B2)-1)/(A2-1))
# (ЧБ*ЧЧ)
w2 = ((A1-B1)/A1)*(B1/(A1-1)) * ((A2-B2)/A2)*(((A2-B2)-1)/(A2-1))
# (ЧЧ*БЧ)
w3 = ((A1-B1)/A1) * (((A1-B1)-1)/(A1-1)) * (B2/A2)*((A2-B2)/(A2-1))
# (ЧЧ*ЧБ)
w4 = ((A1-B1)/A1) * (((A1-B1)-1)/(A1-1)) * ((A2-B2)/A2)*(B2/(A2-1))
result_3 = w1+w2+w3+w4


print(f'Вероятность что мячи белые = {result_1*100 :.2f}%')

print(f'Вероятность что 2 мяча белые = {result_2*100 :.2f}%')

print(f'Вероятность что 1 мяч белый = {result_3*100 :.2f}%')


