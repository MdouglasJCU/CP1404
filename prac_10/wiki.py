import wikipedia


def main():
    wikipedia_page = input("Enter a page title or search phrase")

    while wikipedia_page != "":
        try:
            page_title = wikipedia.page(wikipedia_page)
            print(page_title.title)
            print(wikipedia.summary(wikipedia_page))
            print(page_title.url)
            wikipedia_page = input("Enter a page title or search phrase")
        # Monty didn't work for me, so used Mercury as the example.
        # Looks like I've done it right though..
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            wikipedia_page = input("Enter a page title or search phrase")


main()
