def knapsack_01(values, weights, capacity):
    n = len(values)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
        
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
            
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected_items[::-1]

values = [60, 80, 110]
weights = [20, 30, 40]
capacity = 60
max_value, selected_items = knapsack_01(values, weights, capacity)

print("Maximum value:", max_value)
print("Selected items:", selected_items)