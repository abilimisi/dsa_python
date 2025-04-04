# Time Complexity: O(n2) ,as there are two nested loops
# space: O(1)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):

        min_val = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_val]:  # first checking min val in arr
                min_val = j

        arr[i], arr[min_val] = arr[min_val], arr[i]
        print(arr)


arr = [64, 25, 12, 22, 11]
selection_sort(arr)
for res in arr:
    print(res, end=" ")
print()
