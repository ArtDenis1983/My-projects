#Задачи ко 2 главе
#Задачи по программированию
#Персональные данные
print("Denis Artyushkov")
print("Address:\n     Vasilkovaya 24 B\n     Kazan\n     Tatarstan\n     420129")
print("Phone number: +79172810725")
print("Faculty: Ingeneering")

#Прогноз продаж
planning_sales = float(input("Введите плановую сумму общего объема продаж: "))
planning_profit = (planning_sales * 23) / 100
print("Прогнозируемая прибыль составит: ", planning_profit)

#Рассчет площади земльного участка
sqmetr_sum = float(input("Введите общее количество кв.м. участка земли: "))
akr_sum = sqmetr_sum / 4047
print ("Общее количество акров земли на данном участке: ", (format(akr_sum, '.2f')))

#Задача 4 Общий объем продаж
milk = float(input("Введите цену молока: "))
butter = float(input("Введите цену масла: "))
broad = float(input("Введите цену хлеба: "))
meat = float(input("Введите цену мяса: "))
cheese = float(input("Введите цену сыра: "))
purchase_summary = milk + butter + broad + meat + cheese
total = purchase_summary + (purchase_summary * 0.07)
print("Сумма всех покупок включая налог составляет: ", (format(total, '.2f')))

#Задание 5. Пройденное расстояние
# distance = speed * time
speed = 70
time1 = 6
time2 = 10
time3 = 15
print("Расстояние, которое пройдет автомобиль за 6 часов составляет: ", speed * time1, "км\ч")
print("Расстояние, которое пройдет автомобиль за 10 часов составляет: ", speed * time2, "км\ч")
print("Расстояние, которое пройдет автомобиль за 15 часов составляет: ", speed * time3, "км\ч")

# Задание 7.  Расход бензина в расчете на километры пройденного пути.
fuel_consumption = float(input("Введите количество литров, потраченных за время пути: ")) 
distance = float(input("Введите пройденное расстояние в километрах: "))
print("Расход бензина составил:", (format(distance / fuel_consumption, '.2f')), "литров на 100 км")

#Задание 8. Чаевые, налог и общая сумма
meal_cost = float(input("Please enter the cost of the meal: "))
tax = meal_cost * 0.07
tips = meal_cost * 0.18
print("Total price with tips and taxes is: $", (format (meal_cost + tax + tips, ".2f")), sep="")

# Задание 9. 
# Преобразователь температуры по шкале Цельсия в температуру по шкале Фаренгейта
temp_c = float (input ("Enter temperature in Celsius: "))
temp_f = (9 / 5) * temp_c + 32
print ("Temperature in Fahrenheit: ", (format (temp_f, ".1f")))

# Задание 10.
# Регулятор ингредиентов.
sugar_per_bun = 1.5 / 48
butter_per_bun = 1 / 48
flour_per_bun = 2.75 / 48
buns_numbers = float(input("Please enter the number of buns: "))
print ("For", buns_numbers, "buns you will need:")
print ( format (sugar_per_bun * buns_numbers, ".1f"), "Glass of sugar")
print ( format (butter_per_bun * buns_numbers, ".1f"), "Glass of butter")
print ( format (flour_per_bun * buns_numbers, ".1f"), "Glass of flour")

# Задание 11.
# Процент учащихся обоего пола.
male = int ( input("Please enter the number of male students: "))
female = int ( input("Please enter the number of female students: "))
students_sum = male + female
male_percent = male / students_sum
female_percent = female / students_sum
print("Male students percent is: ", (format(male_percent, ".0%")))
print("Female students percent is: ", (format(female_percent, ".0%")))

# Задание 12.
# Программа расчета купли-продажи акций.
shares_buy = 2000 * 40 						# 2000 shares, $40 for 1 share
buy_com = shares_buy * 0.03 				# 3% comission
shares_sell = 2000 * 42.75 					# 2000 shares, 42.75 for 1 share
sell_com = shares_sell * 0.03 				# 3% comission
balance = shares_sell - (buy_com + sell_com)	
total_profit = balance - shares_buy
print("Total cost of buy shares: $", format (shares_buy, ",.2f"), sep="")
print("Total cost of buy comission: $", format (buy_com, ",.2f"), sep="")
print("Total cost of sell shares: $", format (shares_sell, ",.2f"), sep="")
print("Total cost of sell comission: $", format (sell_com, ",.2f"), sep="")
print("Actual balance: $", format (balance, ",.2f"), sep="")
print("Total profit of deal: $", format (total_profit, ",.2f"), sep="")

# Задание 13
# Выращивание винограда
# 	Формула рассчета: V = (R-2*E) / S
#	V - количество виноградных лоз, которые поместятся на гряде; 
#	R - длина гряды в метрах; 
#	Е - размер пространства в метрах, занимаемых концевыми опорами; 
#	S - размер пространства между виноградными лозами в метрах.
R = float (input ("Please enter vine line lenght in meters: "))
E = float (input ("Please enter end support space in meters: "))
S = float (input ("Please enter space between vine in meters: "))
V = (R-2*E) / S
print("Total number of vine: ", V)

# Задание 14.
# Сложный процент
# Формула рассчета: A = P * (1 + r / n) ** (n * t)
# A - сумма денег на счете после конкретного количества лет
# Р - основная сумма, которая была внесена на счет в начале
# r - годовая процентная ставка
# n - частота начисления процентного дохода в год
# t - конкретное количество лет
P = float(input(" Введите основную сумму, внесенную на сберегательный счет в самом начале: "))
r_inp = float(input(" Введите годовую процентную ставку, начисляемую на остаток счета: "))
n = float(input(" Введите частоту начисления процентного дохода в год (например, \
если проценты начисляются ежемесячно, то ввести 12;  если процентный доход начисляется ежеквартально, то \
ввести 4)"))
t = float(input(" Введите количество лет, в течение которых сберегательный счет будет зарабатывать процент\
ный доход."))
r = r_inp / 100   # Пользователь вводит проценты как "5" или "10", что должно быть приведено к формату 0.05 или 0.1
A = P * (1 + r / n) ** (n * t)
print("Сумма по истечении периода вклада составит: ", format(A, ",.2f"), "руб.")

#Задание 15
#Черепашья графика
#Ромбы
import turtle
t = turtle
t.hideturtle()
t.fillcolor("grey")
t.begin_fill()
t.goto (50,-50)
t.goto (100, 0)
t.goto (50, 50)
t.goto (-50, -50)
t.goto (-100, 0)
t.goto (-50, 50)
t.goto (0, 0)
t.end_fill()
t.done()

#Треугольники
import turtle
t = turtle
t.hideturtle()
t.fillcolor("grey")
t.begin_fill()
t.goto (100, 0)
t.goto (50, 50)
t.goto (0, 0)
t.end_fill()
t.goto (50, 100)
t.goto (100, 0)
t.done()

#Параллелепипед
import turtle
t = turtle
t.hideturtle()
t.fillcolor("grey")
t.begin_fill()
t.goto (100, 0)
t.goto (50, 50)
t.goto (0, 0)
t.end_fill()
t.goto (50, 100)
t.goto (100, 0)
t.done()

#Кольца
import turtle
t = turtle
t.hideturtle()
t.circle(20)
t.penup ()
t.goto (50, 0)
t.pendown ()
t.circle (20)
t.penup ()
t.goto (100, 0)
t.pendown ()
t.circle (20)
t.penup ()
t.goto (25, -20)
t.pendown ()
t.circle (20)
t.penup ()
t.goto (75, -20)
t.pendown ()
t.circle (20)
t.done()

#Стороны света
import turtle
t = turtle
t.hideturtle()
t.goto (0, -25)
t.circle (25)
t.goto (0, -100)
t.goto (0, 100)
t.goto (0, 0)
t.goto (100, 0)
t.goto (-100, 0)
t.penup ()
t.goto (-6, -120)
t.write ("Юг")
t.goto (-140, -7)
t.write ("Запад")
t.goto (110, -7)
t.write ("Восток")
t.goto (-15, 103)
t.write ("Север")
t.done()

#Квадрат, пунктир, точки
import turtle
t = turtle
t.hideturtle()
t.pensize (2)
t.dot ()
t.goto (100, -100)
t.dot ()
t.goto (100, 100)
t.dot ()
t.goto (-100, -100)
t.dot ()
t.goto (-100, 100)
t.dot ()
t.goto (0, 0)
t.goto (-100, 100)
t.goto (-80, 100)
t.penup ()
t.goto (-60, 100)
t.pendown ()
t.goto (-10, 100)
t.penup ()
t.goto (10, 100)
t.pendown ()
t.goto (60, 100)
t.penup ()
t.goto (80, 100)
t.pendown ()
t.goto (100, 100)
t.penup ()
t.goto (-100, -100)
t.pendown ()
t.goto (-80, -100)
t.penup ()
t.goto (-60, -100)
t.pendown ()
t.goto (-10, -100)
t.penup ()
t.goto (10, -100)
t.pendown ()
t.goto (60, -100)
t.penup ()
t.goto (80, -100)
t.pendown ()
t.goto (100, -100)
t.done()

