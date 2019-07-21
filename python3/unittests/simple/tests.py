import unittest
from unittest import TestCase

from code import add_numbers, sub_numbers


class AddNumbersTest(TestCase):

    def setUp(self) -> None:
        print("I run at the beginning of every test for this AddNumbersTest class!")

    def testSimple(self):
        self.assertEqual(add_numbers(1, 2), 3)

    def testLessSimple(self):
        self.assertEqual(add_numbers(1, add_numbers(2, 3)), 6)


class SubtractNumbersTest(TestCase):
    def testSimple(self):
        self.assertEqual(sub_numbers(3, 2), 1)


if __name__ == '__main__':
    test_suite = unittest.TestSuite()

    # Add test suites
    test_suite.addTest(AddNumbersTest)
    test_suite.addTest(SubtractNumbersTest)

    runner = unittest.TextTestResult()

    runner.run(test_suite)
