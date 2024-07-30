n = int(input("Enter the number"))
result = []

for i in range (1,n+1):
    result.append(i)
print( "".join(map(str,result)))
