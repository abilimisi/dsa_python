def sum_of_dig(num):


    while num >= 10:
        sum = 0
        for i in str(num):
            sum+=int(i)
        num = sum
    return sum

num = 789
res = sum_of_dig(num)
print(res)