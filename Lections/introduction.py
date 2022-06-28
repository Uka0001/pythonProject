# 5 базовых типов данных - примитивы.

42   	 #int    : целые числа
42.0	 #float  : дробные
"Hello!" #string : строки
'Hello!' #string : у строк не важен вид кавычек
True  	 #bool   : булеановы значения, их только два - ДА и НЕТ, True/False
None 	 #none   : обозночает отсутствие знаения. ВАЖНО - не нулевое значение, а именно пустоту, отсуствие всякого значения.


# Значок решетки это однострочный комментарий.
# Комментарий - это не тип данных, а инструмент. 
# То, что написано в комментарии, видно людям, но как код не воспринимает.


"""
А вот этот коммент - многострочный. 
В нем начало и конец определяется тремя кавычками.
Не ошибитесь! Строка - одна кавычка, комментарий - три.
"""

'''
Кавычки могут быть, как и у строки, одинарными и двойными.
Принципиальной разницы нет.
'''


"""
print() - Именованная инструкция (их принято называть функциями) для того, 
		  чтобы напечатать что-то в командной строке
"""

# print("232e;ls;md") # Напечатать значение внутри скобок. 
# print(97)


# print("Hello", 97, 11, True, True, None, False, 0.0) #То, что надо напечатать, перечисляеться через запятую
# print("Hello world")

name = "Meganagibator8aRULIt"
level = 11
lattitude = 98.87
longittude = 113.45
chatv_ailable = False
print(name, level)



# Переменные. Присваиваем значение через =

# value = 127919191
# print(value)

# name = "Victor"
# print(name, value, value3)

""" 
Имена переменных должны содержать только латинские символы, без пробелов и тире.
Если имя состоит из нескольких частей, например, user bank account, то соединять
нужно не тирее, а _.
user_bank_account
"""

# правильное именование
value = 45
my_value = False
name = "Victor"
lattitude = 98.05
longitude = 100.05


# Сработает, но с большой буквы начинать не принято.
Value = 0


#Капсом обычно называют константы - переменные, значения которых используются во множестве мест большой программы.
VALUE = 0
 
"""
Вызовет ошибку:
Число не может быть переменной.
Кирилицу нельзя использовать
число не может быть первым символом.
тира нельзя использовать
переменная = "Значение"
"""
# 1 = "Value"
# my-value
# 1value = "value"

# Математика
2 + 6
# print(2+6)

# result = 2+6
# print(result)
result = 15
# print(result)

new_result = result/12
# print(new_result)

result = result*2
# print(resultЫ)

# Равенство это ==, = - присваивание значения переменной.
2 == 3
2 == 2

# print(2 == 3)
# print(2 == 2)

#Форматирование - когда строка используется как шаблон, в который подставляются разные значения.

#1 Форматирование через +

order = 4252424
adress = "Some str. 55"
# print("Курьер уже везет ваш заказ " + str(order)  + " по аддресу " + adress)

#2 Форматирование через .format()
message = "Курьер уже везет ваш заказ {order} по аддресу {adress}".format(order=order, adress=adress)
# print(message)

# f-форматирование
message = f"Курьер уже везет ваш заказ {order} по аддресу {adress}"
# print(message)

# Полезные базовые функции.

# Узнать тип данных
# print(type(35))
# print(type(""))
# print(type(None))

# Можно его напечатать сразу.
# print(type(35))

# Можно присвоить значение типа переменной.
value_type = type(35)
# print(value_type)

"""
Типы данных можно изменять, но только там, где это не противоречит логике.
Вот так можно:
"""
#print(int("56"))
# print(str(None))
# print(float(55))
# А так - нет. Непонятно, как строка может стать дробным числом.
#float('55')
# float("Hello")


# Можно даже изменять множество раз
# print(float(int("56")))
# print(str(float("96.0")))

# print(value)

#функция|метод