package me.joohyuk.sort;

public class QuickSort {
    public static void main(String[] args) {
    }

    public static void quickSortRecursive(int[] nums, int left, int right) {
        if (left >= right) {
            return;
        }

        int pivotPos = partition(nums, left, right);

        quickSortRecursive(nums, left, pivotPos - 1);
        quickSortRecursive(nums, pivotPos + 1, right);
    }

    private static int partition(int[] nums, int left, int right) {
        int pivot = nums[right];

        int i = (left - 1);
        for (int j = left; j < right; ++j) {
            if (nums[j] < pivot) {
              ++i;
              swap(nums, i, j);
            }
        }

        int pivotPos = i + 1;
        swap(nums, pivotPos, right);

        return pivotPos;
    }

    private static void swap(int[] nums, int pivotPos, int right) {
        int temp = nums[pivotPos];
        nums[pivotPos] = nums[right];
        nums[right] = temp;
    }
}
