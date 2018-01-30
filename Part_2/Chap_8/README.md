---
title: 算法导论详解(7)之第八章 线性排序算法
date: 2018-01-27 16:26:53
categories: Algorithm
tags:
	- 算法导论
	- Algorithm
	- Sort
---


任何比较排序在最坏情况下都要经过$\Theta(n\text{lg}n)$次比较。

本文介绍三种线性时间排序的算法：计数排序，基数排序以及桶排序。因此，这些都不属于比较排序。

<!-- more -->

本文所有实现代码均已放在`GitHub`上，欢迎查看：[GitHub链接](https://github.com/qwerty200696/Introduction_to_Algorihtms)
## 本章概述

非比较排序指使用一些非比较的操作来确定排序顺序的排序算法，对于非比较排序，下界O(nlgn)不适用。

计数排序是稳定排序，若n个数据的取值范围是`[0..k]`，则运行时间为`O(n+k)`，运行空间是`O(n+k)`

基数排序也是稳定排序，需要另一个稳定排序作为基础，若n个d位数，每一位有k种取值可能，所用的稳定排序运行时间为`O(n+k)`，则基数排序的时间是`O(d(n+k))`

桶排序也是稳定排序，当输入数据符合均匀分布时，桶排序可以以线性时间运行。所设所有元素均匀分布在区间`[0,1)`上，把区间[0,1)划分成n个相同大小的子区间（桶），对各个桶中的数进行排序，把依次把各桶中的元素列出来。

## 计数排序（8.2，P108）
计数排序(`counting sort`)是使用输入元素的实际值来确定其在数组中的位置。

计数排序的一个重要特性就是它是稳定的：即对于相同值的元素在输出数组中的相对次序与它们在输入数组中的相对次序相同。也就是说，对两个相同的数来说，在输入数组中先出现的数，在输出数组中也位于前面。

计数排序的伪代码：
```c++
COUNTING_SORT(A,B,k)
      for i=0 to k
        do C[i] = 0
      for j=1 to length(A)
          do C[A[j]] = C[A[j]]+1   //C[i]中包含等于元素i的个数
      for i=1 to k
          do C[i] = C[i] + C[i-1]  //C[i]中包含小于等于元素i的个数
      for j=length[A] downto 1
          do B[C[A[j]]] = A[j]
             C[A[j]] = C[A[j]] -1
```

计数排序的`Python`实现：
```python
# Author：wangwlj
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
```

### 练习8.2-3
在`COUNTING_SORT`过程中，第四个for循环为什么是`for j=length[A] downto 1`，而不是`for j=1 to length[A]`？

**为了保证算法是稳定的**。由于是从前往后计数排序，两个数相同的时候，计数值较大的数对应于数组中靠后的元素，所以在输出时需要逆序。

## 基数排序（8.3，P110）
基数排序(`radix sort`)按有效位从低到高依次排序。

伪代码如下：
```
RADIX_SORT(A,d）
    for i=1 to d
          use a stable sort to sort array A on digit i
```

基数排序一般采用**计数排序**作为中间稳定排序。

基数排序的`python`实现请参阅下面的练习题`8.3-4`。

### 练习8.3-1
说明`RADIX-SORT`在如下英文单词上的操作过程：
```
    A = {COW, DOG, SEA, RUG, ROW, MOB, BOX, TAB, BAR, EAR, TAR, DIG, BIG, TEA, NOW, FOX}  
==> A = {SEA, TEA, MOB, TAB, DOG, RUG, DIG, BIG, BAR, EAR, TAR, COW, ROW, NOW, BOX, FOX}  
==> A = {TAB, BAR, EAR, TAR, SEA, TEA, DIG, BIG, MOB, DOG, COW, ROW, NOW, BOX, FOX, RUB}  
==> A = {BAR, BIG, BOX, COW, DIG, DOG, EAR, FOX, MOB, NOW, ROW, TAB, TAR, TEA, SEA, RUB} 
```

### 练习8.3-4
题目：在`O(n)`时间内对`[0..n^3-1]`之间的n个整数排序。

思路：把整数转换为n进制再排序，每个数有三位，每位的取值范围是[0..n-1]，再进行基数排序

实现：
```python
import random

n = 5
base_k = 5  # bask could be any number. In test 8.3-4 is 5(equal to n)
d = 3  # 8.3-4


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
    for i in range(1, d + 1):
        A = stable_sort(A, i)
    # for i in range(0, len(A)):
    #     print(A[i], end=' ')
    return A


if __name__ == "__main__":

    # A = [114, 18, 35, 74, 36]
    A = []
    for i in range(0, n):
        A.append(random.randint(0, pow(n, 3)))

    for i in range(0, len(A)):
        print(A[i], end=' ')
    print('\n')

    A = radix_sort(A)
    print('After radix_sort：')
    for i in range(0, len(A)):
        print(A[i], end=' ')
```

## 桶排序（8.4，P112）
桶排序(`bucket sort`)假设输入数据服从均匀分布，平均情况下它的时间代价为$\text{O}_n$，与计数排序类似，因为对输入数据做了某种假设，桶排序的速度也很快。具体来说，计数排序假设输入数据都属于一个小区间的整数，而桶排序则假设输入是由一个随机过程产生，该过程将元素均匀、独立地分布在[0,1)区间上。


## 参考资料
1.算法导论 中文 第三版
2.[算法导论 第8章 线性时间排序](http://blog.csdn.net/mishifangxiangdefeng/article/details/7678859)这个包含习题答案，很不错
3.[算法导论8.3-4](http://blog.csdn.net/mishifangxiangdefeng/article/details/7685839)
4.[MIT算法导论-第五讲-线性时间排序](http://blog.csdn.net/qing0706/article/details/50117873)
