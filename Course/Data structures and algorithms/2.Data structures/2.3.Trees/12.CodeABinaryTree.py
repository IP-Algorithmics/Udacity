'''
Task 1 intro: https://youtu.be/cixp2hq9_9w
Task 1 solution: https://youtu.be/9maTu-nA4Ec
Task 2 intro: https://youtu.be/UVYwV-z8bfk
Task 2 solution: https://youtu.be/ctNTo-pkF7g
Task 3 intro: https://youtu.be/IQy-bD-Cshw
Task 3 Solution: https://youtu.be/O1U-QfGnQ3U
Task 4 Intro: https://youtu.be/3wEcBGLM_Zo
Task 4 Solution: https://youtu.be/VoGdhGqSO00
Task 5 Intro: https://youtu.be/2Sf3ziM0K5Y
Task 5 Solution: https://youtu.be/HsSIPEyXydQ
Task 6 Intro: https://youtu.be/DxeYBbT_b8c
Task 6 Solution: https://youtu.be/-YGl9VvFGDg
Task 7 Intro: https://youtu.be/XUpEMUtwcyo
Task 7 Solution: https://youtu.be/AC19_mrfKP4
'''

# this code makes the tree that we'll traverse


class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root
