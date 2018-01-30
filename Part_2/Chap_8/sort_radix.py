#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 基数排序
# Author：wangwlj
# Date: 2018年 01月 27日
# More info in blog: http://wangwlj.com

"""
    A 有n个数，每个数得到范围都是n^3-1。
    基数排序：每个数均为nDigits位数(书中用d表示)，每位数有k个取值可能（基【也就是进制】为k，即base_k）。

"""
import random

chn = 5  # the number of elements to be sorted.
base_k = 5  # bask could be any number. In test 8.3-4 is 5(equal to n)
nDigits = 3  # 位数的个数，表示几(3)位数  8.3-4


def stable_sort(A, index):  # similar with counting sort,
    C = []  # C：统计每位数上可能出现的k个数的次数
    for i in range(0, base_k + 1):  # the number is in range of base_k（k）
        C.append(0)
    for j in range(0, len(A)):
        # 统计当前位上的数出现的次数
        num = int(A[j] % pow(base_k, index) / pow(base_k, index - 1))  # the base number
        # print(A[j], ' 当前位编号：', index, '当前值：', num, )  # for test
        C[num] = C[num] + 1  # the count of the base number (C - num)
    for i in range(1, base_k + 1):
        C[i] = C[i] + C[i - 1]

    B = []  # output
    for i in range(0, len(A)):
        B.append(0)
    for j in range(len(A) - 1, -1, -1):
        num = int(A[j] % pow(base_k, index) / pow(base_k, index - 1))
        B[C[num] - 1] = A[j]  # B[n] start from 0, so need -1
        C[num] = C[num] - 1
    return B


def radix_sort(A):
    for i in range(1, nDigits + 1):
        A = stable_sort(A, i)
    # for i in range(0, len(A)):
    #     print(A[i], end=' ')
    return A


if __name__ == "__main__":

    # A = [114, 18, 35, 74, 36]
    A = []
    for i in range(0, n):
        A.append(random.randint(0, pow(n, nDigits)))

    for i in range(0, len(A)):
        print(A[i], end=' ')
    print('\n')

    A = radix_sort(A)
    print('After radix_sort：')
    for i in range(0, len(A)):
        print(A[i], end=' ')
