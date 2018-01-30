#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
def find_maximum_subarray(A):
    j = 0
    max_sum = 0
    left = -1
    cur_left = 0
    right = -1
    sum = 0
    for j in range(0, len(A)):
        sum = sum + A[j]
        if sum > max_sum:
            max_sum = sum
            left = cur_left
            right = j
        elif sum < 0:
            sum = 0
            cur_left = j + 1
    if max_sum > 0:
        return left, right, max_sum
    return None


if __name__ == "__main__":
    A = [1, -3, 7, -1, 4, -1, -5, 3, -1, 3, -5, 9]
    # A = [1, -3, 7, -5, -4, -1, -9, -3, 1, -3, -5, -9]
    # print(find_max_crossing_subarray(A, 0, 6, len(A) - 1))
    print(find_maximum_subarray(A))
    arr = [1, 2, 3, 4, 5]
    print(find_maximum_subarray(arr))
    arr = [-1, 2, 3, 4, 5, -1]
    print(find_maximum_subarray(arr))
    arr = [-1, -1, -1, -1]
    print(find_maximum_subarray(arr))
    arr = [1, -1, 1, -1, 5]
    print(find_maximum_subarray(arr))
    arr = [1, 5, 5, -1, 1, 4, 5, 7, -1, -3, 4, 5, 5 - 9]
    print(find_maximum_subarray(arr))
