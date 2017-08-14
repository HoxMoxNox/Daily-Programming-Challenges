#http://www.techiedelight.com/find-pair-with-given-sum-array/

def printAllSubArrayNFast(arr, N):
    sum_dict = {0:[-1]}
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if (sum - N) in sum_dict:
            for j in range(len(sum_dict[sum - N])):
                print("Sum of",N," in subarray [",sum_dict[sum - N][j] + 1," ... ",i, "]")
                #pass
            sum_dict[sum - N].append(i);
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

#rand_array = createRandomArray(10)

test1 = [0,1,9,0,10,32]

printAllSubArrayNFast(test1, 10)