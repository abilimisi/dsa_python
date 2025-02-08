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



def sec_lar_element(arr_elements):
    largest = float('-inf')
    s_largest = float('-inf')

    for i in arr_elements:
        if i > largest:
            s_largest = largest
            largest = i

        elif(i>s_largest and i != largest):
            s_largest = i
    return s_largest


arr_elements = [12, 37, 14, 48, 23]
print(sec_lar_element(arr_elements))
