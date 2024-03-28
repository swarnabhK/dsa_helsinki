def create(n):
    if n <= 1:
        return [1] if n == 1 else []  # Return [1] if n is 1, otherwise return an empty list

    # Initialize the list of players with numbers from 1 to n
    players = list(range(1, n + 1))
    order = []  # Initialize the list to store the order of players leaving
    index = 1  # Start from the second player (player 2)

    while players:  # Continue until there are no players left
        order.append(players[index])  # Add the current player to the order list
        players.pop(index)  # Remove the current player from the circle

        if players:  # Check if there are still players left in the circle
            index = (index + 1) % len(players)  # Move to the next player in a circular manner

    return order

# Example usage:
n = 7
print(create(n))  # Output: [2, 4, 6, 1, 5, 3, 7]
