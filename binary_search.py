# Time complexity - O(logn)
# auxiliary space - O(1)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    # step = 0

    while low <= high:

        # step+=1
        mid = (low + high) // 2

        if arr[mid] == target:
            # print(step)
            return mid

        elif arr[mid] < target:
            low = mid + 1

        elif arr[mid] > target:
            high = mid - 1

    return -1


arr = [1, 2, 4, 7, 9]  # must be sorted
target = 9

result = binary_search(arr, target)

if result != -1:
    print(f"number found at index : {result}")
else:
    print("number not found")


# ---------------------------------------------------------------------
# Recursive Approach

def binary_search_rec(arr, x, high, low):
    while high >= low:

        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search_rec(arr, x, mid - 1, low)

        else:
            return binary_search_rec(arr, x, high, mid + 1)
    return -1


arr = [1, 6, 9, 10, 45, 76]
x = 45
high = len(arr) - 1
low = 0
res = binary_search_rec(arr, x, high, low)

if res == -1:
    print("Number not found")
else:
    print(f"NUMBER FOUND AT INDEX NUMBER {res} , AND NUMBER IS {arr[res]}")
