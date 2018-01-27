#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: wangwlj
# 快速排序


def PARTITION(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):  # not r-1, but r
        if A[j] < x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]

    return i + 1


def QUICKSORT(A, p, r):
    if p < r:
        q = PARTITION(A, p, r)
        QUICKSORT(A, p, q - 1)
        QUICKSORT(A, q + 1, r)


if __name__ == "__main__":
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    # index = PARTITION(A, 0, len(A) - 1)
    # print(index)

    QUICKSORT(A, 0, len(A) - 1)  # all start from 0
    for i in range(0, len(A)):
        print(A[i], end="  ")


