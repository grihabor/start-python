"""
Краткое содержание

+, -, *, /, //, %, ** - арифметические операции
type - узнать тип объекта
raise - выкинуть ошибку (англ. exception - исключение)
"""

### +, -, *, /, //, %, **

# Питон поддерживает обычные арифметические операции над числами
# Примеры:

x = 3
y = x ** 2 - 5 * x + 6
print(y) # напечатает 0

# В этом примере мы используем операции сложения (+), вычитания (-), умножения (*) и возведения в степень (**)
# Результат 0 получается, так как 3 - корень данного квадратного многочлена

# При выполнении арифметических операций нужно понимать, какого типа получится результат
# Основные типы чисел в питоне - 'int' (англ. integer - целочисленный) 
# и 'float' (англ. floating point number - число с плавающей точкой)

# Например, при сложении объектов типа 'int' получается объект типа 'int'
# Это логично, потому что при сложении целых чисел может получиться только целое число
# Пример:

a = 1 + 3
print(type(a)) # напечатает <class 'int'>

# С помощью функции type() можно узнать тип объекта (что такое class, узнаем чуть позже ;))
# 1 и 3 - объекты типа 'int' - в сумме дают 4, что тоже является объектом типа 'int'
# В простых случаях понятно, но что делать, например, с делением?
# Для решения этой проблемы в 3-ей версии питона (Python 3) ввели 2 разных операции деления:
# целочисленное деление (//) и нецелое деление (/). Примеры:

a = 7
b = 4
print(a / b, type(a / b)) # напечатает 1 <class 'int'>
print(a // b, type(a // b)) # напечатает 1.75 <class 'float'>
      
# В случае целочисленного деления мы просто отбрасываем нецелую часть (округления не происходит!)

