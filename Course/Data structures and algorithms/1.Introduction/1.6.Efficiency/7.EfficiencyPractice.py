"""One of the main goals of this lesson is to help you develop your ability to look at some code and identify its time complexity—and then describe this time complexity using Big O notation.

We will use this graph as a referece and reminder of the importance of the run time of an algorithm. We have the number of inputs (n) on the X axis and the the number of operations required (N) on the Y axis.

Drawing
<all-comparison-computational-complexity.svg>
"Comparison of computational complexity" by Cmglee. Used under CC BY-SA 4.0.
"""
"""Quadratic Example"""
# O(n^2)


def Quad_Example(our_list):
    for first_loop_item in our_list:
        for second_loop_item in our_list:
            print("Items: {}, {}".format(first_loop_item, second_loop_item))


Quad_Example([1, 2, 3, 4])
"""
Items: 1, 1
Items: 1, 2
Items: 1, 3
Items: 1, 4
Items: 2, 1
Items: 2, 2
Items: 2, 3
Items: 2, 4
Items: 3, 1
Items: 3, 2
Items: 3, 3
Items: 3, 4
Items: 4, 1
Items: 4, 2
Items: 4, 3
Items: 4, 4
CPU times: user 3 µs, sys: 0 ns, total: 3 µs
Wall time: 6.2 µs
"""


"""Log Linear Example"""
# O(nlogn)
# Don't worry about how this algorithm works, we will cover it later in the course!


def Log_Linear_Example(our_list):
    if len(our_list) < 2:
        return our_list

    else:
        mid = len(our_list)//2
        left = our_list[:mid]
        right = our_list[mid:]
        Log_Linear_Example(left)
        Log_Linear_Example(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                our_list[k] = left[i]
                i += 1
            else:
                our_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            our_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            our_list[k] = right[j]
            j += 1
            k += 1
        return our_list


Log_Linear_Example([56, 23, 11, 90, 65, 4, 35, 65, 84, 12, 4, 0])

"""Linear Example"""
# O(n)


def Linear_Example(our_list):
    for item in our_list:
        print("Item: {}".format(item))


Linear_Example([1, 2, 3, 4])

"""Logarithmic Example"""
# O(logn)


def Logarithmic_Example(number):
    if number == 0:
        return 0

    elif number == 1:
        return 1

    else:
        return Logarithmic_Example(number-1)+Logarithmic_Example(number-2)


Logarithmic_Example(29)
"""Constant Example"""
# O(1)


def Constant_Example(our_list):
    return our_list.pop()


Constant_Example([1, 2, 3, 4])


"""
What is the run time analysis of the following code: -> O(1)
"""


def main(x, y):
    if True:
        z = x + y
    for i in range(10):
        z += i
    return z


"""
What is the run time analysis of the following code: -> O(n^2)
"""


def main(list_1, list_2):

    count = 0

    for item_1 in list_1:
        for item_2 in list_2:
            if item_1 == item_2:
                count += 1

    return count


"""
What is the simplification of this run time analysis: 4n^2 + 3n + 7 ? -> n^2
"""


# https://www.bigocheatsheet.com/
# https://wiki.python.org/moin/TimeComplexity
