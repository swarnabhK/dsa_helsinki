# You are given the price of a stock for 
# n days. Your task is figure out the highest profit you could have made if you had bought the stock on one day and sold it on another day.


#Alogrithm 1: Naive approach, O(N^2)
def best_profit1(prices):
  max_profit = 0
  for i in range(len(prices)):
    for j in range(i+1,len(prices)):
      max_profit = max(max_profit,prices[j]-prices[i])
  return max_profit


print(best_profit1([3,7,5,1,4,6,2,3]))


# Algorithm 2: two pointer approach. We start from idx 0 and 1, and if the diff is positive
# we know it's a profit, we keep track of the profit, we keep the left pointer in place and check the next element. If there's no profit we change left to right, because there's a chance of getting a larger profit from this point. 


def best_profit2(prices):
  max_profit = 0
  left,right = 0,1
  while(right<len(prices)):
    diff = prices[right]-prices[left]
    if diff>0:
      max_profit = max(max_profit,diff)
    else:
      left = right
    right+=1
  return max_profit

print(best_profit2([3,7,5,1,4,6,2,3]))