arr = [1, 'apple', 2, 'banana', 3, 'apple', 'orange', 2,1,1,1]

# res = list(set(arr))
# print(res)
seen=set()
res=[]

for i in arr:
    if i not in seen:
        res.append(i)
        seen.add(i)
print(res)