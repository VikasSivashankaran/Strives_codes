arr = [56,45,12,85,81]
max=arr[0]
for i in range(len(arr)-1):
    if arr[i] > max:
        max=arr[i]
print(max)