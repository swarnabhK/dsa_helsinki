def count(s):
    # Initialize frequency counters for characters "t", "i", "r", and "a"
    freq = {'t': 0, 'i': 0, 'r': 0, 'a': 0}
    count = 0  # Initialize count of valid substrings
    left = 0  # Initialize left pointer of the sliding window

    # Iterate through the string with a sliding window
    for right in range(len(s)):
        # Update frequency count for the character at the right pointer
        if s[right] in freq:
            freq[s[right]] += 1

        # Shrink the window from the left side if the current window contains all required characters
        while all(freq[char] > 0 for char in freq):
            # Increment count by the size of the valid substring
            count += len(s) - right

            # Update frequency count for the character at the left pointer
            if s[left] in freq:
                freq[s[left]] -= 1

            # Move the left pointer to shrink the window
            left += 1

    return count

if __name__ == "__main__":
    print(count("aybabtu")) # 0
    print(count("tira")) # 1
    print(count("ritari")) # 6
    print(count("tiratiratira")) # 45
    print(count("xaxrxixtx")) # 4
