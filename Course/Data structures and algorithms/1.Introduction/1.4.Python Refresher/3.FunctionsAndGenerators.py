""" Python Functions """
# Example function 1: return the sum of two numbers.


def sum(a, b):
    return a+b

# Example function 2: return the size of list, and modify the list to now be sorted.


def list_sort(my_list):
    my_list.sort()
    return len(my_list),  my_list


""" Python Generators """
""" generator in Python is similar to a function except instead of returning a value and exiting a process, a generator will pause the process, saving its state for next time.
The biggest difference between a function and generator from a code perspective is one word: return is changed to yield.
A generator becomes very useful when dealing with very large collections of data that you don’t want to store in memory all at once. It’s also very useful for dealing with extremely large or even infinite series.
Below is an example of how to use a generator to print even numbers. Printing all even numbers at once would take an infinite amount of time, but the generator allows the process to pause, and go back to creating even numbers when needed.
To create the next successive even number simply call next() on the generator object, and it will yield the next iteration. 
After yield is called, everything in the state of the generator function freezes, and the value is returned. When the generator is called again with next(), it picks back up right where it stopped at yield from before."""
# Definition of the generator to produce even numbers.


def all_even():
    n = 0
    while True:
        yield n
        n += 2


my_gen = all_even()

# Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))

# Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)

# Now go back to generating more even numbers.
for i in range(100):
    print(next(my_gen))


""" Exercise 1 """
"""In the following exercise, you will create a generator fact_gen() that generates factorials. 
For a number n, n factorial is denoted by n!, and it is the product of all positive integers less than or equal to n. For example, 5! = 5 * 4 * 3 * 2 * 1 = 120"""


def prod(a, b):
    # TODO change output to the product of a and b
    return a*b


def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product
        i += 1
        n = output


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120


""" Exercise 2 """
"""In the next exercise, you will write a function that checks sudoku squares for correctness.
A valid sudoku square satisfies these two properties:
Each column of the square contains each of the whole numbers from 1 to n exactly once.
Each row of the square contains each of the whole numbers from 1 to n exactly once.
"""
correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

# Define a function check_sudoku() here:
# An example solution for the check_sudoku() function


def check_sudoku(square):
    for row in square:
        # Create a list with the integers 1, 2, ..., n.
        # We will check that each number in the row is in the list
        # and remove the numbers from the list once they are verified
        # to ensure that each number only occurs once in the row.
        check_list = list(range(1, len(square[0]) + 1))
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
    for n in range(len(square[0])):
        # We do the same here for each column in the square.
        check_list = list(range(1, len(square[0]) + 1))
        for row in square:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])
    return True


print(check_sudoku(incorrect))  # >>> False
print(check_sudoku(correct))  # >>> True
print(check_sudoku(incorrect2))  # >>> False
print(check_sudoku(incorrect3))  # >>> False
print(check_sudoku(incorrect4))  # >>> False
print(check_sudoku(incorrect5))  # >>> False
