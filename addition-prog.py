def add_numbers(a, b):
    return a + b
def main():
    print("Welcome to the adding program. Please input two numbers you want added together.\n")
number1 = input("First number: \n")
number2 = input("Second number: \n")
sum = float(number1) +float(number2)
print("{0} + {1} = {2}".format(number1, number2, sum))
import unittest
class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(12, 18), 30)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(-4, -4), -8)
        self.assertEqual(add_numbers(-5, 5), 0)
        self.assertEqual(add_numbers(11.4, 18.6), 30)
        self.assertEqual(add_numbers(-5, 10), 5)
if __name__ == "__main__":
    main()
unittest.main(argv=[''], verbosity=2, exit=False)