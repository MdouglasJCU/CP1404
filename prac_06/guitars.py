from guitar import guitar

def main():
    print("My guitars!")

    name = input("Enter your guitars name: ")

    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))

main()