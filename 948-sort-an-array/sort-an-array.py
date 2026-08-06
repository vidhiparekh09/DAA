class Solution(object):

    def merge(self, arr, low, mid, high):
        left = arr[low:mid+1]
        right = arr[mid+1:high+1]

        i = 0
        j = 0
        k = low

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, arr, low, high):
        if low < high:
            mid = (low + high) // 2
            self.mergeSort(arr, low, mid)
            self.mergeSort(arr, mid + 1, high)
            self.merge(arr, low, mid, high)

    def sortArray(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums