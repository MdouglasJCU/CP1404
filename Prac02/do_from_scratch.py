#program 1
"""
out_file = open('name.txt', 'w')
user_name = input("What is your name?")
print(user_name, file=out_file)
out_file.close()
"""

#program 2
"""
in_file = open('name.txt', 'r')
print("Your name is", in_file.readline())
in_file.close()
"""

#program 3
"""
in_file = open('numbers.txt', 'r')
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
print(number_1 + number_2)
"""

#program 4
"""
in_file = open('numbers.txt', 'r')
total = 0

for x in in_file:
    number = int(x)
    total += number
in_file.close()
print(total)
"""