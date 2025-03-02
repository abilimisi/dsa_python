def generate_subarrays(arr):
    z = []

    for start in range(len(arr)):
        for end in range(start, len(arr)):
            z.append(arr[start:end + 1])

    print(z)

    sums = sum([sum(num) for num in z])

    print(sums)

arr = [1,2,3]
generate_subarrays(arr)


def generate_subarrays(arr):
    z = []
    sums = 0

    for start in range(len(arr)):
        for end in range(start, len(arr)):
            z.append(arr[start:end + 1])

    for num1 in z:
        for num2 in num1:
            sums+=num2
    print(sums)

arr = [1,2,3,4,5]
generate_subarrays(arr)
