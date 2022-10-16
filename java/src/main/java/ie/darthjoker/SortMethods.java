package ie.darthjoker;

import java.util.Arrays;

public class SortMethods {
    private static int times = 0;

    private static int[] bubbleSort(int[] array) {
        long startTime = System.nanoTime();
        int length = array.length;
        int n = 0;

        for (int i = 0; i < length - 1; i++) {
            for (int j = 0; j < length - i - 1; j++) {
                n++;
                if (array[j] > array[j + 1]) {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }

        long elapsedTime = System.nanoTime() - startTime;
        System.out.printf("It took %sms and %s compares.%n", elapsedTime/1000000, n);

        return array;
    }

    private static int partition(int[] x, int l, int r)
    {
        int pivot = x[r];
        int i = l - 1;

        for (int j = l; j < r; j++) {
            times++;
            if (x[j] < pivot) {
                i++;
                int temp = x[i];
                x[i] = x[j];
                x[j] = temp;
            }
        }

        int temp = x[i+1];
        x[i+1] = x[r];
        x[r] = temp;

        return i + 1;
    }

    private static void quickSort(int[] array, int l, int r) {
        if (l < r) {
            int pivotIndex = partition(array, l, r);
            quickSort(array, l, pivotIndex - 1);
            quickSort(array, pivotIndex + 1, r);
        }
    }

    public static void main(String[] args) {
        int length = 1000;

        int[] arrayToSort = new int[length];
        for (int i = length; i > 0; i--) {
            arrayToSort[i-1] = i;
        }

        bubbleSort(arrayToSort);

        int[] arrayToQuickSort = new int[length];
        for (int i = length; i > 0; i--) {
            arrayToQuickSort[i-1] = i;
        }

        times = 0;
        long startTime = System.nanoTime();
        quickSort(arrayToQuickSort, 0, arrayToQuickSort.length - 1);
        long elapsedTime = System.nanoTime() - startTime;
        System.out.printf("It took %sms and %s compares.%n", elapsedTime/1000000, times);

        System.out.println(Arrays.toString(arrayToQuickSort));
    }
}
