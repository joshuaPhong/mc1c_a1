# TODO: ERROR HANDLING. WHAT IF THE INCORRECT VALUE IS INPUT
# test float where int
# test string, "5" or "200"
# TODO: EDGE TEST. TEST ZERO CASES
# TODO: CORNER CASES. TEST VERY LARGE NUMBERS
# TODO: BOUNDARY TEST. CASES JUST ABOVE AND BELOW
# TODO: TEST NEGATIVE NUMBERS



import unittest
from black_friday import BlackFriday


class TestBlackFriday(unittest.TestCase):
    """
    A test class for testing our Black Friday class.

    """
    def test_one_apply_discount(self):
        """
        Test discount is applied when the minimum conditions are met.

        :return: True if equal, else False
        """
        cart_items = 5
        cart_total = 200.00
        test_instance = BlackFriday()

        self.assertEqual(test_instance.apply_discount(cart_items,
                                                      cart_total), 150,
                         "Test failed; values not equal")

    def test_two_apply_discount(self):
        """
        Test discount is applied when the conditions are exceeded.

        :return: True if equal, else False
        """
        cart_items = 50
        cart_total = 2000.01
        test_instance = BlackFriday()

        self.assertEqual(test_instance.apply_discount(cart_items,
                                                      cart_total), 1950.01,
                         "Test failed; values not equal")

    def test_three_apply_discount(self):
        """
        Test discount is not applied when neither condition is met.

        :return: True if equal, else False
        """
        cart_items = 1
        cart_total = 20.00
        test_instance = BlackFriday()

        self.assertEqual(test_instance.apply_discount(cart_items,
                                                      cart_total), 20,
                         "Test failed; values not equal")

    def test_four_apply_discount(self):
        """
        Test one condition True; cart_items
        Test discount is not applied when the cart has five items
        and the cart total is less than 200.0.

        :return: True if equal, else False
        """
        cart_items = 5
        cart_total = 199.00
        test_instance = BlackFriday()

        self.assertEqual(test_instance.apply_discount(cart_items,
                                                      cart_total), 199,
                         "Test failed; values not equal")

    def test_five_apply_discount(self):
        """
        Test one condition True; cart_total
        Test discount is not applied when the cart has less than five items
        and the cart total is equal to 200.0

        :return: True if equal, else False
        """
        cart_items = 4
        cart_total = 200.00
        test_instance = BlackFriday()

        self.assertEqual(test_instance.apply_discount(cart_items,
                                                      cart_total), 200,
                         "Test failed; values not equal")


if __name__ == '__main__':
    unittest.main()
