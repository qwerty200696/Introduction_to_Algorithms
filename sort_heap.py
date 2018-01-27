#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author： wangwlj
# 堆排序


from math import floor


def PARENT(i):
    return i / 2


def LEFT(i):
    return 2 * i


def RIGHT(i):
    return 2 * i + 1


def MAX_HEAPIFY(A, i, size):
    l = LEFT(i)
    r = RIGHT(i)
    largest = -1
    if l <= size and A[l - 1] > A[i - 1]:
        largest = l
    else:
        largest = i
    if r <= size and A[r - 1] > A[largest - 1]:
        largest = r

    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        MAX_HEAPIFY(A, largest, size)


def BUILD_MAX_HEAP(A):
    heap_size = len(A)
    for i in range(int(floor(heap_size / 2)), 0, -1):
        MAX_HEAPIFY(A, i, heap_size)


def HEAPSORT(A):
    BUILD_MAX_HEAP(A)
    heap_size = len(A)
    for i in range(len(A), 1, -1):
        A[1 - 1], A[i - 1] = A[i - 1], A[1 - 1]  # exchage A[i] with A[1]
        heap_size = heap_size - 1
        MAX_HEAPIFY(A, 1, heap_size)


if __name__ == "__main__":
    # A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    # MAX_HEAPIFY(A, 2)
    # for i in range(0, len(A)):
    #     print(A[i], end=" ")

    # A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    # BUILD_MAX_HEAP(A)
    # for i in range(0, len(A)):
    #     print(A[i], end=" ")

    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    HEAPSORT(A)
    for i in range(0, len(A)):
        print(A[i], end=" ")
