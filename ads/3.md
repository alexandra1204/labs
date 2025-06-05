## Название алгоритма – Сортировка выбором (Selection Sort)

**Описание алгоритма** – сортировка выбором находит минимальный элемент и ставит его в начало, затем ищет следующий минимальный — и так далее. Количество операций обмена — минимально.

**Особенности:**

- Прост в реализации

- Неустойчивый

- Всегда выполняет одинаковое число сравнений

**Реализация алгоритма**
```java
import java.util.*;
import java.lang.*;
import java.io.*;

class SelectionSort {
    public static void sort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[minIdx];
            arr[minIdx] = temp;
        }
    }
}

class Main {
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 5, 6};
        SelectionSort.sort(arr);

        // Print the sorted array
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
```
#### Алгоритмическая сложность алгоритма 

- Лучший случай: O(n²)

- Средний случай: O(n²)

- Худший случай: O(n²)
