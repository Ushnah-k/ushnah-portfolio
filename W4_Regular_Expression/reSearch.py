import re
import unittest

def findmatch(str):
    return re.search('word:\w\w\w',str)
#print(findmatch('an example word:cat!!').group())
class TestFindMatch(unittest.TestCase):
    def test_findmatch(self):
    # Test cases for findmatch
        self.assertEqual('word:cat',findmatch('an example word:cat!!').group(), "not matched")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)