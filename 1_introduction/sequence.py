# Each element in a sequence of numbers is the smallest positive integer that does not occur earlier in the sequence and that has the same digit in the beginning and in the end.
# The sequence begins as follows:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, \dots


def generate(n):
    if n<=9:
        return n
    count,number = 9,11
    
    while(count<n):
        str_number = str(number)
        if str_number[0]==str_number[-1]:
            count+=1
        number+=1
    return number-1

if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 2
    print(generate(3)) # 3
    print(generate(10)) # 11
    print(generate(123)) # 1141
