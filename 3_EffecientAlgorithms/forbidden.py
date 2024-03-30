# Your task is to count how many substrings of a string do not contain the character a.
# The time complexity of the algorithm should be O(n).

# O(N) solution. Can be simiplified into finding the no of subarrays not containing 'a' using sliding window.

from collections import defaultdict
def count(s):
    left,res = 0,0
    freq = defaultdict(int)
    for right in range(len(s)):
      freq[s[right]]+=1
      #while loop to make the sliding window valid
      while('a' in freq):
          freq[s[left]]-=1
          if freq[s[left]]==0:
              del freq[s[left]]
          left+=1
      res+= right-left+1  #no of valid subarrays ending at index right
    return res

if __name__ == "__main__":
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1
    print(count("aybabtu")) # 9

