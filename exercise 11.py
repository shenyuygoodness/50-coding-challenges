arr= [6,9,2,5,1]
sum = 0
average = 0
for i in range(0, len(arr)):
	sum = sum + arr[i]
average = sum/ len(arr)
print(average)