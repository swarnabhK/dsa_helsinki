def create(n, k):
    # Initialize the list with numbers from 1 to n
    result = list(range(1, n + 1))
    start = (n-1)
    if k>n:
         return result
    # Perform swaps to create k inversions
    for _ in range(k):
          result[start],result[start-1] = result[start-1],result[start]
          start-=1
    return result

if __name__ == "__main__":
    print(create(3, 0)) # [1,2,3]
    print(create(3, 1)) # esim. [1,3,2]
    print(create(3, 2)) # esim. [3,1,2]
    print(create(10, 34))
