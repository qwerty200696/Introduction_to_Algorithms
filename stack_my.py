#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 栈-后进先出


class Stack(object):
    def __init__(self, elements, max_length=100):
        # elements is a list
        self.stack = []
        self.top = 0  # represent the number of elements
        self.max_length = max_length
        self.setup(elements)

    def empty(self):
        if self.top == 0:
            return True
        else:
            return False

    def push(self, element):
        if self.top >= self.max_length:
            raise Exception('overflow')
        self.top += 1
        self.stack.append(element)

    def pop(self):
        # if self.top == 0:
        #     raise Exception('underflow')
        self.top -= 1
        return self.stack.pop()

    def setup(self, elements):
        e = elements
        for i in range(len(e)):
            self.push(e[i])

    def length(self):
        return self.top

    def size(self):
        return self.top


if __name__ == "__main__":
    s = Stack([1, 2, 3])
    print(s.stack, s.pop())
    print(s.length(), s.empty())
    print(s.pop())
    print(s.pop())
    print(s.empty())
    # s.pop()  #UNDERFLOW
    s.max_length = 1
    s.push(1)
    print(s.size())
    # s.push(2)  #OVERFLOW
