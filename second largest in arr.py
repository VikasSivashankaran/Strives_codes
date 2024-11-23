def getSecondLargest(arr):
    max1 = float('-inf')
    max2 = float('-inf')
    for i in arr:
        if i>max1:
            max1=i
                
    for i in arr:
        if i>max2 and i != max1:
            max2=i
    return max2 if max2 != float('-inf') else -1

arr = [4,5,8,1,2,78,44,54]
print(getSecondLargest(arr))