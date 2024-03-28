def count(t):
    # we can traverse multiple levels of nested lists by using a stack and extending the stack whenever we find a list
    stack = [t]
    flattened_list = []
    while stack:
        curr = stack.pop()
        if isinstance(curr, list):
          stack.extend(curr)
        else:
            flattened_list.append(curr)
        
    return len(flattened_list)
  

if __name__ == "__main__":
    print(count([1,2,3])) # 3
    print(count([1,[2,3],4,5,[6]])) # 6
    print(count([1,[1,[1,[1]]]])) # 4
    print(count([[1,2,[3,4]],5,[[6,[7],8]]])) # 8
