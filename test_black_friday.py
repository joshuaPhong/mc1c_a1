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

    def test_six_apply_discount(self):
        """
        Test the edges, cart_item.
        Test discount is not applied when the cart has less than five items
        and the cart total is equal to 200.0

        :return: True if equal, else False
        """
        cart_items = 4.999999999999
        cart_total = 200.00
        test_instance = BlackFriday()

        self.assertEqual(test_instance.apply_discount(cart_items,
                                                      cart_total), 200.0,
                         "Test failed; values not equal")

    def test_seven_apply_discount(self):
        """
        Test the edge. cart_total.
        Test discount is not applied when cart has five items and cart_total
        is less than 200.

        :return: True if equal, else False
        """
        cart_items = 4
        cart_total = 199.999999999
        test_instance = BlackFriday()

        self.assertEqual(test_instance.apply_discount(cart_items,
                                                      cart_total),
                         199.999999999,
                         "Test failed; values not equal")

    def test_eight_apply_discount(self):
        """
        Test zeros.
        Test output when parameters are 0.

        :return: True if equal, else False
        """
        cart_items = 0
        cart_total = 0
        test_instance = BlackFriday()

        self.assertEqual(test_instance.apply_discount(cart_items,
                                                      cart_total), 0,
                         "Test failed; values not equal")

    def test_nine_apply_discount(self):
        """
        Test large numbers.
        Test output when parameters are very large.

        :return: True if equal, else False
        """
        cart_items = 9** 10
        cart_total = 9 ** 100
        test_instance = BlackFriday()

        self.assertEqual(test_instance.apply_discount(cart_items,
                                                      cart_total),
                         ((9 ** 100) - 50.0),
                         "Test failed; values not equal")

    def test_ten_apply_discount(self):
        """
        Test negative numbers.
        Test output when parameters are negative.

        :return: True if equal, else False
        """
        cart_items = -5
        cart_total = -200
        test_instance = BlackFriday()

        self.assertEqual(test_instance.apply_discount(cart_items,
                                                      cart_total),
                         -200,
                         "Test failed; values not equal")

    def test_eleven_apply_discount(self):
        """
        Test strings.
        Test output when parameters are input as strings.

        :return: True if equal, else False
        """
        cart_items = "5"
        cart_total = "200"
        test_instance = BlackFriday()

        self.assertEqual(test_instance.apply_discount(cart_items,
                                                      cart_total),
                         150,
                         "Test failed; values not equal")


if __name__ == '__main__':
    unittest.main()
