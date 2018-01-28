#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author: wangwlj
# More info in blog: http://wangwlj.com
# 优先队列


def PARENT(i):
    return i / 2


def LEFT(i):
    return 2 * i


def RIGHT(i):
    return 2 * i + 1


def MAX_HEAPIFY(A, i, heap_size):
    l = LEFT(i)
    r = RIGHT(i)
    largest = -1
    if l <= heap_size and A[l - 1] > A[i - 1]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r - 1] > A[largest - 1]:
        largest = r

    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        MAX_HEAPIFY(A, largest, heap_size)


def HEAP_MAXIMUM(A):
    return A[1]


def HEAP_EXTRACT_MAX(A, heap_size):
    if heap_size < 1:
        print("ERROR!! Heap underflow!!")
        return -1
    max_A = A[1 - 1]
    A[1 - 1] = A[heap_size - 1]
    heap_size = heap_size - 1
    MAX_HEAPIFY(A, 1, heap_size)
    return max_A


def HEAP_INCREASE_KEY(A, i, key):
    if key < A[i - 1]:
        print("ERROR!! New key is smaller than current key!!!")
        return
    A[i - 1] = key
    while i > 1 and A[int(PARENT(i) - 1)] < A[int(i - 1)]:
        A[int(PARENT(i) - 1)], A[int(i - 1)] = A[int(i - 1)], A[int(PARENT(i) - 1)]
        i = PARENT(i)


def MAX_HEAP_INSERT(A, key):
    MAX_INT = 0x7fffffff
    heap_size = len(A) + 1
    A.append(- MAX_INT)  # 尾部追加元素
    HEAP_INCREASE_KEY(A, heap_size, key)


if __name__ == "__main__":
    # A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    # HEAP_INCREASE_KEY(A, 9, 15)  # 调用的数值都是从1开始。
    # for i in range(0, len(A)):
    #     print(A[i], end=" ")

    A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    MAX_HEAP_INSERT(A, 9)  # 调用的数值都是从1开始。
    for i in range(0, len(A)):
        print(A[i], end=" ")
