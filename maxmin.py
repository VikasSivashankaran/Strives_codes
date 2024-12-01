def min(input):
    min = ('inf')
    for i in input:
        if i < min:
            min = i
    return min

def max(input):
    max = ('-inf')
    for i in input:
        if i >max:
            max =i
    return max




if __name__ == "__main__":
    input = list(input().split())
    print("Maximum",max(input))
    print("Minimum",min(input))