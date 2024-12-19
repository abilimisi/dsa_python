# time complexity = O(N)   #bcz it uses min func
# space complexity = O(1)
def min_cost(a):
    return (len(a) - 1) * min(a)


a = [4, 3, 2]
print(min_cost(a))


# -------------------------------

def min_c(arr):
    arr.sort()
    total_cost = 0
    smallest = arr[0]

    for i in range(1, len(arr)):
        total_cost += smallest
    return total_cost


a = [4, 3, 2]
b = [3, 4]
print(min_cost(a))
print(min_cost(b))
