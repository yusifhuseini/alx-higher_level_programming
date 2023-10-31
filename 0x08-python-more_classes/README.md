# Python - More Classes and Objects

The learning objectives are:
```
Why Python programming is awesome
What is OOP
“first-class everything”
What is a class
What is an object and an instance
What is the difference between a class and an object or instance
What is an attribute
What are and how to use public, protected and private attributes
What is self
What is a method
What is the special __init__ method and how to use it
What is Data Abstraction, Data Encapsulation, and Information Hiding
What is a property
What is the difference between an attribute and a property in Python
What is the Pythonic way to write getters and setters in Python
What are the special __str__ and __repr__ methods and how to use them
What is the difference between __str__ and __repr__
What is a class attribute
What is the difference between a object attribute and a class attribute
What is a class method
What is a static method
How to dynamically create arbitrary new attributes for existing instances of a class
How to bind attributes to object and classes
What is and what does contain __dict__ of a class and of an instance of a class
How does Python find the attributes of an object or class
How to use the getattr function
```

## Tasks 0 - 9

A class Rectangle that defines a rectangle by: (based on 8-rectangle.py)

- Private instance attribute: `width:`
	- property `def width(self):` to retrieve it
	- property setter `def width(self, value):` to set it:
		- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
		- if `width` is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: height:
	- property `def height(self):` to retrieve it
	- property setter `def height(self, value):` to set it:
		- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
		- if `height` is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances:`
	- Initialized to `0`
	- Incremented during each new instance instantiation
	- Decremented during each instance deletion
- Public class attribute `print_symbol:`
	- Initialized to `#`
	- Used as symbol for string representation
	- Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
	- if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`:
	- if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
	- `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
	- `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
	- Returns `rect_1` if both have the same area value
- Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`
- You are not allowed to import any module.

## Task 10: N queens
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

- Usage: nqueens N
	- If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
- where N must be an integer greater or equal to `4`
	- If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
	- If N is smaller than `4`, `print N must be at least 4`, followed by a new line, and exit with the status `1`
- The program should print every possible solution to the problem
	- One solution per line
	- Format: see example
	- You don’t have to print the solutions in a specific order
- You are only allowed to import the `sys` module
```
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$
```
