def PairSumNArray(arr,N):
	prev = {}
	for i in range(len(arr)):
		if N - arr[i] in prev:
			print("Pair found at index ", prev[N - arr[i]], " and ", i, " (", N - arr[i], ",", arr[i] ,")")
			return
		prev[arr[i]] = i
	print("No pair found")


test = [0,1,2,3,4]
PairSumNArray(test,7)