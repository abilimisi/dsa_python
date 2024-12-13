# def generate_subarrays(arr):
#     # Outer loop: Select the starting index of the subarray
#     for start in range(len(arr)):
#         # Inner loop: Select the ending index of the subarray
#         for end in range(start, len(arr)):
#             print(arr[start:end + 1])
#
# arr = [1, 2, 3]
# generate_subarrays(arr)


#through recursive approuch

def generate_subarrays(arr, start=0, end=0):
    # Base condition: If the starting index reaches the array's length, stop recursion
    if start == len(arr):
        return

    # If the end index reaches the array's length, move the start index forward
    elif end == len(arr):
        generate_subarrays(arr, start + 1, start + 1)
    else:
        # Print the current subarray
        print(arr[start:end + 1])
        # Move the end index forward
        generate_subarrays(arr, start, end + 1)


# Example usage:
arr = [1, 2, 3]
generate_subarrays(arr)

# its just a basic(not about currenr problem)
# arr = [1,2,3,4,5]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         for k in range(i,j+1):
#             print(arr[k],end=" ")
#         print(" ")



