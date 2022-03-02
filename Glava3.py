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


#Задание 7. Цветовой микшер+

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
