import numpy as np
from scipy.linalg import det, inv
from scipy.stats import multivariate_normal


# #№1
#
# matrix = np.loadtxt('1.txt', delimiter=',')
# summ = np.sum(matrix)
# maxx = np.max(matrix)
# minn = np.min(matrix)
#
# print(f"Сумма всех элементов: {summ}")
# print(f"Максимальный элемент: {maxx}")
# print(f"Минимальный элемент: {minn}")


# #№2
# def run_length_encoding(x):
#
#     values = []
#     counts = []
#
#     current_value = x[0]
#     count = 1
#
#     for i in range(1, len(x)):
#         if x[i] == current_value:
#             count += 1
#         else:
#             values.append(current_value)
#             counts.append(count)
#             current_value = x[i]
#             count = 1
#
#     values.append(current_value)
#     counts.append(count)
#
#     return np.array(values), np.array(counts)
#
# x = np.array([2, 3, 3, 4, 4, 4])
# values, counts = run_length_encoding(x)
# print(f"Values: {values}")
# print(f"Counts: {counts}")


# #№3
#
# np.random.seed(0)
# array = np.random.randn(10, 4)
#
# min_value = np.min(array)
# max_value = np.max(array)
# mean_value = np.mean(array)
# std_deviation = np.std(array)
# first_5_rows = array[:5, :]
#
# print(f"Массив:\n{array}")
# print(f"Минимальное значение: {min_value}")
# print(f"Максимальное значение: {max_value}")
# print(f"Среднее значение: {mean_value}")
# print(f"Стандартное отклонение: {std_deviation}")
# print(f"Первые 5 строк:\n{first_5_rows}")


# #№4
#
# x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
# indices = np.where(x[:-1] == 0)[0]
# max_element = np.max(x[indices + 1])
# print("Ответ:", max_element)


# #№5
#
# def logpdf_multivariate_normal(X, m, C):
#     D = X.shape[1]
#     diff = X - m.reshape(1, D)
#     inv_cov = inv(C)
#     log_det_cov = np.log(det(C))
#     log_density = -0.5 * (D * np.log(2 * np.pi) + log_det_cov + np.sum(diff @ inv_cov * diff, axis=1))
#     return log_density
#
# m = np.array([0, 0])
# C = np.array([[1, 0.5], [0.5, 2]])
# X = np.array([[1, 2], [2, 3], [3, 4]])
#
# log_custom = logpdf_multivariate_normal(X, m, C)
# log_scipy = multivariate_normal(m, C).logpdf(X)
#
# print("Логарифм плотности многомерного нормального распределения (вручную):")
# print(log_custom)
# print("\nЛогарифм плотности многомерного нормального распределения (Scipy):")
# print(log_scipy)


# #№6
#
# a = np.arange(16).reshape(4, 4)
# print("Исходный массив:")
# print(a)
#
# a[[0, 2]] = a[[2, 0]]
#
# print("\nМассив после замены строк:")
# print(a)


# #№7
#
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris = np.genfromtxt(url, delimiter=',', dtype='object')
#
# species_column = iris[:, 4]
# unique_species, counts = np.unique(species_column, return_counts=True)
#
# for species, count in zip(unique_species, counts):
#     print(f"Вид: {species.decode('utf-8')}, Количество: {count}")


#№8

arr = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
nonzero_indices = np.nonzero(arr)

print("Индексы ненулевых элементов:")
print(*nonzero_indices)