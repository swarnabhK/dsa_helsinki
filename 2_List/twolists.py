# You are given two lists A and B both containing the numbers 1 \dots n in some order. Your task is to count how many of the numbers 1 \dots n occur earlier on the list A than on the list B. 
# In this task, n can be large and an efficient algorithm is required. The time complexity should be O(n).
# In a file twolists.py, implement a function count that returns the desired count


#solution, add the indices of the first list in a dictionary. Iterate through the other list and check if the current element index in dictionary is less than the current element index of the list, if yes increment the count.

def count(a, b):
    indices = {}
    res = 0
    for idx,val in enumerate(a):
        indices[val] = idx
    for i in range(len(b)):
        if indices[b[i]]<i:
            res+=1
    return res
if __name__ == "__main__":
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([1,2,3,4], [1,2,3,4])) # 0
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5
