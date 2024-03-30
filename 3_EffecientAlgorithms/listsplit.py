# You are given a list containing n integers. Your task is to count, how many ways you can split the list into two parts so that both parts have the same smallest element.
# The time complexity of the algorithm should be O(n).


def count(t):
    min_idx_map = {}
    curr_min = t[0]
    left,right = 0,len(t)-1
    res = 0
    for i in range(len(t)):
        curr_min = min(curr_min,t[i])
        min_idx_map[i] = curr_min
    for i in range(right):
        left_min = min(min_idx_map[left],min_idx_map[i])
        right_min = min(min_idx_map[i+1],min_idx_map[right])
        if left_min==right_min:
            res+=1
    return res
if __name__ == "__main__":
    print(count([2,1,1,3])) # 1
    print(count([1,1,1,1])) # 3
    print(count([1,2,3,1,2,3])) # 3
    print(count([1,2,3,4,3,2,1])) # 6
    print(count([4,3,2,1,2,3,4])) # 0
