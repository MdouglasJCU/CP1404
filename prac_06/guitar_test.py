from guitar import guitar


def main():
    guitar1 = guitar("Guitar 1", 2005, 502.34)
    guitar2 = guitar("Guitar 2", 1923, 15723)
    guitar3 = guitar("Guitar 3", 1987, 250)

    print(guitar1, guitar2, guitar3)
    print("expected {}, got {}".format(2019 - guitar1.year, guitar1.get_age()))
    print("expected False.  Got {}".format(guitar1.is_vintage()))
    print("expected True.  Got {}".format(guitar2.is_vintage()))


main()