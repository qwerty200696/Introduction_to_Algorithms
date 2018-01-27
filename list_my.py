#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 链表(未排序and双向)-无哨兵版本
# Author: wangwlj
# Date: 2018年 01月 26日
# More info in blog: http://wangwlj.com


class Node:  # 链表的每个节点
    def __init__(self, value=None, _prev=None, _next=None):
        self.value = value
        self.prev = _prev
        self.next = _next

    def __str__(self):  # 在print时默认返回value
        return str(self.value)


class List:
    def __init__(self):
        self.head = None  # init as a empty list

    def search(self, key):
        x = self.head
        while x.next is not None and x.value != key:
            x = x.next
        return x

    def insert(self, x):
        # 插入节点x作为新的头节点
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def delete(self, x):
        # x is in list and known (can use search to find)
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next

        if x.next is not None:
            x.next.prev = x.prev

    def show_value(self):
        # 依次打印链表的值
        x = self.head
        print("The List Value is:", end=' ')
        while x is not None:
            print(x.value, end=' ')
            x = x.next
        print()
        return 'show_value'

    def __str__(self):
        # 支持直接print一个List的对象
        return self.show_value() + " in List"


if __name__ == "__main__":
    l = List()
    l.insert(Node(5))
    l.insert(Node(4))
    l.insert(Node(3))
    n = l.search(5)
    print("search value: ", n.value, n.prev, n.next,
          "\nhead: ", l.head.value, l.head.prev, l.head.next)
    l.delete(n)
    print("head: ", l.head.value, l.head.prev, l.head.next)
    l.insert(Node(6))  # always insert as head.
    l.insert(Node(7))
    l.insert(Node(8))
    l.show_value()

    n = l.search(7)
    print("search value:", n, n.prev, n.next,
          "\nhead:", l.head, l.head.prev, l.head.next)

    l.delete(l.search(6))
    print(l)
    print(type([1]))
