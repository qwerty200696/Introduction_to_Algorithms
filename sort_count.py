#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author：wangwlj
# More info in blog: http://wangwlj.com
# 计数排序


def counting_sort(A):
    k = max(A)  # k is max of A
    C = []
    for i in range(0, k + 1):
        C.append(0)
    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    B = []  # output
    for i in range(0, len(A)):
        B.append(0)
    for j in range(len(A) - 1, -1, -1):
        # m = A[j],n  = C[m],k = B[n - 1]  # for test
        B[C[A[j]] - 1] = A[j]  # B[n] start from 0, so need -1
        C[A[j]] = C[A[j]] - 1
    return B


if __name__ == "__main__":

    A = [2, 5, 3, 0, 2, 3, 0, 3]
    B = counting_sort(A)
    for i in range(0, len(B)):
        print(B[i], end=" ")
