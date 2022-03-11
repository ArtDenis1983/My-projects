#Глава 3
#Задание 1. День недели

day_of_week = int(input("Please enter a valid day of week (1-7)"))
if day_of_week == 1:
	print ("monday")
elif day_of_week == 2:
	print ("tuesday")
elif day_of_week == 3:
	print ("wednesday")
elif day_of_week == 4:
	print ("thursday")
elif day_of_week == 5:
	print ("friday")
elif day_of_week == 6:
	print ("saturday")
elif day_of_week == 7:
	print ("sunday")
else:
	if day_of_week <=0 or day_of_week >=8:
		print ("Out of range")

"""======================================================================================================================"""
#Задание 2. Площади прямоугольника
#
lenght1 = float(input("Enter lenght of rectangle1:"))
width1 = float(input("Enter width of rectangle1:"))
lenght2 = float(input("Enter lenght of rectangle2"))
width2 = float(input("Enter width of rectangle2:"))

rectangle1_area = lenght1 * width1
rectangle2_area = lenght2 * width2
r1 = rectangle1_area
r2 = rectangle2_area
if r1 == r2 :
	print("The area of both rectangles is the same")
elif r1 > r2 :
	print("The area of a rectangle1 is greater than rectangle2")
elif r1 < r2 :
	print("The area of a rectangle2 is greater than rectangle1")

"""======================================================================================================================"""
#Задание 3. Классификатор возраста
#
age = int(input("Введите ваш возраст: "))
if age <= 1 or age == 0:
	print("Младенец")
elif age > 1 and age < 13:
	print("Ребенок")
elif age >= 13 and age <= 20:
	print("Подросток")
elif age > 20:
	print("Взрослый")
else:
	print("Некорректное значение")

"""======================================================================================================================"""
	#Задание 4. Римские цифры

num = int(input("Введите цифру от 1 до 10, чтобы увидеть римский вариант написания:  "))

if num == 1:
	print("Римский вариант написания:  I")
elif num == 2:
	print("Римский вариант написания:  II")
elif num == 3:
	print("Римский вариант написания:  III")
elif num == 4:
	print("Римский вариант написания:  IV")
elif num == 5:
	print("Римский вариант написания:  V")
elif num == 6:
	print("Римский вариант написания:  VI")	
elif num == 7:
	print("Римский вариант написания:  VII")
elif num == 8:
	print("Римский вариант написания:  VIII")
elif num == 9:
	print("Римский вариант написания:  IX")
elif num == 10:
	print("Римский вариант написания:  X")
else:
	print("Значение вне диапазона 1-10")

"""======================================================================================================================"""
#Задание 5. Масса и вес

weigth_kg = float(input("Введите массу тела в килограммах: "))
weight_N = weigth_kg * 9.8
w = weight_N
if w < 100:
	print("Тело слишком легкое")
elif w > 500:
	print("Тело слишком тяжелое")
elif w >= 100 and w <=500:
	print("Вес в ньютонах: ", format(w,'.2f'),"Н", sep="")

#Задание 6. Волшебные даты

day = int(input("Введите число рождения : "))
month = int(input("Введите месяц рождения в числовой форме: "))
year = int(input("Введите две последние цифры года рождения: "))
a = day * month
if a == year:
	print("!!! Введенная дата является волшебной !!!")
elif a != year:
	print("Введенная дата не является волшебной")

"""======================================================================================================================"""
"""#Задание 7. Цветовой микшер+

# При смешивании двух основных цветов получается вторичный цвет: 
# если смешать красный и синий, то получится фиолетовый; 
# если смешать красный и желтый, то получится оранжевый; 
# если смешать синий и желтый, то получится зеленый. 

a = input("Введите название смешиваемых цветов: ")
if a == "красный и синий":
	print("фиолетовый")
elif a == "красный и желтый":
	print("оранжевый")
elif a == "синий и желтый":
	print("зеленый")
else:
	print("неправильный формат ввода")
"""
red = 1
blue = 2
yellow = 3

a = input("Введите название первого цвета (красный, синий или желтый): ")
if a == "красный":
	color1 = 1
elif a == "синий":
	color1 = 2
elif a == "желтый":
	color1 = 3
else:
	print("Введен не корректный цвет, либо неправильный формат ввода. Проверьте написание\nцвета (красный, синий или желтый)")

b = input("Введите название второго цвета (красный, синий или желтый): ")
if b == "красный":
	color2 = 1
elif b =="синий":
	color2 = 2
elif b == "желтый":
	color2 = 3
else: 
	print("Введен не корректный цвет, либо неправильный формат ввода. Проверьте написание\nцвета (красный, синий или желтый)")

if color1 == 1 and color2 == 2:
	print("Получится цвет: Фиолетовый")
elif color1 == 1 and color2 == 3:
	print("Получится цвет: Оранжевый")
elif color1 == 2 and color2 == 3:
	print("Получится цвет: Зеленый")
elif color1 == color2:
	print("При смешении одинаковых оттенков цвет не изменится")
else:
	print("Введен не корректный цвет, либо неправильный формат ввода. Проверьте написание\nцвета (красный, синий или желтый)")

"""======================================================================================================================"""
#Задание 8. Калькулятор сосисок
# 
SAUSAGE_PACK = 10
BUN_PACK = 8
sausage_packages = True
aux_var1 = True #aux_var1 - вспомогательная переменная для сосисок
aux_var2 = True #aux_var2 - вспомогательная переменная для булок

persons = int(input("Введите количество участников фестиваля: "))
hotdog = int(input("Введите количество хотдогов для каждого участника: "))

total_hotdogs = persons * hotdog
t = total_hotdogs

if t <= SAUSAGE_PACK:
	sausage_packages = 1
	sausage_leftover = SAUSAGE_PACK - t
elif t > SAUSAGE_PACK:
	aux_var1 = t % SAUSAGE_PACK
	if aux_var1 == 0:
		sausage_packages = t / SAUSAGE_PACK
	elif aux_var1 >=1:
		sausage_packages = t / SAUSAGE_PACK +1

sausage_leftover = int(sausage_packages) * SAUSAGE_PACK - t

if t <= BUN_PACK:
	bun_packages = 1
	bun_leftover = BUN_PACK - t
elif t > BUN_PACK:
	aux_var2 = t % BUN_PACK
	if aux_var2 == 0:
		bun_packages = t // BUN_PACK
	elif aux_var2 >=1:
		bun_packages = t // BUN_PACK + 1

bun_leftover = int(bun_packages) * BUN_PACK - t

print("Необходимое количество упаковок сосисок: ", int(sausage_packages))
print("Необходимое количество упаковок булочек: ", int(bun_packages))
print("Остаток сосисок в открытой упаковке: ", int(sausage_leftover))
print("Остаток булочек в открытой упаковке: ", int(bun_leftover))


"""======================================================================================================================"""
#Задание 9. Цвета колеса рулетки
"""
color = 0 зеленый
color = 1 красный
color = 2 черный
color = 999 недопустимое число
"""
color = True
number = int(input("Введите число от 0 до 36 включительно: "))

if number < 0 or number > 36:
	color = 999
elif number == 0:
	color = 0
elif number >= 1 and number <= 10:
	even_odd = number % 2
	if even_odd == 0:
		color = 2
	elif even_odd == 1:
		color = 1
elif number >= 11 and number <= 18:
	even_odd = number % 2
	if even_odd == 0:
		color = 1
	elif even_odd == 1:
		color = 2
elif number >= 19 and number <= 28:
	even_odd = number % 2
	if even_odd == 0:
		color = 2
	if even_odd == 1:
		color = 1
elif number >= 29 and number <= 36:
	even_odd = number % 2
	if even_odd == 0:
		color = 1
	if even_odd == 1:
		color = 2

if color == 0:
	print ("Зеленая ячейка")
elif color == 1:
	print("Красная ячейка")
elif color == 2:
	print("Черная ячейка")
else:
	color = 999
	print("Недопустимое число")

"""======================================================================================================================"""
#Задание 10. Игра с подсчитыванием монет

coin_1 = int(input("Выберете количество монет, достоинством 1 цент: "))
coin_5 = int(input("Выберете количество монет, достоинством 5 центов: "))
coin_10 = int(input("Выберете количество монет, достоинством 10 центов: "))
coin_25 = int(input("Выберете количество монет, достоинством 25 центов: "))
print ("Вы выбрали:")
print ("1 цент: ", coin_1, "шт")
print ("5 цент: ", coin_5, "шт")
print ("10 цент: ", coin_10, "шт")
print ("25 цент: ", coin_25, "шт")

dollar = 100
cent_1 = 1
cent_5 = 5
cent_10 = 10
cent_25 = 25

total_cent_1 = coin_1 * cent_1
total_cent_5 = coin_5 * cent_5
total_cent_10 = coin_10 * cent_10
total_cent_25 = coin_25 * cent_25
total_sum = total_cent_1 + total_cent_5 + total_cent_10 + total_cent_25

if total_sum == dollar:
	print("CONGRATULATIONS!!! YOU WIN!!!")
elif total_sum > dollar:
	print("Общая стоимость всех монет больше 1$") 
elif total_sum < dollar:
	print("Общая стоимость всех монет меньше 1$")


"""======================================================================================================================"""
#Задание 11. Очки книжного клуба

books = int(input("Введите количество книг: "))

if books <= 1:
	print("Количество заработанных очков: 0")
elif books >= 2 and books < 4:
	print("Количество заработанных очков: 5")
elif books >=4 and books < 6:
	print("Количество заработанных очков: 15")
elif books >=6 and books < 8:
	print("Количество заработанных очков: 30")
elif books >=8:
	print("Количество заработанных очков: 60")

"""======================================================================================================================"""
#Задание 12. Реализация программного обеспечения

soft_pack = int(input("Введите количество пакетов ПО: "))

pack_cost = 99
if soft_pack <= 9:
	disc = 0
elif soft_pack >=10 and soft_pack <=19:
	disc = 0.1
elif soft_pack >=20 and soft_pack <= 49:
	disc = 0.2
elif soft_pack >=50 and soft_pack <= 99:
	disc = 0.3
elif soft_pack > 99:
	disc = 0.4

total_cost = soft_pack * pack_cost
cost_with_disc = total_cost - (total_cost * disc)
disc_sum = total_cost - cost_with_disc

if disc > 0:
	print("Ваша скидка ", int(disc * 100), "%", " Сумма скидки $", format(disc_sum, ",.2f"), sep="")

print ("Сумма покупки с учетом скидки: $", format (cost_with_disc, ",.2f"), sep="")
"""======================================================================================================================"""
#Задание 13. Стоимость достваки

weight = float(input("Введите массу пакета в граммах, чтобы рассчитать стоимость доставки: "))

if weight <= 200:
	rate = 150
elif weight > 200 and weight <= 600:
	rate = 300
elif weight > 600 and weight <= 1000:
	rate = 400
elif weight > 1000:
	rate = 475

cost = (weight / 100) * rate

print("Стоимость доставки составляет: ", format(cost, ",.0f"), " рублей", sep="")
"""======================================================================================================================"""
#Задание 14. Опредление массы тела

weight = float(input("Введите ваш вес в килограммах: "))
height = float(input("Введите ваш рост в сантиметрах: "))

height_metr = height / 100 

bmi = weight / height_metr

print("Ваш индекс массы тела: ", format(bmi, ".1f"))
if bmi < 18.5:
	print("Вес ниже нормы")
elif bmi >=18.5 and bmi <= 25:
	print("Оптимальный вес")
elif bmi > 25:
	print("Избыточный вес")
"""======================================================================================================================"""
#Задание 15. Калькулятор времени

total_seconds  =  float(input('Bвeдитe количество секунд:  ')) 

hours  =  (total_seconds  // 3600) % 24 		#  Получить количество часов. 
minutes  =  (total_seconds  //  60) % 60  		#  Получить количество оставшихся минут. 
seconds  =  total_seconds  % 60  				#  Получить количество оставшихся секунд. 
days = ((total_seconds // 3600) // 24) % 365
years = (((total_seconds // 3600) // 24) // 365)

if total_seconds <= 60:
	print ("В введенном количестве секунд содержится:\nминут:", int(minutes), "\nсекунд:", int(seconds))
elif total_seconds > 60 and total_seconds <= 3600:
	print ("В введенном количестве секунд содержится: \nчасов:", int(hours),  "\nминут:", int(minutes), "\nсекунд:", int(seconds))
elif total_seconds >3600 and total_seconds <= 86400:
	print ("В введенном количестве секунд содержится: \n\
дней:", int(days), "\nчасов:", int(hours),  "\nминут:", int(minutes), "\nсекунд:", int(seconds))
elif total_seconds > 86400:
	print ("В введенном количестве секунд содержится: \n\
годы:", int(years),"\nдней:", int(days), "\nчасов:", int(hours),  "\nминут:", int(minutes), "\nсекунд:", int(seconds))

"""======================================================================================================================"""
#Задание 16. Дни в феврале

year = int(input("Введите год: "))

if year % 100 == 0 and year % 400 == 0:
	print ("В", year, "году 29 дней в феврале, високосный год")
elif year % 100 !=0 and year % 4 == 0:
	print ("В", year, "году 29 дней в феврале високосный год")
else:
	print("В", year, "году 28 дней в феврале год невисокосный")

"""======================================================================================================================"""
#Задание 17. Диагностическое дерево проверки качества Wi-Fi.

print("Перезагрузите компьютер и попробуйте подключиться.")
a = input("Проблема решена? да/нет: ")
if a == "да":
	print("Спасибо за обращение в службу поддержки")
else:
	print("Перезагрузите маршрутизатор и попробуйте подключиться")
	a = input("Проблема решена? да/нет: ")
	if a == "да":
		print("Спасибо за обращение в службу поддержки")
	else:
		print("Убедитесь, что кабели между маршрутизатором и модемом/компьютером прочно подсоединены")
		a = input("Проблема решена? да/нет: ")
		if a == "да":
			print("Спасибо за обращение в службу поддержки")
		else:
			print("Переместите маршрутизатор в новое место")
			a = input("Проблема решена? да/нет: ")
			if a == "да":
				print("Спасибо за обращение в службу поддержки")
			else:
				print("Возьмите новый марщрутизатор")

"""======================================================================================================================"""
#Задание 18. Селектор ресторанов

vegetarian = input("Будет ли на ужине вегетарианец? (да/нет): ")
vegan = input("Будет ли на ужине веган? (да/нет): ")
gluten = input("Будет ли на ужине приверженец безглютеновой диеты? (да/нет): ")

if vegetarian == "да":
	vegetarian = 1
else:
	vegetarian = 0
if vegan == "да":
	vegan = 1
else:
	vegan = 0
if gluten == "да":
	gluten = 1
else:
	gluten = 0

print("Ваши варианты ресторанов: ")

if vegetarian == 0 and vegan== 0 and gluten == 0:
	print("Изысканные бургеры от Джо")
if vegetarian >= 0 and vegan == 0 and gluten >= 0:
	print("Центральная пиццерия")
if vegan >= 0 and vegan >= 0 and gluten >= 0:
	print ("Кафе за углом")
	print ("Кухня Шеф-повара")
if vegetarian >= 0 and vegan == 0 and gluten == 0:
	print ("Блюда от итальянской мамы")

"""======================================================================================================================"""
#Задание 19. Черепашья графика: Модификация игры "Порази цель"

import  turtle 
#  Именованные константы 
SCREEN_WIDTH  =  600  #  Ширина экрана. 
SCREEN_HEIGHT  =  600  #  Высота экрана. 
TARGET_LLEFT_Х =  100  #  Левая нижняя координата х цели. 
TARGET_LLEFT_Y =  250  #  Левая нижняя координата у цели. 
TARGET_WIDTH =  25  #  Ширина цели. 
FORCE_FACTOR  =  30  #  Фактор произвольной силы. 
PROJECTILE_SPEED = 1  #  Скорость анимации снаряда. 
NORTH  =  90  #  Угол северного направления. 
SOUTH  =  270  #  Угол южного направления. 
EAST = 0  #  Угол восточного направления. 
WEST  =  180  #  Угол западного направления. 

#Настроить окно. 
turtle.setup(SCREEN_WIDTH,  SCREEN_HEIGHT) 
#  Нарисовать цель. 
turtle.hideturtle() 
turtle.speed() 
turtle.penup() 
turtle.goto(TARGET_LLEFT_Х, TARGET_LLEFT_Y) 
turtle.pendown() 
turtle.setheading(EAST) 
turtle.forward(TARGET_WIDTH) 
turtle.setheading(NORTH) 
turtle.forward(TARGET_WIDTH) 
turtle.setheading(WEST) 
turtle.forward(TARGET_WIDTH) 
turtle.setheading(SOUTH) 
turtle.forward(TARGET_WIDTH) 
turtle.penup() 
#  Центрировать черепаху. 
turtle.goto(0,  0) 
turtle.setheading(EAST) 
turtle.showturtle() 
turtle.speed(PROJECTILE_SPEED) 
#  Получить угол и силу от  пользователя. 
angle = float(input("Bвeдитe угол снаряда:  ")) 
force  =  float(input("Bвeдитe пусковую силу  (1-10):  ")) 
#  Рассчитать расстояние. 
distance  =  force  *  FORCE_FACTOR 
#  Задать направление. 
turtle.setheading(angle) 
#  Запустить снаряд. 
turtle.pendown() 
turtle.forward(distance) 
#  Снаряд поразил цель? 
if  (turtle.xcor()  >=  TARGET_LLEFT_Х and 
	turtle.xcor()  <=  (TARGET_LLEFT_Х  +  TARGET_WIDTH)  and 
	turtle.ycor()  >=  TARGET_LLEFT_Y and 
	turtle.ycor()  <=  (TARGET_LLEFT_Y  +  TARGET_WIDTH)): 
		print ('Цель  поражена! ') 
else: 
	print ('Вы промахнулись.')
if (turtle.xcor()  >= TARGET_LLEFT_Х and turtle.ycor() >=  (TARGET_LLEFT_Y  +  TARGET_WIDTH)):
	print ('Попробуйте снизить скорость ')
elif (turtle.xcor()  >= (TARGET_LLEFT_Х  +  TARGET_WIDTH) and turtle.ycor() >= TARGET_LLEFT_Y):
	print ('Попробуйте снизить скорость ')
elif (turtle.xcor()  <= TARGET_LLEFT_Х and turtle.ycor() <=  (TARGET_LLEFT_Y  +  TARGET_WIDTH)):
	print ('Попробуйте увеличить скорость ')
elif (turtle.xcor()  <= (TARGET_LLEFT_Х  +  TARGET_WIDTH) and turtle.ycor() <= TARGET_LLEFT_Y):
	print ('Попробуйте увеличить скорость ')
else:
	print("Измените угол")

turtle.done()
