import random
import time

def printAllSubArray0Slow(arr):
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr) - i):
            sum += arr[j + i]
            if(sum == 0): # print("Sum of 0 in subarray [",i," ... ",j + i, "]")
                pass
    return


def printAllSubArray0Fast(arr):
    sum_dict = {0:[-1]}
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum in sum_dict:
            for j in range(len(sum_dict[sum])):
                # print("Sum of 0 in subarray [",sum_dict[sum][j] + 1," ... ",i, "]")
                pass
            sum_dict[sum].append(i);
        else:
            sum_dict[sum] = [i];
    return


def createRandomArray(d_size):
    rand_array = []
    i = 0
    while(i < d_size):
        rand_array.append(random.randint(-8,8))
        i += 1
    return rand_array

rand_array = createRandomArray(1000000)

# t0 = time.clock()
# printAllSubArray0Slow(rand_array)
# print(time.clock() - t0, "Slow algo time")


t0 = time.clock()
printAllSubArray0Fast(rand_array)
print(time.clock() - t0, "Fast algo time")
