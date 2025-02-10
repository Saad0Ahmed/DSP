def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half, right_half = arr[:mid], arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            arr[k] = left_half[i] if left_half[i] < right_half[j] else right_half[j]
            k += 1
            if left_half[i] < right_half[j]: i += 1
            else: j += 1

        while i < len(left_half): arr[k] = left_half[i]; i += 1; k += 1
        while j < len(right_half): arr[k] = right_half[j]; j += 1; k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Merge sort original array:", arr)
merge_sort(arr)
print("Merge sort sorted array:", arr)

def quicksort(arr1):
    if len(arr1) <= 1:
        return arr1 #base case: already sorted
    pivot = arr1[len(arr1)//2] # choose the middle element as pivot
    left = [x for x in arr1 if x < pivot] #element smaller than pivot
    middle = [x for x in arr1 if x == pivot] #element equal to pivot
    right = [x for x in arr1 if x > pivot] #element is greater than pivot
    return quicksort(left) + middle + quicksort(right) #recurrsively sort and cobmine

#example usage
arr1 = [45,78,85,47,12,39,90,4]
sorted_arr1 = quicksort(arr1)
print("Quick sort sorted array: ", sorted_arr1)