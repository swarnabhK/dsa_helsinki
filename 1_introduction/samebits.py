# You are given a string where each character is a bit (0 or 1). Your task is to change the string so that every bit is the same. What is the smallest number of changes needed?
# You may assume that the string contains at most 100 characters.
from collections import defaultdict
def count(s):
    #the smallest no of changes needed will be to flip the bit with less count
    dict = defaultdict(int)
    for c in s:
      dict[c]+=1
    return min(dict['1'],dict['0'])

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4
