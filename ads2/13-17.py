# #13
#
# # Функция хеширования (берем сумму кодов символов строки по модулю длины таблицы)
#
#
# def hash_function(key, size):
#     return sum(ord(char) for char in key) % size
#
#
# # Класс для элемента таблицы (узла связного списка)
# class HashNode:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
#
#
# # Класс для хеш-таблицы с наложением
# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [None] * size  # Инициализация пустой таблицы заданного размера
#
#     # Метод добавления элемента в таблицу
#     def insert(self, key, value):
#         index = hash_function(key, self.size)
#
#         # Создание нового узла
#         new_node = HashNode(key, value)
#
#         # Если ячейка пуста, вставляем новый узел
#         if self.table[index] is None:
#             self.table[index] = new_node
#         else:
#             # Вставляем узел в начало цепочки (наложение)
#             current = self.table[index]
#             while current.next is not None and current.key != key:
#                 current = current.next
#             if current.key == key:
#                 current.value = value  # Обновляем значение, если ключ уже существует
#             else:
#                 current.next = new_node  # Вставка в конец цепочки
#
#     # Метод поиска элемента по ключу
#     def search(self, key):
#         index = hash_function(key, self.size)
#         current = self.table[index]
#         while current is not None:
#             if current.key == key:
#                 return current.value
#             current = current.next
#         return None
#
#     # Метод отображения таблицы (для проверки)
#     def display(self):
#         for i, node in enumerate(self.table):
#             print(f"Index {i}:", end=" ")
#             current = node
#             while current is not None:
#                 print(f"({current.key}: {current.value}) -> ", end="")
#                 current = current.next
#             print("None")
#
#     # Метод записи таблицы в файл
#     def write_to_file(self, filename):
#         with open(filename, 'w', encoding='utf-8') as file:
#             for i, node in enumerate(self.table):
#                 file.write(f"Index {i}: ")
#                 current = node
#                 while current is not None:
#                     file.write(f"({current.key}: {current.value}) -> ")
#                     current = current.next
#                 file.write("None\n")
#
#
# # Чтение из файла и построение хеш-таблицы
# def read_file_and_create_hash_table(filename, table_size=10):
#     hash_table = HashTable(table_size)
#     with open(filename, 'r', encoding='utf-8') as file:
#         for line in file:
#             words = line.strip().split()
#             for word in words:
#                 # Вставляем слово в хеш-таблицу
#                 hash_table.insert(word, word)  # Можно использовать любое значение вместо 'word'
#     return hash_table
#
#
# # Пример использования
# filename = 'text.txt'  # Укажите путь к вашему текстовому файлу
# output_filename = 'hash_table_output.txt'  # Укажите путь к результирующему файлу
# hash_table = read_file_and_create_hash_table(filename, 10)
# hash_table.display()
# hash_table.write_to_file(output_filename)
# print(f"Хеш-таблица записана в файл {output_filename}")



# def hash_function(key, size):
#     return sum(ord(char) for char in key) % size
#
# # Класс для хеш-таблицы с наложением (открытая адресация)
# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [None] * size  # Инициализация пустой таблицы заданного размера
#
#     # Метод добавления элемента в таблицу с линейным пробированием
#     def insert(self, key, value):
#         index = hash_function(key, self.size)
#         start_index = index
#
#         # Поиск следующей доступной ячейки в случае коллизии
#         while self.table[index] is not None:
#             if self.table[index][0] == key:
#                 # Если ключ уже существует, обновляем значение
#                 self.table[index] = (key, value)
#                 return
#             index = (index + 1) % self.size
#             # Если возвращаемся к стартовому индексу, таблица заполнена
#             if index == start_index:
#                 print("Ошибка: Таблица заполнена")
#                 return
#
#         # Вставляем новый элемент
#         self.table[index] = (key, value)
#
#     # Метод поиска элемента по ключу
#     def search(self, key):
#         index = hash_function(key, self.size)
#         start_index = index
#
#         # Поиск ключа с линейным пробированием
#         while self.table[index] is not None:
#             if self.table[index][0] == key:
#                 return self.table[index][1]
#             index = (index + 1) % self.size
#             if index == start_index:
#                 break
#         return None
#
#     # Метод отображения таблицы (для проверки)
#     def display(self):
#         for i, element in enumerate(self.table):
#             print(f"Index {i}: {element}")
#
#     # Метод записи таблицы в файл
#     def write_to_file(self, filename):
#         with open(filename, 'w', encoding='utf-8') as file:
#             for i, element in enumerate(self.table):
#                 file.write(f"Index {i}: {element}\n")
#
# # Чтение из файла и построение хеш-таблицы
# def read_file_and_create_hash_table(filename, table_size=10):
#     hash_table = HashTable(table_size)
#     with open(filename, 'r', encoding='utf-8') as file:
#         for line in file:
#             words = line.strip().split()
#             for word in words:
#                 # Вставляем слово в хеш-таблицу
#                 hash_table.insert(word, word)  # Можно использовать любое значение вместо 'word'
#     return hash_table
#
# # Пример использования
# filename = 'text.txt'  # Укажите путь к вашему текстовому файлу
# output_filename = 'output1.txt'  # Укажите путь к результирующему файлу
# hash_table = read_file_and_create_hash_table(filename, 10)
# hash_table.display()
# hash_table.write_to_file(output_filename)
# print(f"Хеш-таблица записана в файл {output_filename}")


# #14
# import re
# #
# # Размер таблицы
# TABLE_SIZE = 10
#
#
# # Хеш-функция: сумма кодов символов % размер таблицы
# def hash_function(key):
#     return sum(ord(char) for char in key) % TABLE_SIZE
#
#
# # Создание хеш-таблицы с цепочками (списками)
# def create_hash_table(filename):
#     hash_table = [[] for _ in range(TABLE_SIZE)]
#
#     # Чтение файла и добавление слов в таблицу
#     with open(filename, 'r', encoding='utf-8') as file:
#         text = file.read()
#         # Разделение текста на слова
#         words = re.findall(r'\b\w+\b', text)
#
#         for word in words:
#             index = hash_function(word)
#             hash_table[index].append(word)
#
#     return hash_table
#
#
# # Запись хеш-таблицы в файл
# def write_hash_table(hash_table, output_filename):
#     with open(output_filename, 'w', encoding='utf-8') as file:
#         for i, chain in enumerate(hash_table):
#             # Структура вывода для каждого индекса
#             chain_output = " -> ".join(f"({word}: {word})" for word in chain) if chain else "None"
#             file.write(f"Index {i}: {chain_output}\n")
#
#
# # Основная часть программы
# input_filename = 'text.txt'  # Исходный файл с текстом
# output_filename = 'output.txt'  # Файл для записи хеш-таблицы
#
# # Создаем хеш-таблицу и записываем ее в файл
# hash_table = create_hash_table(input_filename)
# write_hash_table(hash_table, output_filename)
#
# print(f"Хеш-таблица записана в файл {output_filename}")





#15

# import re
#
# class Node:    #Класс узла бинарного дерева
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# class BinaryTree:    #Класс бинарного дерева
#     def __init__(self, root=None):
#         self.root = root
#
#     @staticmethod
#     def parse_tree(tree_str):    #Разбор строки в формате линейно-скобочной записи
#         def h(tokens):
#             if not tokens:
#                 return None
#             value = tokens.pop(0)
#             if value == ',' or value == ')':  # Пустое поддерево
#                 return None
#             node = Node(int(value))
#             if tokens and tokens[0] == '(':
#                 tokens.pop(0)  # Убираем '('
#                 node.left = h(tokens)
#                 if tokens and tokens[0] == ',':
#                     tokens.pop(0)  # Убираем ','
#                 node.right = h(tokens)
#                 if tokens and tokens[0] == ')':
#                     tokens.pop(0)  # Убираем ')'
#             return node
#
#         # Разбиваем строку на токены (узлы, скобки и запятые)
#         tokens = re.findall(r'\d+|[(),]', tree_str)
#         return h(tokens)
#
#     def preorder_traversal(self, node, result=None):     #Прямой обход
#
#         if result is None:
#             result = []
#         if node:
#             result.append(node.value)
#             self.preorder_traversal(node.left, result)
#             self.preorder_traversal(node.right, result)
#         return result
#
#     def inorder_traversal(self, node, result=None):        #Центральный обход
#
#         if result is None:
#             result = []
#         if node:
#             self.inorder_traversal(node.left, result)
#             result.append(node.value)
#             self.inorder_traversal(node.right, result)
#         return result
#
#     def postorder_traversal(self, node, result=None):#Концевой обход
#
#         if result is None:
#             result = []
#         if node:
#             self.postorder_traversal(node.left, result)
#             self.postorder_traversal(node.right, result)
#             result.append(node.value)
#         return result
#
#
# # Пример
# tree_str = "8 (3 (1, 6 (4,7)), 10 (, 14(13,)))"
# binary_tree = BinaryTree()
# binary_tree.root = BinaryTree.parse_tree(tree_str)
#
# print("Прямой обход:", binary_tree.preorder_traversal(binary_tree.root))
# print("Центральный обход:", binary_tree.inorder_traversal(binary_tree.root))
# print("Концевой обход:", binary_tree.postorder_traversal(binary_tree.root))



#16

# class Node:
#     """Класс узла бинарного дерева"""
#
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# class BinaryTree:
#     """Класс бинарного дерева"""
#
#     def __init__(self, root=None):
#         self.root = root
#
#     @staticmethod
#     def parse_tree(tree_str):
#         """Разбор строки в формате линейно-скобочной записи"""
#         import re
#
#         def helper(tokens):
#             if not tokens:
#                 return None
#             value = tokens.pop(0)
#             if value == ',' or value == ')':  # Пустое поддерево
#                 return None
#             node = Node(int(value))
#             if tokens and tokens[0] == '(':
#                 tokens.pop(0)  # Убираем '('
#                 node.left = helper(tokens)
#                 if tokens and tokens[0] == ',':
#                     tokens.pop(0)  # Убираем ','
#                 node.right = helper(tokens)
#                 if tokens and tokens[0] == ')':
#                     tokens.pop(0)  # Убираем ')'
#             return node
#
#         # Разбиваем строку на токены (узлы, скобки и запятые)
#         tokens = re.findall(r'\d+|[(),]', tree_str)
#         return helper(tokens)
#
#     def iterative_preorder(self):
#         """Нерекурсивный прямой обход (NLR) с использованием стека"""
#         if not self.root:
#             return ""
#
#         stack = [self.root]
#         result = []
#
#         while stack:
#             node = stack.pop()
#             result.append(str(node.value))  # Добавляем значение узла в результат
#
#             # Сначала добавляем правого потомка, затем левого,
#             # чтобы левый обрабатывался первым (в соответствии с прямым обходом)
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#
#         return " ".join(result)  # Возвращаем строку обхода
#
#
# # Пример использования
# tree_str = "8 (3 (1, 6 (4,7)), 10 (, 14(13,)))"
# binary_tree = BinaryTree()
# binary_tree.root = BinaryTree.parse_tree(tree_str)
#
# # Выполняем нерекурсивный прямой обход
# print("Нерекурсивный прямой обход (NLR):", binary_tree.iterative_preorder())


#17

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def from_string(self, s):
        """Создает дерево из линейно-скобочной записи."""
        def parse(subtree):
            if not subtree:
                return None

            # Извлекаем корневое значение
            i = subtree.find('(')
            if i == -1:
                return Node(int(subtree))

            value = int(subtree[:i].strip())
            node = Node(value)

            # Находим границы поддеревьев
            stack, start = 0, i + 1
            for j in range(start, len(subtree)):
                if subtree[j] == '(':
                    stack += 1
                elif subtree[j] == ')':
                    stack -= 1
                elif subtree[j] == ',' and stack == 0:
                    node.left = parse(subtree[start:j].strip())
                    node.right = parse(subtree[j + 1:-1].strip())
                    break

            return node

        self.root = parse(s.strip())

    def to_string(self, node=None):
        """Возвращает дерево в линейно-скобочной записи с правильным форматированием."""
        if node is None:
            node = self.root
        if not node:
            return ''

        left = self.to_string(node.left) if node.left else ''
        right = self.to_string(node.right) if node.right else ''

        # Формируем строку с учетом наличия левого и правого поддерева
        if left or right:
            return f"{node.value} ({left}{',' if left or right else ''}{right})"
        else:
            return f"{node.value}"

    def add(self, value):
        """Добавляет значение в БДП."""
        if not self.root:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    break

    def find(self, value):
        """Ищет значение в БДП."""
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, value):
        """Удаляет узел с заданным значением."""
        def delete_node(node, value):
            if not node:
                return None

            if value < node.value:
                node.left = delete_node(node.left, value)
            elif value > node.value:
                node.right = delete_node(node.right, value)
            else:
                # Узел найден
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                # Найти минимальный узел в правом поддереве
                min_larger_node = node.right
                while min_larger_node.left:
                    min_larger_node = min_larger_node.left
                node.value = min_larger_node.value
                node.right = delete_node(node.right, min_larger_node.value)

            return node

        self.root = delete_node(self.root, value)

# Меню для взаимодействия с деревом
def menu():
    tree = BinaryTree()

    # Ввод дерева
    input_string = input("Введите дерево в линейно-скобочной записи: ")
    tree.from_string(input_string)

    while True:
        print("\nМеню:")
        print("1. Добавить вершину")
        print("2. Удалить вершину")
        print("3. Найти вершину")
        print("4. Показать дерево в линейно-скобочной записи")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            value = int(input("Введите значение для добавления: "))
            tree.add(value)
            print("Значение добавлено.")

        elif choice == '2':
            value = int(input("Введите значение для удаления: "))
            tree.delete(value)
            print("Значение удалено.")

        elif choice == '3':
            value = int(input("Введите значение для поиска: "))
            found = tree.find(value)
            print("Значение найдено." if found else "Значение не найдено.")

        elif choice == '4':
            print("Текущее дерево:", tree.to_string())

        elif choice == '5':
            print("Текущее дерево:", tree.to_string())
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu()