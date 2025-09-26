import csv
import random
import collections
import os
class TitanicDataViewer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()
    def load_data(self):
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data

    def show(self, view_type='top', num_rows=5, separator=','):
        if view_type == 'top':
            displayed_data = self.data[:num_rows]
        elif view_type == 'bottom':
            displayed_data = self.data[-num_rows:]
        elif view_type == 'random':
            displayed_data = random.sample(self.data, min(num_rows, len(self.data)))
        else:
            print("Неправильный тип вывода (Введите top, bottom или random)")
            return

        if len(displayed_data) < 5:
            print(f"Строк меньше пяти.")

        max_lengths = [max(len(str(cell)) for cell in column) for column in zip(*displayed_data)]
        for row in displayed_data:
            print(separator.join(str(cell).ljust(length) for cell, length in zip(row, max_lengths)))

    def info(self):
        if not self.data:
            print("Нет доступных данных.")
            return

        num_rows = len(self.data) - 1
        num_columns = len(self.data[0])
        print(f"Rows x Columns: {num_rows}x{num_columns}")

        headers = self.data[0]
        data_types = collections.defaultdict(lambda: {'Qty': 0, 'Type': set()})
        for row in self.data[1:]:
            for idx, value in enumerate(row):
                if value.strip():
                    data_types[headers[idx]]['Qty'] += 1
                    data_types[headers[idx]]['Type'].add(self.get_data_type(value))

        print("Field\t\t\tQty\t\tType")
        for field, info in data_types.items():
            qty = info['Qty']
            data_type = ', '.join(info['Type'])
            print(f"{field.ljust(16)}{qty}\t\t{data_type}")

    def get_data_type(self, value):
        try:
            int(value)
            return 'int'
        except ValueError:
            try:
                float(value)
                return 'float'
            except ValueError:
                return 'str'
    def DelNaN(self):
        self.data = [row for row in self.data if all(cell.strip() for cell in row)]

    def MakeDS(self):
        random.shuffle(self.data)
        train_size = int(0.7 * len(self.data))
        train_data = self.data[:train_size]
        test_data = self.data[train_size:]

        workdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'workdata')
        if not os.path.exists(workdir):
            os.makedirs(workdir)
        learning_dir = os.path.join(workdir, 'Learning')
        testing_dir = os.path.join(workdir, 'Testing')
        os.makedirs(learning_dir, exist_ok=True)
        os.makedirs(testing_dir, exist_ok=True)

        with open(os.path.join(learning_dir, 'train.csv'), 'w', newline='') as train_file:
            writer = csv.writer(train_file)
            writer.writerows(train_data)
        with open(os.path.join(testing_dir, 'test.csv'), 'w', newline='') as test_file:
            writer = csv.writer(test_file)
            writer.writerows(test_data)

        print("Данные записаны в папку workdata.")

# Функция Show():
print("\nФункция Show():")
viewer = TitanicDataViewer("Titanic.csv")

print("Вывод по умолчанию:")
viewer.show()

print("Top:")
viewer.show(view_type='top')

print("\nBottom:")
viewer.show(view_type='bottom')

print("\nRandom:")
viewer.show(view_type='random')

print("\nПользовательский:")
viewer.show(view_type=input("\nТип вывода (введите top, bottom или random): "),num_rows=int(input("\nКоличество выводимых строк: ")), separator=input("\nРазделитель: "))


# Функция Info()
print("\nФункция Info()")
viewer = TitanicDataViewer("Titanic.csv")
viewer.info()

# Функция  DelNaN()
print("\nФункция  DelNaN()")
viewer = TitanicDataViewer("Titanic.csv")
viewer.DelNaN()
print("Данные после удаления строк с пустыми ячейками:")
viewer.show(num_rows=len(viewer.data), separator='|')

# Функция MakeDS()
print("\nФункция MakeDS()")
viewer = TitanicDataViewer("Titanic.csv")
viewer.MakeDS()


