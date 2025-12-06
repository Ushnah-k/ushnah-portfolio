# --- Corrected version: avoids double-counting by evaluating the chosen set directly ---
# Strategy: Enumerate all item subsets (fine for homework-size inputs). For each subset,
# compute its weight and base value; if it fits, add bonuses ONLY if the entire bonus set
# is contained in THIS subset. No layering on partial results → no double-counting.

def knapsack_with_bonuses_correct(weights, values, W, bonuses):
    """
    Correct reference solution for knapsack-with-bonuses.

    Key fix compared to the buggy version:
    - We compute the value of a candidate set of items directly (not on top of a
      previous state that might already include some of those items).
    - We add a bonus only when the whole bonus set is present in THIS set.
    - This guarantees each item (and each bonus) is counted exactly once.
    """
    n = len(weights)
    best = 0

    # Convert 1-based indices in bonuses to 0-based for easier checks
    norm_bonuses = []
    for items, bonus in bonuses:
        norm_bonuses.append(([i - 1 for i in items], bonus))

    # Try every subset (0..(1<<n)-1)
    for mask in range(1 << n):
        total_w = 0
        total_v = 0
        taken = []

        for i in range(n):
            if mask & (1 << i):
                total_w += weights[i]
                total_v += values[i]
                taken.append(i)

        if total_w > W:
            continue  # doesn't fit

        # Add bonuses whose entire set is included in THIS chosen subset
        taken_set = set(taken)
        bonus_sum = 0
        for items0, b in norm_bonuses:
            if all(i in taken_set for i in items0):
                bonus_sum += b

        best = max(best, total_v + bonus_sum)

    return best


# --- Verification test (run this file directly) ---
if __name__ == "__main__":
    W = 4
    weights = [2, 1]
    values  = [6, 4]
    bonuses = [([1, 2], 5)]  # 1-based indices

    result   = knapsack_with_bonuses_correct(weights, values, W, bonuses)
    expected = 15

    print("[FIXED DEMO]")
    print("Result:  ", result)     # Should print 15 (correct)
    print("Expected:", expected)