# Star Patterns Generator
# Author: Dhruv Sharma

def lower_triangle(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n + 1):
        print("* " * i)
    print()


def upper_triangle(n):
    print("Upper Triangular Pattern:")
    for i in range(n, 0, -1):
        print("* " * i)
    print()


def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '* ' * (i + 1)
        print(spaces + stars)
    print()


# Modify this value to change pattern size
rows = 5

lower_triangle(rows)
upper_triangle(rows)
pyramid(rows)
