def daysInMonth(monthNum):
    monthDays = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] ##no none
    return monthDays[monthNum] ## monthNum -1

import unittest

class DaysInMonthTester(unittest.TestCase):
    def testJanuary(self):
        self.assertEquals(31, daysInMonth(1))
    def testFebruary(self):
        self.assertEquals(28, daysInMonth(2))
    def testDecember(self):
        self.assertEquals(31, daysInMonth(12))


if __name__ == '__main__':
    unittest.main()