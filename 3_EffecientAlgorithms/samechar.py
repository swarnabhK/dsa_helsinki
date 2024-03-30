# A substring is a contiguous string inside a string. For example, the substrings of the string abc are a, b, c, ab, bc and abc. Your task is to count how many substrings have the same character at all positions.
# The time complexity of the algorithm should be O(n).


# O(N): this problem can be simplified into finding the no of subarrays containing atmost one distinct character. Use sliding window.

from collections import defaultdict
def count(s):
    freq = defaultdict(int)
    res,left = 0,0
    for right in range(len(s)):
        freq[s[right]]+=1
        while(len(freq)>1):
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1
        res+= right-left+1 #no of valid subarrays ending at right is the length of the subarray.
    return res

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5
