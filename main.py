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


# import module
import black_friday


if __name__ == '__main__':

    # create an instance
    discount_instance = black_friday.BlackFriday()
    # access the function
    print(discount_instance.apply_discount("4.9", 23.0))
    print(discount_instance.apply_discount(1, -203.0))
    print(discount_instance.apply_discount(4.9, 200.0))
    print(discount_instance.apply_discount(5,
                                           200000000000000000000000000000000000000000000000000.01))