# #№1
# def count(nums):
#     nums = set(nums)
#     return len(nums)
#
# list=[]
# n=int(input("Введите количество чисел в списке: "))
# print("Введите числа: ")
# for i in range(n):
#     c=int(input())
#     list.append(c)
#
# print("Входные данные:", *list)
# print("Выходные значения:", count(list))


# #№2
#
# set1=set()
# set2=set()
#
# n=int(input("Введите количество чисел множества 1: "))
# print("Введите числа: ")
# for i in range(n):
#     c=int(input())
#     set1.add(c)
#
# n=int(input("Введите количество чисел множества 2: "))
# print("Введите числа: ")
# for i in range(n):
#     c=int(input())
#     set2.add(c)
#
# print(set1!=set2 and set1.issubset(set2))

# #№3
#
# def check(city, cities_set):
#     if city in cities_set:
#         return "REPEAT"
#     else:
#         cities_set.add(city)
#         return "OK"
#
# n = int(input("Введите максимальное количество названных городов: "))
# cities_set = set()
#
# for i in range(n):
#     city = input("Введите название города: ")
#     result = check(city, cities_set)
#     print(result)


# #№4
#
# input_string = input("Введите строку текста: ")
# words = input_string.split()
# seen_words = {}
# result = []
#
# for word in words:
#     if word in seen_words:
#         result.append(str(seen_words[word]))
#     else:
#         result.append('0')
#     seen_words[word] = seen_words.get(word, 0) + 1
#
# print("Вывод программы:", ' '.join(result))



# #№5
# n = int(input("Введите количество записей о покупках: "))
# purchases = {}
#
# for i in range(n):
#     record = input("Введите запись о покупке (ID Покупателя, Товар, Количество): ").split()
#     customer_id = int(record[0])
#     product = record[1]
#     quantity = int(record[2])
#
#     if customer_id not in purchases:
#         purchases[customer_id] = set()
#
#     purchases[customer_id].add((product, quantity))
#
# for customer_id, shopping_set in purchases.items():
#     print(f"Покупатель {customer_id}:")
#     for product, quantity in shopping_set:
#         print(f"  {product}: {quantity}")



#№6

text = input("Введите текст: ")

word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(word)