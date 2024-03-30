import heapq

def find(nums):
    # Initialize a min-heap with the given list
    heap = nums[:]
    heapq.heapify(heap)  # Convert the list into a min-heap

    # Perform the process until only one element remains in the heap
    while len(heap) > 1:
        # Extract the two smallest elements from the heap
        smallest1 = heapq.heappop(heap)
        smallest2 = heapq.heappop(heap)

        # Calculate the sum minus one
        result = smallest1 + smallest2 - 1

        # Add the result back to the heap
        heapq.heappush(heap, result)

    # Return the last remaining element in the heap
    return heap[0]


if __name__ == "__main__":
    print(find([1,2,3,4])) # 7
    print(find([1,1,1])) # 1
    print(find([5,1,1,7,9,1,2])) # 20
