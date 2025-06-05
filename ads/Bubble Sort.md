## Название алгоритма – Сортировка пузырьком (Bubble Sort)

**Описание алгоритма** – сортировка пузырьком — простой алгоритм сортировки, который многократно проходит по списку, сравнивая соседние элементы и меняя их местами, если они идут в неправильном порядке. На каждой итерации самый "тяжёлый" элемент "всплывает" в конец.

**Особенности:**

- Прост в реализации

- Неэффективен на больших массивах

- Стабильный алгоритм

**Реализация алгоритма**
```java
import java.util.*;
import java.lang.*;
import java.io.*;

class BubbleSort {
    public static void sort(int[] arr) {
        int n = arr.length;
        boolean swapped;
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
    }
}

class Main {
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 5, 6};
        BubbleSort.sort(arr);
        // Print the sorted array
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
```
#### Алгоритмическая сложность алгоритма 

- Лучший случай: O(n) (если массив уже отсортирован)

- Средний случай: O(n²)

- Худший случай: O(n²)

