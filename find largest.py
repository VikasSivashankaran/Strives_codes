arr = [56,450,87,12,85]
max=arr[0]
for i in range(1,len(arr)):
    if arr[i] > max:
        max=arr[i]
print(max)

l1=[56,450,87,12,85]
print(l1)
for i in range(0, len(l1)):
   for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            temp = l1[i]
            l1[i] = l1[j]
            l1[j] = temp
print(l1,"\n",l1[-3])
