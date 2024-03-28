# You are given a list with integers as elements. Your task is to create a new list where each element has been incremented by the value x.
# You may assume that the list contains at most 100 integers and that each integer is in the range 1 \dots 10^9.
# In a file listadd.py, implement a function create that returns the new list.


def create(t, x):
    res = []
    for num in t:
        res.append(num+x)
    return res

if __name__ == "__main__":
    print(create([1,2,3],1)) # [2,3,4]
    print(create([1,1,1,1,1],4)) # [5,5,5,5,5]
    print(create([0],10**9)) # [1000000000]
