
def count_unique_and_duplicates(nums):
    hash_table = [0] * 101

    for num in nums:
        hash_table[num] += 1


    unique_count = 0
    duplicate_count = 0

    for freq in hash_table[1:]:
        if freq == 1:
            unique_count += 1

        elif freq > 1:
            duplicate_count += freq - 1


    print(unique_count, duplicate_count)
    print(hash_table)

nums = [1,4,5,4,6,7,4]
count_unique_and_duplicates(nums)


def counts_unique_and_duplicates(arr):
    dict_counting = {}
    unique_count = 0
    dup_count = 0

    for i in arr:
        if i in dict_counting:
            dict_counting[i]+=1
        else:
            dict_counting[i] = 1
    for value in dict_counting.values():
        if value == 1:
            unique_count+=1
        else:
            dup_count+=1
    print(dict_counting)

arr = [1,2,3,4,1,3]
counts_unique_and_duplicates(arr)