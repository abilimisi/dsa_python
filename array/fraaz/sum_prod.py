def sum_and_product(arr):
    sum = 0
    prod = 1
    for i in arr:
        sum+=i
        prod*=i
    return sum,prod

arr = [1, 2, 3, 4]
print(sum_and_product(arr))