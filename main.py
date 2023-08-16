# import module
from black_friday import BlackFriday


if __name__ == '__main__':

    # create an instance
    black_friday = BlackFriday()
    # access the function
    print(black_friday.apply_discount(-1.09, 23.0))
    print(black_friday.apply_discount(1, -203.0))
    print(black_friday.apply_discount(5,199.99 ))
    print(black_friday.apply_discount(5,
                                      200000000000000000000000000000000000000000000000000.01))