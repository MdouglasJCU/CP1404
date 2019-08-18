minimum_length = 5


def main():
    password = get_password(minimum_length)
    asterisk_conversion(password)


def get_password(minimum_length):
    password = input("Please enter your password")
    while len(password) < minimum_length:
        password = input("Please enter your password")

    return password


def asterisk_conversion(print_asterisk):
    print("*" * len(print_asterisk))


main()