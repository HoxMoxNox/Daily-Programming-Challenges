

#linear sort to put evens first
def quicksortBinArray(arr):
    pivot = 1
    previous = 0
    for i in range(len(arr)):
        if arr[i] % 2  != 1:
            arr[i], arr[previous] = arr[previous], arr[i]
            previous += 1
    return arr


test1 = [2,3,3,3,3,3,4]
test2 = [1]
test3 = [2]
test4 = [1,2,3,4,5,6,7,8,9]
test5 = [4,4,4]
test6 = [3,3,3]
test7 = [5,6,7,3,4,2,6,8,5,7,1,10,11,100,123]



