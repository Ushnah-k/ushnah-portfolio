from bonuses_llm import knapsack_with_bonuses

# Example where the buggy LLM code gives the wrong answer
W = 4
weights = [2, 1]
values  = [6, 4]
bonuses = [([1, 2], 5)]  # 1-based indices, as in the LLM code

result = knapsack_with_bonuses(weights, values, W, bonuses)
expected = 15

print("Result:", result)
print("Expected:", expected)