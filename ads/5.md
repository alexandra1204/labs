## Название алгоритма – Сортировка слиянием (Merge Sort)

**Описание алгоритма** – cортировка слиянием также использует подход "разделяй и властвуй": массив делится пополам, каждая половина сортируется рекурсивно, затем сливаются в один отсортированный массив.

**Особенности:**

- Стабильный алгоритм

- Требует дополнительную память

- Эффективен для работы с файлами или большими структурами

**Реализация алгоритма**
```java
import java.util.*;
import java.lang.*;
import java.io.*;

class MergeSort {
    public static void sort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            sort(arr, left, mid);
            sort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    private static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        for (int i = 0; i < n1; i++) L[i] = arr[left + i];
        for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k++] = L[i++];
            } else {
                arr[k++] = R[j++];
            }
        }

        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }
}


class Main {
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 5, 6};
        MergeSort.sort(arr, 0, arr.length - 1);

        // Print the sorted array
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
```
#### Алгоритмическая сложность алгоритма 

- Лучший случай: O(n log n)

- Средний случай: O(n log n)

- Худший случай: O(n log n)
