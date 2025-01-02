def dup_in_k_dist(element, k):

    for i in range(len(element) - k):
        if element[i] == element[i + k]:
            return True
        else:
            False


arr = [1, 2, 3, 1, 4, 5]
k = 3
res = dup_in_k_dist(arr, k)
if res:
    print(True)
else:
    print(False)
