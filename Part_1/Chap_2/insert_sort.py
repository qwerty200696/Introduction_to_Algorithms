#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
对插入排序的简单理解：
从第二个数开始，依次比较前面的数和key的大小，若大于key，则后移。
最后将key插入到最前方停下的位置。
j是遍历数组每个元素；
i是每个元素前面、需要移动的最前方。

形象的解释：插入纸牌：key是当前带插入的牌，找到插入的位置，先把每个大的都往后挪一个位置出来，再把key插入到空出来的位置。
"""
# Author: wangwlj
# More info in blog: http://wangwlj.com
# 插入排序

def insertion_sort(A):
    length = len(A)
    for j in range(1, length):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


A = [5, 3, 19, 1, 8, ]
print(insertion_sort(A))
"""
[1, 3, 5, 8, 19]
"""