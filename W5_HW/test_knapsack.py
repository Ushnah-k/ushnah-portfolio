import unittest
from conflicting_llm import knapsack_with_conflicts
from bonuses_llm import knapsack_with_bonuses

class TestKnapsackFailures(unittest.TestCase):
    def test_conflicts_blocks_valid_choice(self):
        # Part A failing test
        W = 2
        weights = [2, 2]
        values  = [5, 5]
        conflicts = [(0, 1)]
        result = knapsack_with_conflicts(weights, values, conflicts, W)
        expected = 5  # should be able to take either item
        # Helpful prints for your screenshot
        print("\n[Part A] result:", result, "expected:", expected)
        self.assertEqual(result, expected, "LLM code wrongly blocks both items when only one is needed.")

    def test_bonus_applied_without_items(self):
        # Part B failing test
        W = 4
        weights = [3, 4]
        values  = [4, 5]
        bonuses = [([1, 2], 10)]  # 1-based indices as per LLM code (items 1 and 2)
        result = knapsack_with_bonuses(weights, values, W, bonuses)
        expected = 4  # only item 0 fits; bonus set (both items) is impossible
        print("\n[Part B] result:", result, "expected:", expected)
        self.assertEqual(result, expected, "LLM code seems to grant a bonus even when the set can't fit.")

if __name__ == "__main__":
    unittest.main(verbosity=2)