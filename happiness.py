# Input the values
n, m = map(int, input().split())
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# Initialize happiness
happiness = 0

# Calculate happiness
for number in array:
    if number in A:
        happiness += 1
    elif number in B:
        happiness -= 1

# Output the final happiness
print(happiness)
