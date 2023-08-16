# import module
from black_friday import BlackFriday


if __name__ == '__main__':

    # create an instance
    black_friday = BlackFriday()
    # access the function
    print(black_friday.apply_discount(1, 23.0))
    print(black_friday.apply_discount(1, 203.0))
    print(black_friday.apply_discount(5, 23.0))
    print(black_friday.apply_discount(5, 203.0))