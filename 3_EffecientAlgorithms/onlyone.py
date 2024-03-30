# You are given a list consisting of n integers. n-1 of the integers are equal and one has a different value. Your task is to determine what the different integer is.
# The time complexity of the algorithm should be O(n). You may assume that n>2.

#O(N), compare the adjacent two numbers, for the only one different number it won't be equal to either of it's adjacent numbers.
# O(2N), if we solve using frequency 
def find(t):
    #Corner cases, the different number is the first number or the last number
    if(t[0]!=t[1] and t[0]!=t[2]):
        return t[0]
    if(t[-1]!=t[-2] and t[-1]!=t[-3]):
        return t[-1]
    for i in range(len(t)):
        if t[i]!=t[i-1] and t[i]!=t[i+1]:
            return t[i]

if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5
