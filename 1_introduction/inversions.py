# You are given a list that consists of the numbers 1 \dots n. A pair of indices (i,j) is an inversion if i<j and the element at index i on the list is greater than the element at index j.
# You may assume that n is at most 100.


def count(numbers):
  result  = 0
  for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
      if numbers[i]>numbers[j]:
        result+=1
  return result
  

if __name__ == "__main__":
  print(count([1,3,2])) # 1
  print(count([1])) # 0
  print(count([4,3,2,1])) # 6
  print(count([1,8,2,7,3,6,4,5])) # 12
