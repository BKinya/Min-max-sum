arr = list(map(int, input().rstrip().split()))
k = 4

num_sum = sum(arr[i] for i in range(len(arr)))# sum of all integers
result = sum(arr[i] for i in range(4))#sum of the first 4 elements

max_sum = result
min_sum = result


for i in range(0, k):
     current =  num_sum - arr[i]# get sum of all possible combinations of 4 integers
     #get the maximum sum
     if current > max_sum:
          max_sum = current
     
     #get the minimum result
     if current < min_sum:
          min_sum = current
print( str(max_sum)+ " "+str(min_sum))
     
