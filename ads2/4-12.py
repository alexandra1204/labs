# Лабы №4-12 "Методы сортировки"
# Дана последовательность чисел. Отсортировать и вывести последовательность чисел, определённым методом.

# №4 Сортировка методом прочесывания

# def Sort(a):
#     step=int(len(a)//1.25)
#     while step>0:
#         for i in range(0,len(a)-step):
#             if (a[i]>a[i+step]):
#                 a[i],a[i+step]=a[i+step],a[i]
#         step=int(step//1.25)
#     return a
#
# arr=[2,7,3,9,4,8,5,1,6]
#
# print(Sort(arr))


# №5 Вставками


# def Sort(a):
#     for i in range (1,len(a)):
#         while (i>0 and a[i]<a[i-1]):
#             a[i],a[i-1]=a[i-1],a[i]
#             i-=1
#     return a
# arr = [2,7,3,9,4,8,5,1,6]
# print(Sort(arr))


# №6 Посредством выбора

# def Sort(a):
#     for i in range(0,len(a)):
#         for n in range(i+1,len(a)):
#             if(a[n]<a[i]):
#                 a[i],a[n]=a[n],a[i]
#     return a
# arr=[2,7,3,9,4,8,5,1,6]
# print(Sort(arr))


# №7 Шелла
# import math
#
# def Sort(a):
#     n = len(a)
#     k = int(math.log2(n))
#     interval = 2**k -1
#     while interval > 0:
#         for i in range(interval, n):
#             temp = a[i]
#             j = i
#             while j >= interval and a[j - interval] > temp:
#                 a[j] = a[j - interval]
#                 j -= interval
#             a[j] = temp
#         k -= 1
#         interval = 2**k -1
#     return a
#
# arr=[2,7,3,9,4,8,5,1,6]
# print(Sort(arr))

# №8 Поразрядная

#
# def Sort(arr):
#     max_digits = max([len(str(x)) for x in arr])
#     # основание системы счисления
#     base = 10
#     # промежуточный пустой массив
#     bins = [[] for _ in range(base)]
#     for i in range(0, max_digits):
#         for x in arr:
#             digit = (x // base ** i) % base
#             bins[digit].append(x)
#         arr = [x for q in bins for x in q]
#         bins = [[] for _ in range(base)]
#     return arr
#
# arr=[1371371, 2439573, 474290561035, 5, 276, 42]
# print(Sort(arr))
#
#
# # №9 Пирамидальная (heap sort)
#
#
# def heapsort(alist):
#     build_max_heap(alist)
#     for i in range(len(alist) - 1, 0, -1):
#         alist[0], alist[i] = alist[i], alist[0]
#         max_heapify(alist, index=0, size=i)
#
#
# def parent(i):
#     return (i - 1) // 2
#
#
# def left(i):
#     return 2 * i + 1
#
#
# def right(i):
#     return 2 * i + 2
#
#
# def build_max_heap(alist):
#     length = len(alist)
#     start = parent(length - 1)
#     while start >= 0:
#         max_heapify(alist, index=start, size=length)
#         start = start - 1
#
#
# def max_heapify(alist, index, size):
#     l = left(index)
#     r = right(index)
#     if (l < size and alist[l] > alist[index]):
#         largest = l
#     else:
#         largest = index
#     if (r < size and alist[r] > alist[largest]):
#         largest = r
#     if (largest != index):
#         alist[largest], alist[index] = alist[index], alist[largest]
#         max_heapify(alist, largest, size)
#
#
# alist = input('Enter the list of numbers: ').split()
# alist = [int(x) for x in alist]
# heapsort(alist)
# print('Sorted list: ', end='')
# print(alist)
#
#
# # №10 Слиянием
#
#
# def mySort(A):
#     if len(A) <= 1:
#         return (A)
#     L = mySort(A[:len(A) // 2])
#     R = mySort(A[len(A) // 2:])
#     B = []
#     l = r = 0
#     while l < len(L) and r < len(R):
#         B.append(L[l] if L[l] <= R[r] else R[r])
#         [l, r] = [l + 1, r] if L[l] <= R[r] else [l, r + 1]
#     for l in range(l, len(L)):
#         B.append(L[l])
#     for r in range(r, len(R)):
#         B.append(R[r])
#     return B
#
#
# a = [7, 5, 3, 1, 4, 9, 3, 2]
# print(mySort(a))
#
#
# # №11 Быстрая
#
#
# def quicksort(nums, fst, lst):
#     if fst >= lst: return
#
#     i, j = fst, lst
#     pivot = nums[random.randint(fst, lst)]
#
#     while i <= j:
#         while nums[i] < pivot: i += 1
#         while nums[j] > pivot: j -= 1
#         if i <= j:
#             nums[i], nums[j] = nums[j], nums[i]
#             i, j = i + 1, j - 1
#     quicksort(nums, fst, j)
#     quicksort(nums, i, lst)
#
#
#
#
# def quicksort(nums):
#    if len(nums) <= 1:
#        return nums
#    else:
#        q = random.choice(nums)
#        s_nums = []
#        m_nums = []
#        e_nums = []
#        for n in nums:
#            if n < q:
#                s_nums.append(n)
#            elif n > q:
#                m_nums.append(n)
#            else:
#                e_nums.append(n)
#        return quicksort(s_nums) + e_nums + quicksort(m_nums)

# №12 Внешняя многофазная


# def multiphase_sort(array):
#     # Сгенерируем ряд Фибоначчи, который будет использоваться для разделения массива на фазы
#     fibonacci_series = [0, 1]
#     while fibonacci_series[-1] < len(array):
#         fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
#
#         # Определим функцию для сортировки одной фазы
#
#     def sort_phase(array, distance):
#         # Сортируем каждую пару элементов, расположенных на расстоянии distance друг от друга
#         for i in range(distance, len(array)):
#             j = i
#             while j > 0 and array[j] < array[j - distance]:
#                 # Меняем элементы местами, если требуется
#                 array[j], array[j - distance] = array[j - distance], array[j]
#                 j -= distance
#
#                 # Сортируем каждую фазу отдельно
#
#     for distance in fibonacci_series[::-1]:
#         sort_phase(array, distance)
#
#     # Проверяем работу функции
#
#
# array = [5, 3, 8, 6, 1, 9, 2, 7, 4]
# multiphase_sort(array)
# print(array)  # Должно вывести [1, 2, 3, 4, 5, 6, 7, 8, 9]



import heapq
import os

def external_sort(input_file, output_file, chunk_size=100):
    """
    Реализация внешней многофазной сортировки.
    :param input_file: Имя входного файла с числами.
    :param output_file: Имя выходного файла с отсортированными числами.
    :param chunk_size: Размер одной порции данных для сортировки в памяти.
    """
    temp_files = []

    # Фаза 1: Разбиение и сортировка
    with open(input_file, 'r') as file:
        while True:
            # Читаем часть данных
            lines = file.readlines(chunk_size)
            if not lines:
                break

            # Преобразуем строки в числа
            numbers = [int(line.strip()) for line in lines]
            numbers.sort()  # Сортируем в памяти

            # Сохраняем отсортированный блок в временный файл
            temp_file_name = f'temp_{len(temp_files)}.txt'
            with open(temp_file_name, 'w') as temp_file:
                temp_file.writelines(f"{num}\n" for num in numbers)
            temp_files.append(temp_file_name)

    # Фаза 2: Многофазное слияние
    with open(output_file, 'w') as output:
        # чтениe из временных файлов
        iterators = [open(file, 'r') for file in temp_files]
        heap = []

        # Инициализация кучи
        for i, it in enumerate(iterators):
            line = it.readline()
            if line:
                heapq.heappush(heap, (int(line.strip()), i))

        # Слияние
        while heap:
            smallest, file_index = heapq.heappop(heap)
            output.write(f"{smallest}\n")
            next_line = iterators[file_index].readline()
            if next_line:
                heapq.heappush(heap, (int(next_line.strip()), file_index))

        # Закрываем временные файлы
        for it in iterators:
            it.close()

    # Удаляем временные файлы
    for file in temp_files:
        os.remove(file)

# Пример использования
if __name__ == "__main__":
    # Создаем входной файл с числами
    with open("input.txt", "w") as f:
        f.write("50\n20\n60\n10\n40\n30\n70\n90\n80\n100\n")

    # Выполняем внешнюю сортировку
    external_sort("input.txt", "output.txt")

    # Читаем отсортированный результат
    with open("output.txt", "r") as f:
        print(f.read())