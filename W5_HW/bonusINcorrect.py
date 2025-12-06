# --- Incorrect LLM solution: demonstrates the bug (double-counts items in a bonus set) ---

def knapsack_with_bonuses(weights, values, W, bonuses):
    """
    Buggy behavior: After building a base table, it applies each bonus set on top of
    existing results without checking overlap. This can count an item twice:
    once from the base result and again inside the bonus bundle.
    """
    n = len(weights)

    # Base table for "normal" knapsack (standard template)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # --- BUG HERE: "bonus as a bundle" is layered on top of dp[n][...] which may already
    # include some of the same items in the bundle. That overlap causes double-counting.
    for items, bonus in bonuses:  # items are 1-based indices (per the LLM code)
        total_weight = sum(weights[i - 1] for i in items)
        total_value  = sum(values[i - 1] for i in items) + bonus
        for w in range(W, total_weight - 1, -1):
            # If dp[n][w - total_weight] already includes one of the "items",
            # we add them again via total_value, inflating the answer.
            dp[n][w] = max(dp[n][w], dp[n][w - total_weight] + total_value)

    return dp[n][W]


# --- Minimal failing test (run this file directly) ---
if __name__ == "__main__":
    # Case: picking items (0 and 1) gives 6 + 4 = 10; bonus +5 → should be 15
    # Capacity W=4, weights 2 and 1 fit together (total 3)
    W = 4
    weights = [2, 1]
    values  = [6, 4]
    bonuses = [([1, 2], 5)]  # 1-based indices

    result   = knapsack_with_bonuses(weights, values, W, bonuses)
    expected = 15

    print("[INCORRECT DEMO]")
    print("Result:  ", result)     # Typically prints 19 (wrong)
    print("Expected:", expected)   # Correct answer is 15