class BlackFriday:
    """
    A class for XClouds black friday sale.
    :ivar _black_friday_discount: The discount applied if the conditions are met.
        A private variable, for Black Friday use only.
    :type _black_friday_discount: float

    Methods:

    Example:


    """

    def __init__(self):
        """
        The constructor for BlackFriday class.
        Initializes the Black Friday instance when called.
        Has a default, private variable; _black_friday_discount: float
        """

        self._black_friday_discount = 50.0

    def apply_discount(self, cart_items, cart_total):
        """
        Apply the black friday discount if:
        cart_items >= 5 AND cart_total >= 200.
        :param cart_items: The total number of items in a customer's cart.
        :type cart_items: int
        :param cart_total: The total value of the customer's cart items.
        :type cart_total: float

        :return: Cart_total - discount; If discount is applied, otherwise
        cart_total
        :rtype: float

        Example:

        """
        try:
            if cart_items >= 5 and cart_total >= 200.0:
                return cart_total - self._black_friday_discount
            else:
                return cart_total
        except Exception as err:
            return f"You have an error: {err}"
