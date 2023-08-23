# sources
# gpt 23/8/23 ? I want to improve my documentation on a unit test. supplied
# current version of test one.
# response. expand description, explain test steps, change return type
# (tests have none, was true or false), add an exception, and enhance the
# error message.
# it also suggested using the given, when then model
# https://pythontest.com/strategy/given-when-then-2/
# https://softwareengineering.stackexchange.com/questions/367378/should-given
# -when-and-then-comments-be-included-in-unit-tests
# I will apply this to all the tests.
# I have chosen to implement each test separately for readability and
# modularity. Each one can be modified. And the test steps and reasons are
# clearer.


import unittest
from black_friday import BlackFriday


class TestBlackFriday(unittest.TestCase):
    """
    A test class for testing our Black Friday class.
    """

    def test_one_apply_discount(self):
        """
        Test method apply_discount(), from class BlackFriday.
        Test method is applied correctly when the minimum conditions are met.

        :return: None
        :raises AssertionError: != if the expected result does not equal
        applied test inputs.
        """
        # given test data
        cart_items = 5
        cart_total = 200.00
        expected_total = 150
        test_instance = BlackFriday()
        # when we call the apply_discount function with the test data
        apply_discount_total = test_instance.apply_discount(cart_items,
                                                            cart_total)
        # then implement test
        self.assertEqual(apply_discount_total, expected_total,
                         f"Test failed; expected {expected_total}, "
                         f"got {apply_discount_total}")

    def test_two_apply_discount(self):
        """
        Test method apply_discount(), from class BlackFriday.
        Test discount is correctly applied when method conditions are exceeded.

        :return: None
        :raises AssertionError: != if the expected result does not equal
        applied test inputs.
        """

        # given test data
        cart_items = 50
        cart_total = 2000.01
        expected_total = 1950.01
        test_instance = BlackFriday()
        # when we call the apply_discount function with the test data
        apply_discount_total = test_instance.apply_discount(cart_items,
                                                            cart_total)

        self.assertEqual(apply_discount_total, expected_total,
                         f"Test failed; expected {expected_total}, "
                         f"got {apply_discount_total}")

    def test_three_apply_discount(self):
        """
        Test method apply_discount(), from class BlackFriday.
        Test discount is not applied when neither condition is met,
        cart items < 5 and cart total < 200.

        :return: None
        :raises AssertionError: != if the expected result does not equal
        applied test inputs.
        """
        # given test data
        cart_items = 1
        cart_total = 20.00
        expected_total = 20.00
        test_instance = BlackFriday()
        # when we call the apply_discount function with the test data
        apply_discount_total = test_instance.apply_discount(cart_items,
                                                            cart_total)
        # then implement test
        self.assertEqual(apply_discount_total, expected_total,
                         f"Test failed; expected {expected_total}, "
                         f"got {apply_discount_total}")

    def test_four_apply_discount(self):
        """
        Test method apply_discount(), from class BlackFriday.
        Test when one condition is True; cart_items >= 5,
        and one condition is False; cart_total <= 200
        Test discount is not applied when the cart has five items
        and the cart total less than to 200.0.
        :return: None
        :raises AssertionError: != if the expected result does not equal
        applied test inputs.
        """
        # given test data
        cart_items = 5
        cart_total = 199.00
        expected_total = 199.00
        test_instance = BlackFriday()

        # when we call the apply_discount function with the test data
        apply_discount_total = test_instance.apply_discount(cart_items,
                                                            cart_total)
        # then implement test
        self.assertEqual(apply_discount_total, expected_total,
                         f"Test failed; expected {expected_total}, "
                         f"got {apply_discount_total}")

    def test_five_apply_discount(self):
        """
        Test method apply_discount(), from class BlackFriday.
        Test one condition True; cart_total >= 200.0,
        and one condition is False; cart_items < 5
        Test discount is not applied when the cart has less than five items
        and the cart total is equal to 200.0

        :return: None
        :raises AssertionError: != if the expected result does not equal
        applied test inputs.
        """
        # given test data
        cart_items = 4
        cart_total = 200.00
        test_instance = BlackFriday()
        expected_total = 200

        # when we call the apply_discount function with the test data
        apply_discount_total = test_instance.apply_discount(cart_items,
                                                            cart_total)
        # then implement test
        self.assertEqual(apply_discount_total, expected_total,
                         f"Test failed; expected {expected_total}, "
                         f"got {apply_discount_total}")

    def test_six_apply_discount(self):
        """
        Test method apply_discount(), from class BlackFriday.
        Test the edges, cart_item.
        Test float not int
        Test discount is not applied when the cart has less than five items
        and the cart total is equal to 200.0

        :return: None
        :raises AssertionError: != if the expected result does not equal
        applied test inputs.
        """
        # given test data
        cart_items = 4.999999999999
        cart_total = 200.00
        test_instance = BlackFriday()
        expected_total = 200.0

        # when we call the apply_discount function with the test data
        apply_discount_total = test_instance.apply_discount(cart_items,
                                                            cart_total)
        # then implement test
        self.assertEqual(apply_discount_total, expected_total,
                         f"Test failed; expected {expected_total}, "
                         f"got {apply_discount_total}")

    def test_seven_apply_discount(self):
        """
        Test method apply_discount(), from class BlackFriday.
        Test the edge, cart_total.
        Test discount is not applied when cart has five items and cart_total
        is less than 200.

        :return: None
        :raises AssertionError: != if the expected result does not equal
        applied test inputs.
        """
        # given test data
        cart_items = 4
        cart_total = 199.999999999
        test_instance = BlackFriday()
        expected_total = 199.999999999

        # when we call the apply_discount function with the test data
        apply_discount_total = test_instance.apply_discount(cart_items,
                                                            cart_total)
        # then implement test
        self.assertEqual(apply_discount_total, expected_total,
                         f"Test failed; expected {expected_total}, "
                         f"got {apply_discount_total}")

    def test_eight_apply_discount(self):
        """
        Test method apply_discount(), from class BlackFriday.
        Test zeros.
        Test discount is not applied when parameters are 0.

        :return: None
        :raises AssertionError: != if the expected result does not equal
        applied test inputs.
        """
        # given test data
        cart_items = 0
        cart_total = 0
        test_instance = BlackFriday()
        expected_total = 0

        # when we call the apply_discount function with the test data
        apply_discount_total = test_instance.apply_discount(cart_items,
                                                            cart_total)
        # then implement test
        self.assertEqual(apply_discount_total, expected_total,
                         f"Test failed; expected {expected_total}, "
                         f"got {apply_discount_total}")

    def test_nine_apply_discount(self):
        """
        Test method apply_discount(), from class BlackFriday.
        Test large numbers.
        Test discount is applied even for very large numbers.

        :return: None
        :raises AssertionError: != if the expected result does not equal
        applied test inputs.
        """
        # given test data
        cart_items = 9 ** 10
        cart_total = 9 ** 100
        test_instance = BlackFriday()
        expected_total = ((9 ** 100)-50.0)
        # when we call the apply_discount function with the test data
        apply_discount_total = test_instance.apply_discount(cart_items,
                                                            cart_total)
        # then implement test
        self.assertEqual(apply_discount_total, expected_total,
                         f"Test failed; expected {expected_total}, "
                         f"got {apply_discount_total}")

    def test_ten_apply_discount(self):
        """
        Test method apply_discount(), from class BlackFriday.
        Test negative numbers.
        Test discount is not applied when parameters are negative.

        :return: None
        :raises AssertionError: != if the expected result does not equal
        applied test inputs.
        """
        # given test data
        cart_items = -5
        cart_total = -200
        test_instance = BlackFriday()
        expected_total = -200
        # when we call the apply_discount function with the test data
        apply_discount_total = test_instance.apply_discount(cart_items,
                                                            cart_total)
        # then implement test
        self.assertEqual(apply_discount_total, expected_total,
                         f"Test failed; expected {expected_total}, "
                         f"got {apply_discount_total}")

    def test_eleven_apply_discount(self):
        """
        Test method apply_discount(), from class BlackFriday.
        Test strings.
        Test discount is applied when parameters are input as strings.

        :return: None
        :raises AssertionError: != if the expected result does not equal
        applied test inputs.
        """
        # given test data
        cart_items = "5.0"
        cart_total = "200"
        test_instance = BlackFriday()
        expected_total = 150
        # when we call the apply_discount function with the test data
        apply_discount_total = test_instance.apply_discount(cart_items,
                                                            cart_total)
        # then implement test
        self.assertEqual(apply_discount_total, expected_total,
                         f"Test failed; expected {expected_total}, "
                         f"got {apply_discount_total}")


if __name__ == '__main__':
    unittest.main()
