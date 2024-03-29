# You are given a bit string consisting of the characters 0 and 1. How many ways can you select two positions in the bit string so that the left position contains the bit 0 and the right position contains the bit 1?


#O(N^2) naive algorithm. Count all the ones to the left of every 0
def count_ways(bits):
  total = 0
  for i in range(len(bits)):
    if bits[i]!=0:
      continue
    for j in range(i+1,len(bits)):
      if bits[j]==1:
        total+=1
  return total


print(count_ways([0,1,0,0,1,0,1,1]))

#O(2N) algorithm, first count the total no of ones in one pass, in the second pass keep a track of the current number of ones. the no of pairs will be = total_ones-no of ones encountered till now

def count_ways2(bits):
  curr_ones,count = 0,0
  total_ones = sum(1 for bit in bits if bit==1)
  for bit in bits:
    if bit==0:
      count+=total_ones-curr_ones
    else:
      curr_ones+=1
  return count


print(count_ways2([0,1,0,0,1,0,1,1]))