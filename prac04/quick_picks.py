import random
quick_picks = int(input("How many quick picks? "))

for x in range(quick_picks):
    random_numbers = []
    for y in range(6):
        number = random.randint(1, 45)
        while number in random_numbers:
            number = random.randint(1, 45)
        random_numbers.append(number)
    random_numbers.sort()
    print(" ".join("{:2}".format(number) for number in random_numbers))