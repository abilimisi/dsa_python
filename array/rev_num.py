def rev_num(num):
    rev = 0
    while num != 0:
        mod = num % 10

        rev = rev*10 + mod

        num//=10
    return rev

num = 4532
print(rev_num(num))