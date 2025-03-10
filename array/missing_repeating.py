
def findTwoElement(arr):
    n = len(arr)
    freq = [0] * (n + 1)
    repeating = -1
    missing = -1

    for i in range(n):
        freq[arr[i]] += 1

    for j in range(1,n+1):
        if freq[j] == 0:
            missing = j

        elif freq[j] == 2:
            repeating = j

    return [repeating, missing]

arr = [3, 1, 3]
ans = findTwoElement(arr)
print(ans)