#№1
f=open('input.txt','r')
numbers = f.readline().split()
numbers = [int(num) for num in numbers]
prod = 1
for num in numbers:
    prod *= num

f2 = open('output.txt', 'w')
f2.write(str(prod))
print('Произведение записано в файл output.txt')
f.close()
f2.close()

# #№2
# f=open('input2.txt','r')
# numbers = f.readlines()
# numbers = [int(num) for num in numbers]
# numbers.sort()
# f2 = open('output2.txt', 'w')
# for num in numbers:
#     f2.write(str(num)+"\n")
# print('Отсортированные числа записаны в файл output2.txt')
# f.close()
# f2.close()

# #№3
# f=open('input3.txt', 'r',encoding='utf-8')
# lines = f.readlines()
#
# youngest = None
# oldest = None
#
# for line in lines:
#     parts = line.split()
#     surname = parts[0]
#     name = parts[1]
#     age = int(parts[2])
#
#     if youngest is None or age < youngest[2]:
#         youngest = (surname, name, age)
#
#     if oldest is None or age > oldest[2]:
#         oldest = (surname, name, age)
#
# with open('youngest.txt', 'w') as file:
#     file.write(f'Самый младший ребенок: {youngest[0]} {youngest[1]}, возраст {youngest[2]}')
#     file.close()
#
# with open('oldest.txt', 'w') as file:
#     file.write(f'Самый старший ребенок: {oldest[0]} {oldest[1]}, возраст {oldest[2]}')
#     file.close()
# print('Данные записаны в youngest.txt и oldest.txt')
# f.close()

# #№4
# import json
# import csv
# import os
#
# def json_to_csv(json_file):
#     with open(json_file, 'r') as f:
#         data = json.load(f)
#
#     csv_filename = os.path.splitext(json_file)[0] + '.csv'
#
#     if not data:
#         print("JSON файл пуст.")
#         return
#
#     if isinstance(data, list):
#         if not data:
#             print("JSON файл не содержит записей.")
#             return
#         headers = list(data[0].keys())
#     elif isinstance(data, dict):
#         headers = list(data.keys())
#         data = [data]
#     else:
#         print("Некорректный формат JSON данных.")
#         return
#
#     with open(csv_filename, 'w', newline='') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=headers)
#         writer.writeheader()
#         for row in data:
#             writer.writerow(row)
#
#     print(f"JSON файл преобразован в CSV. Результат записан в {csv_filename}.")
#
# if __name__ == "__main__":
#     json_file = "Sample-employee-JSON-data.json"
#     json_to_csv(json_file)