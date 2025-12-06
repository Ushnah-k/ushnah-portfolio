# Ushnah Khan
# CS 2104 - Week 3: Python First Steps

# During the preparation of this assignment, Ushnah used chatGPT
# in the leap_year function to help with the setup for code. 
# After using this tool, I/we reviewed and edited the content as needed to ensure its 
# accuracy and take full responsibility for the content in relation to grading.

def leap_year(year: int) -> bool:
    """
    Determines if a given year is a leap year.
    Returns True if leap year, False otherwise.
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
import unittest

class TestLeapYear(unittest.TestCase):
    def test_leap_year_flowchart_paths(self):
     
        # Case 1: Divisible by 400 → Leap year
        self.assertTrue(leap_year(2000))
        
        # Case 2: Not divisible by 4 → Not a leap year
        self.assertFalse(leap_year(2001))

        # Case 3: Divisible by 4 but NOT by 100 → Leap year
        self.assertTrue(leap_year(2004))

        # Case 4: Divisible by 100 but NOT by 400 → Not a leap year
        self.assertFalse(leap_year(2100))

if __name__ == "__main__":
    unittest.main()
