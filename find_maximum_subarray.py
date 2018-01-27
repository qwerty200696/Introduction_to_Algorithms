#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MAX = 1 << 31
import math


def find_max_crossing_subarray(A, low, mid, high):
    max_left = mid
    max_right = mid
    left_sum = 0  # original version init with -max, now is zero,because minimum is zero
    all_sum = 0
    for i in range(mid - 1, low - 1, -1):  # 左边不经过mid
        all_sum += A[i]
        if all_sum > left_sum:
            left_sum = all_sum
            max_left = i
    right_sum = A[mid]  # original version init with -max, now is A[mid],because A[mid] must be included.
    all_sum = 0
    for i in range(mid, high + 1):
        all_sum += A[i]
        if all_sum > right_sum:
            right_sum = all_sum
            max_right = i
    # print([low, mid, high], [max_left, max_right, left_sum + right_sum])
    return [max_left, max_right, left_sum + right_sum]


def find_maximum_subarray(A, low, high):
    if high == low:
        return [low, high, A[low]]
    else:
        mid = math.floor((low + high) / 2)
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return [left_low, left_high, left_sum]
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return [right_low, right_high, right_sum]
        else:
            return [cross_low, cross_high, cross_sum]


if __name__ == "__main__":
    A = [1, -3, 7, -1, 4, -1, -5, 3, -1, 3, -5, 9]
    # A = [1, -3, 7, -5, -4, -1, -9, -3, 1, -3, -5, -9]
    # print(find_max_crossing_subarray(A, 0, 6, len(A) - 1))
    print(find_maximum_subarray(A, 0, len(A) - 1))
    arr = [1, 2, 3, 4, 5]
    print(find_maximum_subarray(arr, 0, len(arr) - 1))
    arr = [-1, 2, 3, 4, 5, -1]
    print(find_maximum_subarray(arr, 0, len(arr) - 1))
    arr = [-1, -1, -1, -1]
    print(find_maximum_subarray(arr, 0, len(arr) - 1))
    arr = [1, -1, 1, -1, 5]
    print(find_maximum_subarray(arr, 0, len(arr) - 1))
    arr = [1, 5, 5, -1, 1, 4, 5, 7, -1, -3, 4, 5, 5 - 9]
    print(find_maximum_subarray(arr, 0, len(arr) - 1))
