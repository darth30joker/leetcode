package ie.darthjoker;

import java.util.Arrays;

public class BubbleSort {
    private static void sort(int[] array) {
        int length = array.length;

        for (int i = 0; i < length - 1; i++) {
            for (int j = 0; j < length - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }

        System.out.println(Arrays.toString(array));
    }

    public static void main(String[] args) {
        sort(new int[]{1, 5, 3});
        sort(new int[]{10, 9, 8, 7, 6, 5, 4, 3, 2, 1});
    }
}
