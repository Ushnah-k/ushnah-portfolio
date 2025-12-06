
"""def find_repeated_letters(input_string):
    repeated_letters = []
    for i in range(len(input_string)):
        if input_string[i] in input_string[:i] and input_string[i] not in repeated_letters:
            repeated_letters.append(input_string[i])
    return repeated_letters
# Example usage
input_string = "programming"
print(find_repeated_letters(input_string))
# Output will be
#['r', 'm', 'g'
"""
def find_repeated_letters(input_string):
    repeated_letters = []
    for i, char in enumerate(input_string): #instead of running three times
        if char in input_string[:i] and char not in repeated_letters:
            repeated_letters.append(char)
    return repeated_letters


# Example usage
input_string = "programming mississipi"
print(find_repeated_letters(input_string))
# Expected: ['r', 'm', 'g', 's', 'i']


import unittest
class TestFindRepeatedLetters(unittest.TestCase):
    def test_no_repeats(self):
        self.assertEqual(find_repeated_letters("abc"), [])

    def test_simple_repeats(self):
        self.assertEqual(find_repeated_letters("programming"), ['r', 'm', 'g'])

    def test_multiple_repeats(self):
        self.assertEqual(find_repeated_letters("mississipi"), ['s', 'i'])

    def test_with_spaces(self):
        self.assertEqual(find_repeated_letters("hello world"), ['l', 'o'])

    def test_empty_string(self):
        self.assertEqual(find_repeated_letters(""), [])

if __name__ == "__main__":
    unittest.main()

#Notes
#go to regex 101 to test python