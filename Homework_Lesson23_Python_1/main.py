#4. **Напишите программу, которая выводит фразу «Привет, мир!».**

def hello():
    print('Hello world!')

#5. **Напишите программу, которая вычисляет сумму 2 + 2 и выводит результат.**
#  - Программа должна использовать операцию сложения и выводить ответ на экран с помощью функции `print`.

def math_sum():
    print(f'2 + 2 = {2+2}')

#6. **Программа приветствия:**
#   - Напишите программу, которая запрашивает у пользователя его имя и выводит сообщение: «Привет, [имя]!».

def custom_hello():
    name = input('input your name:\n')
    print(f'Hello, {name}')

#7. **Числовой вывод:**
#   - Создайте программу, которая выводит на экран числа от 1 до 10.

def number_output():
    print('numbers from 1 to 10: \n')
    print(*(i for i in range(1,11)))
    
#8. **Определение возраста:**
#   - Напишите программу, которая запрашивает возраст пользователя и выводит сообщение: «Ваш возраст — [возраст] лет».
def age():
    age = input('input your age:\n')
    print(f'Your age is - {age} years')

#9. **Произведение чисел:** # type: ignore
#   - Напишите программу, которая запрашивает у пользователя два числа и выводит их произведение.
def produce_number():
    number1 = int(input('input number 1:\n'))
    number2 = int(input('input namber 2:\n'))
    print(f'{number1} * {number2} = {number1 * number2}')

#10. **Первая буква слова:**
#    - Создайте программу, которая запрашивает у пользователя слово и выводит его первую букву.
def first_letter():
    word = input('input word:\n')
    print(f'first letter: {word[0]}')

#11. **Квадрат числа:**
#    - Напишите программу, которая запрашивает у пользователя целое число и выводит его квадрат.
def custom_square():
    number = int(input('input int number:\n'))
    print(f'square {number}: {number ** 2}')

#12. **Таблица умножения:**
#    - Создайте программу, которая выводит таблицу умножения на число 5 (от 1 до 10).
def custom_multipli():
    print('numbers from 1 to 10 multiplied by 5: \n')
    print(*(el * 5 for el in range(1,11)))

#13. **Среднее арифметическое:**
#    - Напишите программу, которая запрашивает у пользователя два числа и выводит их среднее арифметическое.
def custom_arifmetic_mean():
    number1 = int(input('input number 1:\n'))
    number2 = int(input('input namber 2:\n'))
    print(f'arifmetic mean {number1} and {number2} is {(number1+number2)/2}')


print(f'\n Задание 4:')
hello()
print(f'\n Задание 5:')
math_sum()
print(f'\n Задание 6:')
custom_hello()
print(f'\n Задание 7:')
number_output()
print(f'\n Задание 8:')
age()
print(f'\n Задание 9:')
produce_number()
print(f'\n Задание 10:')
first_letter()
print(f'\n Задание 11:')
custom_square()
print(f'\n Задание 12:')
custom_multipli()
print(f'\n Задание 13:')
custom_arifmetic_mean()