---
title: 算法导论详解(3) 第四章分治策略
date: 2018-01-08 16:43:37
categories: Algorithm
tags:
	- 算法导论
	- Algorithm
	- 最大子数组
	- 矩阵乘法
	- 分治
---
本章讲解更多关于分治策略的算法。第一个算法是求解最大子数组的问题，然后是求解$n\times n$矩阵乘法问题的分治算法，最后介绍了主方法。

<!-- more -->

## 分治策略简介

分治策略在每层递归时都有三个步骤：
- 分解原问题为若干子问题；子问题的形式与原问题一样，只是规模更小。
- 解决这些子问题，递归地求解各子问题。如果子问题的规模足够小，则停止递归，直接求解。
- 合并这些子问题的解成原问题的解。

递归情况(recursive case)
基本情况(base case)：子问题足够小的时候，递归已经“触底”时。


递归式：我们用递归式描述了MERGE-SORT过程的最坏情况运行时间$T(n)$：
$$T(n) = 
 \begin{cases}
  \Theta(1) & 若n=1 \\
 2T(n/2)+f(n) &  若n>1\\
  \end{cases}
$$
求解递归式的方法：代入法（猜测）；递归树法；主方法。本书使用主方法。

主方法可求解形如下面公式的递归式的界：
$$T(n) = aT(n/b)+f(n)$$
其中，$a\geqslant 1,b>1,f(n)$是一个给定的函数。

递归式的技术细节
- 忽略递归式声明和求解的一些细节，如MERGE-SORT的最坏情况运行时间准确的递归式为：

$$T(n) = 
 \begin{cases}
  \Theta(1) & 若n=1 \\
 T(\lceil n/2\rceil )+T(\lfloor n/2\rfloor )+\Theta(n) &  若n>1\\
  \end{cases}
$$

- 边界条件是我们通常忽略的细节。
- 当声明、求解递归式时，我们常常忽略向下取整、向上取整及边界条件。

本章讲解更多关于分治策略的算法。第一个算法是求解最大子数组的问题，然后是求解$n\times n$矩阵乘法问题的分治算法。

## 最大子数组问题(4.1，P38)
### 问题
买股票（低价买入，高价卖出）。给定一段时间，选取最大收益。

### 问题变换
不关注每天的价格，而是关注每日价格变化。
那么问题就转化为寻求价格变化数组A的最大非空连续子数组。
称这样的连续子数组为**最大子数组**。

### 使用分治策略的求解方法

```python
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
```

### 分治算法的分析
假设问题规模为2的幂，这样所有问题的规模都是整数。

在`find_maximum_subarray`函数中，需要求解两个子问题——左数组和右数组(分别为5/6行)，每个子问题的运行时间为$T(n/2)$，两个子问题加起来就是$2T(n/2)$。
第7行，`find_max_crossing_subarray`函数求解跨越中点的子数组，花费线性的时间，为$\Theta (n)$。

总的运行时间递归式为：
$$T(n) = \begin{cases}
\Theta (1) & if\ \ n=1\\
2T(n/2)+\Theta (n) & if\ \  n>1
\end{cases}
$$
与鬼归并排序的递归式相同。在4.5节用主方法求解该递归式，其解为$T(n) =\Theta (n\ \text{lg}n) $。

### 线性复杂度的解法--习题4.1-5(P42)

主要思想：从左到右处理，记录目前为止已经处理的最大子数组。非递归、线性复杂度。

从左到右累加，如果当前子数组的累加和小于零，则意味着最大子数组(maximun subarray)肯定不包括该子数组，所以果断舍弃，重新开始累加。

该解法的python实现：
```python
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
```


## 矩阵乘法的Strassen算法(4.2，P43)

若$A=(a_{ij}),B=(b_{ij})$是$nxn$的方阵，则对$i,j=1,2,\cdots ,n$,定义矩阵乘积$C=A\cdot B$中的$c_{ij}$为：
$$c_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$$

写成程序，是一个三重循环，因此，复杂度为$\Theta (n^3)$。

```python
def SQUARE_MATRIX_MULTIPLY(A, B):  
    assert(len(A) == len(B))  
    n = len(A)  
    C = [[0 for col in range(n)] for row in range(n)]  
    for i in range(0, n):  
        for j in range(0, n):  
            for k in range(0, n):  
                C[i][j]= C[i][j] + A[i][k]*B[k][j]  
    return C
```


### 一个简单的分治算法(4.2，P43)
假定三个矩阵均为$n\times n$矩阵，其中n为2的幂。在每个分解步骤中，$n\times n$矩阵都被划分为4个$n/2 \times n/2$的子矩阵，如下：
$$A = \begin{bmatrix}
A_{11} & A_{12}\\A_{21} & A_{22}
\end{bmatrix}, 
B = \begin{bmatrix}
B_{11} & B_{12}\\B_{21} & B_{22}
\end{bmatrix},
C = \begin{bmatrix}
C_{11} & C_{12}\\C_{21} & C_{22}
\end{bmatrix}
$$
因此，公式$C=A\cdot B$改写成：
$$\begin{bmatrix}
C_{11} & C_{12}\\C_{21} & C_{22}
\end{bmatrix}= \begin{bmatrix}
A_{11} & A_{12}\\A_{21} & A_{22}
\end{bmatrix} \cdot
\begin{bmatrix}
B_{11} & B_{12}\\B_{21} & B_{22}
\end{bmatrix}
$$
等价于：
$$\begin{matrix}
C_{11} = A_{11}\cdot B_{11} + A_{12}\cdot B_{21} \\
C_{12} = A_{11}\cdot B_{12} + A_{12}\cdot B_{22} \\
C_{21} = A_{21}\cdot B_{11} + A_{22}\cdot B_{21} \\
C_{22} = A_{21}\cdot B_{12} + A_{22}\cdot B_{22}
\end{matrix}$$

该简单分治算法的总运行时间递归式为：
$$T(n) = \begin{cases}
\Theta (1) & if\ \ n=1\\
8T(n/2)+\Theta (n^2) & if\ \  n>1
\end{cases}
$$
### Strassen 方法(4.2，P45)

为减小时间复杂度，采用Strassen 法，其原理仍将讲矩阵A,B,C划分成n/2 x n/2 ,然后按如下计算：

![](http://ww1.sinaimg.cn/large/c38a0784ly1fn945rgi23j20bx08575e.jpg)

即：先创建10个矩阵$S_1,\cdots,S_{10} $，由于进行了10次$n/2\times n/2$矩阵的加减法，所以该步骤花费$\Theta(n^2)$时间。

接着，递归地计算七次$n/2\times n/2$矩阵的乘法，即计算$P_1,\cdots,P_{7}$矩阵。

最后计算结果矩阵C的子矩阵$C_{11},C_{12},C_{21},C_{22}$。

其时间复杂度为：

$$T(n)= \begin{cases}
\Theta (1) & if\ \ n=1\\
7T(n/2)+\Theta (n^2) & if\ \  n>1
\end{cases}
$$

利用4.5节的主方法，可以求出上述的解为：
$$T(n)= \Theta(n^{\text{lg}7}) $$

## 用主方法求解递归式(4.5，P53)

主方法依赖于主定理。

### 主定理

令$a\geqslant 1$和$b>1$是常数，$f(n)$是一个函数，$T(n)$是定义在非负整数上的递归式：
$$T(n)= aT(n/b)+f(n)$$

其中，我们将$n/b$解释为$\lfloor n/b \rfloor$或$\lceil n/b \rceil$。那么$T(n)$有如下的渐近界：

1. 若对某个常数$\epsilon > 0$有$f(n) = \text{O}(n^{\text{log}_ba - \epsilon})$，则$T(n)=\Theta(n^{\text{log}_ba} )$

2. 若$f(n) = \Theta(n^{\text{log}_ba})$，则$T(n)=\Theta(n^{\text{log}_ba} \text{lg}n)$
3. 若对某个常数$\epsilon > 0$有$f(n) = \Omega(n^{\text{log}_ba + \epsilon})$，且对某个常数$c<1$和所有足够大的n有$aT(n/b)\leqslant cf(n)$，则$T(n)=\Theta(f(n) )$

以上就是主定理的完整叙述。

解释：我们将函数$f(n)$和$n^{\text{log}_ba}$进行比较。直觉上，两个函数较大者决定了递归式的解。
情况1表示：函数$n^{log_ba}$更大，则解为$T(n)=\Theta(n^{\text{log}_ba} )$；
情况3表示：函数$f(n)$更大，则解为$T(n)=\Theta(f(n) )$。
情况2表示：当两个函数大小相当，则乘上一个对数因子，解为$T(n)=\Theta(n^{\text{log}_ba} \text{lg}n)$。

> 上述的大于/小于都是多项式意义上的，也就是渐近小于(大于)。每种情况之间都有一定的间隙。若$f(n)$落在间隙中，就不能使用主方法。

### 使用主方法

使用主方法，只需要确定主定理的哪种情况成立，即可以得到解。

下面举几个例子。

$$T(n)= 9T(n/3)+n$$
上式中，$a=9,b=3,f(n) = n$，因此，$n^{\text{log}_ba} =n^{\text{log}_39} = \Theta(n^2) $。由于$f(n) = \text{O}(n^{\text{log}_39 - \epsilon})$，其中$\epsilon = 1$，所以应用主定理的情况1，从而得到$T(n) = \Theta(n^2) $

$$T(n)= T(2n/3)+1$$
上式中，$a=1,b=3/2,f(n) = 1$，因此，$n^{\text{log}_ba} =n^{\text{log}_{3/2}1} =n^0 = 1 $，由于$f(n) = \Theta(n^{\text{log}_ba}) = \Theta (1)$，所以，适用于情况二，从而得到最终解为$T(n) = \Theta(\text{lg} n ) $

归并排序和最大子数组方法的运行时间的递归式：
$$ T(n)= 2T(n/2)+\Theta(n)$$
同理，$n^{\text{log}_ba} =n^{\text{log}_{2}2} =n $， 由于$f(n) = \Theta(n)$，所以应用情况2，得到解$T(n) = \Theta(n\text{lg} n ) $

矩阵乘法的第一个分治算法的运行时间：
$$ T(n)= 8T(n/2)+\Theta(n^2)$$
上式，有：$n^{\text{log}_ba} =n^{\text{log}_{2}8} =n^3 $，$n^3$多项式意义上大于$f(n)$，因此应用情况1，解为$T(n) = \Theta(n^3) $

矩阵乘法的Strassen算法运行时间：
$$ T(n)= 7T(n/2)+\Theta(n^2)$$
上式中，有$n^{\text{log}_ba} =n^{\text{log}_{2}7} = n^{\text{lg}7}$，由于$2.80<lg7<2.81$，对$\epsilon = 0.8$，有$f(n) = \text{O}(n^{\text{lg}7-\epsilon})$，故应用情况1，得到：$T(n) = \Theta(n^{\text{lg}7}) $


## 参考资料
- 算法导论 中文版 原书第三版
- [算法导论 第四章：分治法(二)](http://blog.csdn.net/u010183397/article/details/46866577)
- [算法导论课后习题解析 第四章 上](http://blog.csdn.net/sushauai/article/details/50491477)
