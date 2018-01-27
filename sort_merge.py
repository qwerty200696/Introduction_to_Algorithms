#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: wangwlj
# 归并排序
from math import floor

MAX = 1 << 31


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(0, n1):
        L.append(A[p + i])  # 因为我初始化为空列表，所以直接赋值的话会报错，只能以append的形式追加值。
    for i in range(0, n2):
        R.append(A[q + i + 1])
    L.append(MAX)  # 使用无穷大作为哨兵
    R.append(MAX)
    assert len(L) == n1 + 1 and len(R) == n2 + 1

    i = 0  # python是从0开始
    j = 0
    for k in range(p, r + 1):  # 需要加1，因为首尾每个都算
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        q = floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)  # 首尾都包含了，所以要加1
        merge(A, p, q, r)


if __name__ == "__main__":
    # test function
    A = [1, 3, 5, 2, 4, 6, 0, -1, 5]
    merge_sort(A, 0, len(A) - 1)
    print(A)
