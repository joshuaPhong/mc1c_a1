class BlackFriday:
    """
    A class for XClouds black friday sale.
    :ivar _black_friday_discount: The discount applied if the conditions are
    met.
        A private variable, for Black Friday use only.
    :type _black_friday_discount: float

    Methods:
        apply_discount(): Applies a discount if discount conditions are met

    Example:
        Apply a discount:
            discount = apply_discount(cart_items: int, cart_total: float)
            discount = apply_discount(5, 200.0)
        If importing module:
        Create an instance first.
            discount_instance = BlackFriday()
        Use the function:
            discount_instance.apply_discount(5, 200.0)

    """

    def __init__(self):
        """
        Initialize the Black Friday instance when called:
        With the default private variable; _black_friday_discount: float
        """

        self._black_friday_discount = 50.0
        self.debug = True

    def apply_discount(self, cart_items, cart_total):
        """
        Apply the black friday discount if:
        cart_items >= 5 AND cart_total >= 200.
        :param cart_items: The total number of items in a customer's cart.
        This should be an integer but is of type float for error handling
        :type cart_items: float
        :param cart_total: The total value of the customer's cart items.
        :type cart_total: float

        :return: Cart_total - discount; If discount is applied, otherwise
        cart_total
        :rtype: float

        Example:
        Apply a discount:
            discount = apply_discount(cart_items: int, cart_total: float)
            discount = apply_discount(5, 200.0)

        """
        try:
            # Parameters are cast to handle strings and prevent any rounding
            # of cart_items. Error handling.
            if float(cart_items) >= 5 and float(cart_total) >= 200.0:
                return float(cart_total) - self._black_friday_discount
            else:
                return cart_total
        except Exception as err:
            if self.debug is True:
                return f"You have an error: {err}"
            else:
                return "Whoops, there has been an error. Try again"
                # then send the user back
