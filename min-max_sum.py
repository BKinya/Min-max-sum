arr = list(map(int, input().rstrip().split()))
k = 4

num_sum = sum(arr[i] for i in range(len(arr)))# sum of all integers
result = sum(arr[i] for i in range(4))#sum of the first 4 elements
sum_list = [] # list to store sum of all possible combinations of 4 integers

for i in range(0, k):
     current = result, num_sum - arr[i]
     sum_list.extend(current)
print(str(min(sum_list)) + " " +str(max(sum_list)) )
     
