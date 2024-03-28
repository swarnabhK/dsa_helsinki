#where we are given a list of numbers, and the goal is to find the largest difference #between any two numbers


# Algorithm 1 : Run a double loop to find the difference of each number with the other
# O(N**2)

def max_diff1(numbers):
  max_diff = 0
  for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
      max_diff = max(max_diff,abs(numbers[i]-numbers[j]))
  return max_diff


print(max_diff1([3, 2, 6, 5, 8, 5]))

#Algoritm 2: Sort the list. The max diff is the max value(end of list)-min value(start of list)
# O(NlogN)
def max_diff2(numbers):
  numbers.sort()
  return numbers[-1]-numbers[0] 

print(max_diff2([3, 2, 6, 5, 8, 5]))

#Algoritm 3: The max diff is the max value in list-min value in list
# O(N) Most optimal solution

def max_diff3(numbers):
  return max(numbers) - min(numbers)

print(max_diff3([3, 2, 6, 5, 8, 5]))
