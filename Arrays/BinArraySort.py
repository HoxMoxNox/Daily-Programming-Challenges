#http://www.techiedelight.com/sort-binary-array-linear-time/

def sortBinArray(arr):
    num_of_0s = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            num_of_0s += 1
            arr[i] = 1
    arr[0:num_of_0s] = [0] * num_of_0s
    return arr



def quicksortBinArray(arr):
    pivot = 1
    previous = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            arr[i], arr[previous] = arr[previous], arr[i]
            previous += 1
    return arr





test_arr = [0,1,0,1,0,1,0,0,0,1,0,0,1]
test_2 = [1,0,1,0,1,0,0,1]
test_3 = [0]
test_4 = [1]
test_5 = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]


print(sortBinArray(test_arr))
print(sortBinArray(test_2))
print(sortBinArray(test_3))
print(sortBinArray(test_4))
print(sortBinArray(test_5))

assert(sortBinArray(test_arr)  == quicksortBinArray(test_arr))
assert(sortBinArray(test_2)  == quicksortBinArray(test_2))
assert(sortBinArray(test_3)  == quicksortBinArray(test_3))
assert(sortBinArray(test_4)  == quicksortBinArray(test_4))
assert(sortBinArray(test_5)  == quicksortBinArray(test_5))