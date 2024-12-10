

def rotate(arr,n):
    n=len(arr)
    i=0
    j=n-1
    while i!=j:
        arr[i],arr[j]=arr[j],arr[i]
        i=i+1
    pass
arr = [1,2,3]
n=len(arr)
rotate(arr,n) 
for i in range(0,n):
    print(arr[i],end='')

