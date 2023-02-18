# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

import math as m

all_carts = 52
take_carts = 4
one_suit = 13

favorable_outcomes_1 = m.factorial(one_suit) / (m.factorial(take_carts)*m.factorial(one_suit - take_carts))
all_outcomes_1 = m.factorial(all_carts)/(m.factorial(take_carts)*m.factorial(all_carts-take_carts))
result_1 = favorable_outcomes_1 / all_outcomes_1
print(f'все карты крести = {result_1*100 :.2f}%')

# Расчет возможных случаев благоприятного исхода

p1 = (m.factorial(4)/(m.factorial(1)*m.factorial(4-1)))*(m.factorial(48)/(m.factorial(3)*m.factorial(48-3)))
p2 = (m.factorial(4)/(m.factorial(2)*m.factorial(4-2)))*(m.factorial(48)/(m.factorial(2)*m.factorial(48-2)))
p3 = (m.factorial(4)/(m.factorial(3)*m.factorial(4-3)))*(m.factorial(48)/(m.factorial(1)*m.factorial(48-1)))
p4 = m.factorial(4)/(m.factorial(4)*m.factorial(4-4))
favorable_outcomes_2 = p1+p2+p3+p4

# Расчет всех равновозможных исходов
all_outcomes_2 = m.factorial(52)/(24*m.factorial(48))

result_2 = favorable_outcomes_2/all_outcomes_2

print(f"Вероятность наличия хотя бы одного туза из 4 карт = {result_2*100 :.2f}%")
print()

#  На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того,
# что человек, не знающий код, откроет дверь с первой попытки?


all_numbers = 10
code = 3

favorable_outcomes_3 = 1
all_outcomes_3 = m.factorial(10)/(m.factorial(3)*m.factorial(10-3))

result_3 = favorable_outcomes_3/all_outcomes_3
print(f"Вероятность определения кода с первой попытки = {result_3*100 :.2f}%")
print()


# В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

all_details = 15
details_color = 9
take_details = 3

favorable_outcomes_4 = m.factorial(details_color)/(m.factorial(take_details) * m.factorial(details_color-take_details))
all_outcomes_4 = m.factorial(all_details)/(m.factorial(take_details) * m.factorial(all_details - take_details))

result_4 = favorable_outcomes_4/all_outcomes_4
print(f"Вероятность того, что все детали окрашены = {result_4*100 :.2f}%")
print()


# В лотерее 100 билетов. Из них 2 выигрышных. Какова
# вероятность того, что 2 приобретенных билета окажутся выигрышными?

all_tickets = 100
prize = 2

favorable_outcomes_5 = 1
all_outcomes_5 = m.factorial(100)/(m.factorial(2)*m.factorial(100-2))

result_5 = favorable_outcomes_5/all_outcomes_5
print(f"Вероятность приобретения 2 выигрышных билетов  = {result_5*100 :.2f}%")



