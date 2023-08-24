# SOURCES:
# https://realpython.com/documenting-python-code/
# https://stackoverflow.com/questions/41052221/what-is-the-difference-between-var-cvar-and-ivar-in-pythons-sphinx
# https://www.jetbrains.com/help/pycharm/documenting-source-code.html
# https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#info-field-lists
# https://chat.openai.com/ ? i want to change the exception type as I am going
# to remove debug mode: It was at this time a blanket Exception as err
# ValueError Exception: The exception type is changed to ValueError,
# which is more appropriate for handling conversion issues.
# for the read me I looked at markdown https://commonmark.org/help/
# https://www.geeksforgeeks.org/python-oops-concepts/


class BlackFriday:
    """
    A class for XClouds black friday sale.
    :cvar _black_friday_discount: The discount applied if the conditions are
    met. A private variable, for Black Friday use only.
    :type _black_friday_discount: float

    Methods:
        apply_discount(): Applies a discount if discount conditions are met

    Example:
        Apply a discount:
            discount = apply_discount(cart_items: int, cart_total: float)

        Import module: import black_friday
        Create an instance: discount_instance = black_friday.BlackFriday()
        Use the function: discount_instance.apply_discount(5, 200.0)
    """
    _black_friday_discount = 50.0

    def __init__(self):
        """
        Initialize the Black Friday instance when called.
        """

    def apply_discount(self, cart_items: int | float, cart_total: float):
        """
        Apply the black friday discount if:
        cart_items >= 5 AND cart_total >= 200.
        :param cart_items: The total number of items in a customer's cart.
        :type cart_items: int | float
        :param cart_total: The total value of the customer's cart items.
        :type cart_total: float

        :return: Cart_total - discount; If discount is applied, otherwise
        cart_total
        :rtype: float
        :raises ValueError: for inputting incorrect types

        Example:
        Apply a discount:
            discount = apply_discount(cart_items: int, cart_total: float)
            discount = apply_discount(5, 200.0)
        """
        try:
            # Parameters are cast to handle strings. Error handling.
            if float(cart_items) >= 5 and float(cart_total) >= 200.0:
                return float(cart_total) - self._black_friday_discount
            else:
                return cart_total
        except ValueError:
            return (f"You have entered an incorrect value, please enter cart "
                    f"items: int, cart total: float")
