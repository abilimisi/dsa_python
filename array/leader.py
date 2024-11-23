def leaders(arr):
    arr_size = len(arr)

    result = []

    for i in range(arr_size):
        for j in range(i + 1, arr_size): #its inner loop so it will compares that i value with all remaining right elements
            if arr[i] < arr[j]: #if it becomes true then it will breaks the loop and wont go for else part
                break
        else:
            result.append(arr[i])
    return result


arr = [16, 17, 4, 3, 2]

result = leaders(arr)
print(" ".join(map(str, result)))

# comparison of 4 with [3, 2]
# Key Observations
# For arr = [16, 17, 4, 3, 2], the process for 4 is:
#
# Compare 4 with 3: No break.
# Compare 4 with 2: No break.
# The inner loop completes fully without a break.
# The else block executes, and 4 is added to the result list.