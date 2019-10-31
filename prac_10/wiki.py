import wikipedia


def main():
    wikipedia_page = input("Enter a page title or seacrh phrase")

    while wikipedia_page != "":
        print(wikipedia.summary(wikipedia_page))
        wikipedia_page = input("Enter a page title or seacrh phrase")


main()
