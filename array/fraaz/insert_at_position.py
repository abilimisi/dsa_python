def insert_at_position(arr, pos, val):
    n = len(arr)

    # Step 1: Create a new list with one extra space
    new_arr = [0] * (n + 1)

    # Step 2: Copy elements up to the position
    for i in range(pos):
        new_arr[i] = arr[i]

    # Step 3: Insert the new value at the position
    new_arr[pos] = val

    # Step 4: Copy the remaining elements
    for i in range(pos, n):
        new_arr[i + 1] = arr[i]

    # Step 5: Print the result
    print(new_arr)


# Test the function
arr = [3, 7, 11, 2, 1, 10]
pos = 3
val = 9
insert_at_position(arr, pos, val)
