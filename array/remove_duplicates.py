# time complexity 0(n)
# space complaxity 0(n)

#first one is recommended
def remove_duplicates(elements):
    seen = set()
    idx = 0

    for num in elements:
        if num not in seen:
            seen.add(num)
            idx+=1
    return seen,idx


arr = [1, 3, 3, 4, 5, 7, 7]
res = remove_duplicates(arr)
print(res)

# time complexity 0(n)
# space complaxity 0(1)

# arr1 = [1, 3, 3, 4, 5, 7, 7,3]
# for i in arr1:
#     if arr1.count(i) > 1:
#         arr1.remove(i)
# print(arr1)
