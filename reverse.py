def reverse(val):
    stack=[]
    for i in val:
        stack.append(i)
    i = 0
    while stack:
        val[i]=stack.pop()
        i=i+1
    return val



if __name__=="__main__":
    val = input().split()
    print(reverse(val))