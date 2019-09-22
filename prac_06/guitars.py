from guitar import guitar


def main():
    guitars = []

    print("My guitars")

    name = input("Enter your guitars name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added.")
        name = input("Enter your guitars name: ")

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, Guitar in enumerate(guitars):
            vintage_string = ""
            if Guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1.name} ({1.year}), worth ${1.cost:5,.2f} {2}".format(i + 1, Guitar, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")


main()
