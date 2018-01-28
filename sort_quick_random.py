#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: wangwlj
# More info in blog: http://wangwlj.com
# 快速排序的随机化版本

import random


def PARTITION(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):  # not r-1, but r
        if A[j] < x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]

    return i + 1


def RANDOMIZED_PARTITION(A, p, r):
    rand_i = random.random()
    # print(round(a *(r - p)) + p)
    rand_i = round(rand_i * (r - p) + p)  # 区间的计算需要注意，否则不对
    A[rand_i], A[r] = A[r], A[rand_i]
    return PARTITION(A, p, r)


def RANDOMIZED_QUICKSORT(A, p, r):
    if p < r:
        q = RANDOMIZED_PARTITION(A, p, r)
        RANDOMIZED_QUICKSORT(A, p, q - 1)
        RANDOMIZED_QUICKSORT(A, q + 1, r)


if __name__ == "__main__":
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    # index = PARTITION(A, 0, len(A) - 1)
    # print(index)

    RANDOMIZED_QUICKSORT(A, 0, len(A) - 1)  # all start from 0
    for i in range(0, len(A)):
        print(A[i], end="  ")
