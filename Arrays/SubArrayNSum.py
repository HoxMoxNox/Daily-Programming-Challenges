#http://www.techiedelight.com/find-pair-with-given-sum-array/

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