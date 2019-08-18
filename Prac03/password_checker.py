minimum_length = 5
get_password = input("Please enter your password")

while len(get_password) < minimum_length:
    get_password = input("Please enter your password")

print("*" * len(get_password))