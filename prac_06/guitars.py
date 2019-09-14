from guitar import guitar

def main():
    guitars = []

    print("My guitars!")

    name = input("Enter your guitars name: ")

    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        add_guitar = guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added.")
        name = input("Enter your guitars name: ")


main()
