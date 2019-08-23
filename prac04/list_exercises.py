# Basic list operations
numbers = []
for i in range(5):
    number = int(input("Number:  "))
    numbers.append(number)


print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average number is {}".format(sum(numbers) / len(numbers)))


# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
get_username = input("Please enter your username")
if get_username in usernames:
    print("Access granted")
else:
    print("Access denied")
