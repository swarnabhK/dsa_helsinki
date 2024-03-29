# You are given a list containing n integers. Your task is to count how many ways one can split the list into two parts so that both parts have the same total sum of elements.


#O(N) algo. We can track of the running left sum as we iterate through the array.
# and at each step we find the right sum which is the total sum-sum of current element.
def count_splits(numbers):
    n = len(numbers)
    result = 0
    left_sum = 0
    total_sum = sum(numbers)
    for i in range(n - 1):
        left_sum += numbers[i]
        right_sum = total_sum - left_sum
        if left_sum == right_sum:
            result += 1
    return result



print(count_splits([1,-1,1,-1,1,-1,1,-1]))
