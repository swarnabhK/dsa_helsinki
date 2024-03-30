# You are given a bit string that consists of the characters 0 and 1. How many ways can you choose two positions in the bit string so that each position has the same bit?
# The time complexity of the algorithm should be O(n).


# O(N) solution. Find the count of each bit. When we encounter a bit we see that it can pair with dict[bit]-1 other bits. Add that to the count and remove one from the dict[bit] value

from collections import defaultdict
def count(s):
    freq = defaultdict(int)
    res = 0
    for bit in s:
        freq[bit]+=1
    for bit in s:
        freq[bit]-=1  # we are subtracting one because the bit cannot pair with itself.
        res+=freq[bit]
    return res

if __name__ == "__main__":
    print(count("0101")) # 2
    print(count("000000")) # 15
    print(count("000111")) # 6
    print(count("00100001101100")) # 46
