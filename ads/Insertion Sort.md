## Название алгоритма – Сортировка вставками (Insertion Sort)

**Описание алгоритма** – сортировка вставками проходит по массиву и "вставляет" каждый элемент на нужное место в уже отсортированной части массива. Эффективен при небольшом объёме данных и частично отсортированных массивах.

**Реализация алгоритма**
```java
import java.util.*;
import java.lang.*;
import java.io.*;

class InsertionSort {
    public static void sort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }
}

class Main {
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 5, 6};
        InsertionSort.sort(arr);

        // Print the sorted array
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
```
#### Алгоритмическая сложность алгоритма 

- Лучший случай: O(n)

- Средний случай: O(n²)

- Худший случай: O(n²)
