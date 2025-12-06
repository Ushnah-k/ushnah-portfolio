# --- Buggy LLM code (unchanged) ---
def knapsack_with_bonuses(weights, values, W, bonuses):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    # Apply bonuses (buggy double-counting)
    for items, bonus in bonuses:
        total_weight = sum(weights[i - 1] for i in items)
        total_value  = sum(values[i - 1] for i in items) + bonus
        for w in range(W, total_weight - 1, -1):
            dp[n][w] = max(dp[n][w], dp[n][w - total_weight] + total_value)
    return dp[n][W]

# --- Failing test (no imports; same file) ---
if __name__ == "__main__":
    W = 4
    weights = [2, 1]
    values  = [6, 4]
    bonuses = [([1, 2], 5)]  # 1-based indices

    result = knapsack_with_bonuses(weights, values, W, bonuses)
    expected = 15
    print("Result:", result)
    print("Expected:", expected)