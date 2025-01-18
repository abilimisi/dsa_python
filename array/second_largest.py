# O(n) Time and O(1) Space
def sec_lar(arr):
    largest = float('-inf')
    s_largest = float('-inf')

    for i in arr:
        if i > largest:
            largest = i
    for j in arr:
        if j > s_largest and j != largest:
            s_largest = j
    return largest,s_largest


arr = [12, 37, 14, 48, 23]
print(sec_lar(arr))
