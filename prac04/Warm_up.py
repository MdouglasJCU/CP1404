numbers = [3, 1, 4, 1, 5, 9, 2]
"""
numbers[0] = Will select 3
numbers[-1] = Will select 2
numbers[3] = Will select 1
numbers[:-1] = Will remove 2
numbers[3:4] = Will select 1
5 in numbers = True
7 in numbers = False
"3" in numbers = False
numbers + [6, 5, 3] = won't work
"""

#1 Change the first element of numbers to "ten"
numbers[0] = "ten"

#2 Change the last element of numbers to 1
numbers[-1] = 1

#3 Get all the elements from numbers except the first two
numbers[:2]

#4 Check if 9 is an element of numbers
9 in numbers