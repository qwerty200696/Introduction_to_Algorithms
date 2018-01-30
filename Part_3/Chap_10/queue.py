#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 队列-先进先出
# Author: wangwlj
# Date: 2018年 01月 26日 星期五 13:41:25 CST
# More info in blog: http://wangwlj.com


class Queue(object):
    def __init__(self, elements, max_length=100, head_start=0):
        self.queue = []
        self.length = max_length  # max length
        self.head = head_start
        self.tail = self.head
        self.setup(elements)  # init

    def enqueue(self, element):
        if self.head == (self.tail + 1) or (self.head == 0 and self.tail == self.length - 1):
            raise Exception('overflow')
        e = element
        self.queue[self.tail] = e
        if self.tail == self.length - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.head == self.tail:  # is empty
            raise Exception('underflow')
        x = self.queue[self.head]
        if self.head == self.length - 1:
            self.head = 0
        else:
            self.head += 1
        return x

    def setup(self, elements):
        for i in range(self.length):
            self.queue.append(0)
        e = elements
        for i in range(len(e)):
            self.enqueue(e[i])

    def size(self):
        return self.tail - self.head if self.tail >= self.head \
            else self.length - (self.head - self.tail)


if __name__ == "__main__":
    q = Queue([], max_length=6, head_start=4)  # 最多存储5个元素
    print(q.queue, q.head, q.tail, q.size())
    q.enqueue(4)
    print(q.queue, q.head, q.tail, q.size())
    q.enqueue(1)
    print(q.queue, q.head, q.tail, q.size())
    q.enqueue(3)
    print(q.queue, q.head, q.tail, q.size())
    q.enqueue(5)
    print(q.queue, q.head, q.tail, q.size())
    q.enqueue(8)
    print(q.queue, q.head, q.tail, q.size())
    # q.enqueue(8)  # raise overflow
    # print(q.queue, q.head, q.tail, q.size())
