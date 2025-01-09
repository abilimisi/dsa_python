def sm_larg_num(num):
    num_str = str(num)

    smallest = float('inf')
    largest = float('-inf')

    for k in num_str:
            digit = int(k)
            if digit > largest:
                largest = digit
            elif digit < smallest:
                smallest = digit

    return smallest, largest

num = 67190
res = sm_larg_num(num)
print(res)
