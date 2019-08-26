colours = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "azure1": "#f0ffff", "beirge": "#f5f5dc", "black": "#000000", "brown": "#a52a2a", "burlywood": "deb887", "CadetBlue": "#5f9ea0", "coral": "#ff7f50", "DarkGreen": "#006400"}

get_colour = input("Please choose a colour: ")
false_input = False

while not false_input:
    if get_colour in colours:
        print("The hexadecimal colour of {} is {}".format(get_colour, colours[get_colour]))
        get_colour = input("Please choose a colour: ")
    elif get_colour == "":
        print("Thanks for choosing colours")
        false_input = True
    else:
        get_colour = input("Please choose a colour: ")
