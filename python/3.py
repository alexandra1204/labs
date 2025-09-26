# # Задание_1
# string=input("Строка: ")
# string_2=""
# k=1
# for i in range(1,len(string)):
#     if(i>0 and string[i]==string[i-1]):
#         k+=1
#     else:
#         if(k>1):
#             string_2+=string[i-1]+str(k)
#             k=1
#         else:
#             string_2+=string[i-1]
#             k=1
# if (k>1):
#     string_2+=string[-1]+str(k)
# else:
#     string_2+=string[-1]
# print(string_2)




# # Задание_2
# str_1=input("Строка: ")
# str_2=""
# for i in range(len(str_1)-1):
#     if (str_1[i].isalpha() and str_1[i+1].isdigit()):
#         num=int(str_1[i+1])
#         str_2+=str_1[i]*num
#     elif (str_1[i].isalpha() and str_1[i + 1].isalpha()):
#         str_2 += str_1[i]
# if(str_1[-1].isalpha()):
#     str_2+=str_1[-1]
# print(str_2)




# # Задание_3
# def numbers(n):
#     units = ['ноль', 'один', 'два', 'три', 'четыре', 'пять',
#              'шесть', 'семь', 'восемь', 'девять', 'десять',
#              'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
#              'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
#              'девятнадцать']
#     tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
#             'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     hundreds = ['','сто', 'двести', 'триста', 'четыреста', 'пятьсот',
#                 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
#
#     if n == 0:
#         return units[0]
#
#     words = ''
#     if n // 100 > 0:
#         words += hundreds[n // 100] + ' '
#         n %= 100
#     if n // 10 > 1:
#         words += tens[n // 10] + ' '
#         n %= 10
#         if n > 0:
#             words += units[n]
#     elif n > 0:
#         words += units[n]
#
#     return words
#
# number = int(input("Введите число от 1 до 1000: "))
# if 1 <= number <= 1000:
#     words = numbers(number)
#     print(f"{number} - {words}")
# else:
#     print("Число вне диапазона от 1 до 1000")




# # Задание_4
# lines=[
#      ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc'],
#      ['aaa', 'bbb', 'ccc'],
#      ['abc', 'abc', 'abc']
#  ]
# for line in lines:
#     dict1 = {}
#     for item in line:
#         if item in dict1:
#             dict1[item] += 1
#         else:
#             dict1[item] = 1
#     print("Входные данные: ", line)
#     print("Выходные данные: ",end=" ")
#     for key in dict1:
#         print(dict1[key],end=" ")
#     print('\n')





# # Задание_5
# mat = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 80]
# ]
#
# def dependency(matrix):
#     a = [row[0] for row in matrix]
#     b = [row[1] for row in matrix]
#     c = [row[2] for row in matrix]
#
#     det = a[0] * (b[1] * c[2] - b[2] * c[1]) - b[0] * (a[1] * c[2] - a[2] * c[1]) + c[0] * (a[1] * b[2] - a[2] * b[1])
#
#     if det == 0:
#         print("Столбцы матрицы линейно зависимы")
#     else:
#         print("Столбцы матрицы линейно независимы")
#
# print("Матрица:")
# for row in mat:
#     print(row)
#
# dependency(mat)




# Задание_6

input_string = input("Введите строку: ")
words = input_string.split()
a = ""
for word in words:
    a += word[0].upper()
print("Аббревиатура: ",a)
