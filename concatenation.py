import numpy as np

def main():
    N,M,P = map(int, input().split())
    
    first_array = []
    second_array = []
    
    for _ in range(N):
        row = list(map(int, input().split()))
        first_array.append(row)
    
    for _ in range(M):
        row = list(map(int, input().split()))
        second_array.append(row)
        
    first_array = np.array(first_array)
    second_array = np.array(second_array)
    
    concatenation = np.concatenate((first_array,second_array),axis = 0 )
    
    print(concatenation)
    
if __name__ == "__main__":
    main()
