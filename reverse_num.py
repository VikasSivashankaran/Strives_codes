def numb(num):
    
    left = 0
    right = len(num)-1
    while (left<right):
        temp = num[left]
        num[left]=num[right]
        num[right]=temp
        left+=1
        right-=1
    return " ".join(map(str, num)) 
num = [1,4,3,2]
print(numb(num))