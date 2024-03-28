# A gummy candy costs a euros and a chocolate candy costs b euros. What is the maximum number of candies you can buy if you have c euros?
# You may assume that a, b and c are integers in the range 1 - 100.

def count(a, b, c):
    if c<a and c<b:
        return 0
    min_val,candies = min(a,b),0
    while(c>=min_val):
        c-=min_val
        candies+=1
    return candies
        
if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4
