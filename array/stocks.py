def stock_buy_sell(arr):
    minimal = arr[0]
    for i in range(len(arr)-1):
        if arr[i+1] > arr[i]:
            maximal = arr[i+1]

        else:
            maximal = arr[i]
            break

    print(maximal-minimal)

# arr = [100, 180, 260, 310, 40, 535, 695]
arr = [4, 2, 2, 2, 4]
stock_buy_sell(arr)
