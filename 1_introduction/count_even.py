# how many of the numbers are even
def count_even(numbers):
  result = 0
  for num in numbers:
    if num%2==0:
      result+=1
  return result


print(count_even([1, 2, 3])) # 1
print(count_even([2, 2, 2, 2, 2])) # 5
print(count_even([5, 4, 1, 7, 9, 6])) # 2

