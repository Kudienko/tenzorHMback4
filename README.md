Задача «Скобки в коде»
Необходимо написать программу, которая проверит правильность
расположения скобок в тексте. Скобки в тексте могут быть трех видов,
квадратные «[]», круглые «()» и фигурные «{}». Каждой открывающей скобке
обязательно должна присутствовать соответствующая ей закрывающая и
наоборот.
Если расположение скобок в тексте верное, выведи «Success»
Если в тексте есть ошибки – выведите индекс символа первой
встреченной ошибки (нумерация символов с единицы).
Для решения лучше использовать структуру типа «стек», по
возможности больше использовать возможности классов.
На входе одна строка, количество символов ограничено 1000.
На выходе результат проверки.
Пример формата входных данных (скобки расставлены верно):
[{}([])]
Пример выходного файла с решением:
Success
Пример формата входных данных (нет закрывающей):
def function[T](value: T -> T:
Пример выходного файла с решением (у 16 символа скобки «(» нет
закрывающей):
16
Пример формата входных данных (нет открывающей):
[())]
Пример выходного файла с решением:
4
