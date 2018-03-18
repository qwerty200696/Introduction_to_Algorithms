

## 二叉搜索树概述

搜索树数据结构支持许多动态集合操作：`SEARCH`、`MINIMUM`、`MAXIMUM`、`PREDECESSOR`、`SUCCESSOR`、`INSERT`与`DELETE`。

上述基本操作花费的时间与这棵树的高度成正比。

### 定义与性质
（1）设`x`为二叉查找树中的一个结点，若`y`是`x`左子树中的一个结点，则`key[y] <= key[x`]；若`y`是`x`右子树中的一个结点，则`key[x]<=key[y]`
（2）二叉查找树上执行的基本操作的时间与树的高度成正比。

### 结构
每个节点就是一个对象，包含：关键字`key`，卫星数据`data`，以及三个属性：分别指向父、左右孩子的指针`p`,` left`, `right`

### 在二叉查找树上的操作
查找一个关键字：SEARCH(x, k)
求最小关键字：MINIMUM(x)
求最大关键字：MAXIMUM(x)
求前驱：PREDECESSOR(x)
求后继：SUCCESSOR(x)
插入一个结点：INSERT(T, z)
删除一个结点：DELETE(z)
### 二叉查找树的应用
1.遍历：中序遍历、先序遍历、后序遍历【根关键字遍历的先后顺序】

2.查找：查找包含某个关键字的结点，查找关键字最大或最小的结点、查找某个结点的前驱或后继

### 12.1-2
二叉搜索树的性质与最小堆的性质有什么不同？

二叉搜索树：左子树关键字<=根结点关键字<=右子树关键字

最小堆：左子树关键字>=根结点关键字 && 右子树关键字>=根结点关键字

不能，因为一个结点的的左子树与右子树的关键字大小没有关系
 
### 12.1-3 遍历的非递归实现
给出一个非递归的中序树遍历算法。(提示：有两种方法，在较容易的方法中，可以采用栈作为辅助数据结构；较复杂的方法中，不采用栈结构，但假设可以测试两个指针是否相等)。

中根遍历要求顺序是左根右，借助栈s实现。先将根root入栈，接着从根root开始查找最左的子孩子结点直到为空为止，然后将空节点出栈，再将左子树节点出栈遍历，然后判断该左子树的右子树节点入栈。循环此过程，直到栈为空为止。此时需要注意的是入栈过程中空结点也入栈了，用以判断左孩子是否结束和左孩子是否有右孩子结点。
```C++
//中序遍历非递归过程
void BST_Tree::Inorder_Iterative_Traverse(BST_Node *root)
{  //用C++STL——栈stack实现
    if (root == NULL) return; //空树
    stack<BST_Node *>s;
    s.push(root);
    while (!s.empty()) {
        BST_Node *p = s.top();
        while(p != NULL)        //直到左节点为空，即最小元素
        {
            s.push(p->left);
            p = s.top();
        }                           
        s.pop();                //空结点出栈
        if(!s.empty())
        {
            p = s.top();
            cout << p->key << " ";
            s.pop();
            s.push(p->right);   //右子树结点入栈（不一定有右节点，可以压入NULL
        }
    }
    cout << endl;
}
```

一个更加简洁的写法：
```cpp
//中序遍历非递归过程——简洁版
void BST_Tree::Inorder_Iterative_Traverse_2(BST_Node *root)
{  //用C++STL——栈stack实现
    stack<BST_Node *>s;
    BST_Node *p = root;
    while (p || !s.empty()) {
        if(p != NULL)           //左节点入栈
        {
            s.push(p);          //压入值非空
            p = p->left;
        }
        else
        {   //出栈遍历
            p = s.top();
            cout << p->key << " ";
            s.pop();
            p = p->right;
        }
    }
    cout << endl;
}
```

## 查询二叉搜索树

### 查找任一节点
伪码：
```
TREE-SEARCH(x, k)
	if x == NIL or k == x.key
    	return x
    if k < x.key
    	return TREE-SEARCH(x.left, k)
   	else return TREE-SEARCH(x.right, k)

INTERATIVE-TREE-SEARCH(x, k)
	while x != NIL and k != x.key
        if k < x.key
            x = x.left
        else x = x.right
    return x
```
运行时间为$O(h)$，h为树的高度。

### 最大关键字元素和最小关键字元素
根据二叉查找树的特征，很容易查找出最大和最小关键字。
查找二叉树中的最小关键字：从根结点开始，沿着各个节点的left指针查找下去，直到遇到NULL时结束。如果一个结点x无左子树，则以x为根的子树中，最小关键字就是key[x]。
查找二叉树中的最大关键字：从根结点开始，沿着各个结点的right指针查找下去，直到遇到NULL时结束。

书中给出了查找最大最小关键字的伪代码：

```
TREE-MINIMUM(x)
	while x.left != NIL
    	x = x.left
    return x
    
TREE-MAXIMUM(x)
	while x.right != NIL
    	x = x.right
    return x
```
均能在$O(h)$时间内执行完。

### 后继与前驱
伪码：
```
TREE-SUCCESSOR(x)
	if x.right != NIL
    	return TREE-MINIMUM(x.right)
    y = x.p
    while y != NIL and x == y.right
    	x = y
        y = y.p
    return y
```
x.p 指向双亲。 右侧为空，则向上搜索。

> 在一颗高度为`h`的二叉搜索树上，动态集合上的操作`SEARCH`、`MINIMUM`、`MAXIMUM`、`SUCCESSOR` 和`PREDECEDOR`可以在$O(h)$时间内完成。

## 插入和删除

### 插入
伪码：
```
TREE-INSERT(T,z)
	y = NIL
    x = T.root
    while x != NIL
    	y = x
        if z.key < x.key
        	x = x.left
        else x = x.right
    z.p = y
    if y == NIL
    	T.root = z   # tree T is empty
    else if z.key < y.key
    	y.left = z
    else y.right = z
```
从树根开始，指针x记录了一条向下的简单路径，直到查找到要替换为输入项z的NIL。NIL占据的位置就是z放置的位置。
上述过程保持遍历指针(`trailing pointer`)y作为x的双亲，找到NIL时需要直到z属于哪个节点。

该过程可以在$O(h)$时间内完成。
### 删除
从二叉查找树中删除给定的结点z，分以下情况讨论：

- 如果z没有左孩子，那么用右孩子来替换z
- 如果z有且仅有一个左孩子，那么用其左孩子替换z
- 否则，z既有左孩子又有右孩子，此时我们查找z 的后继y，这个后继位于z的右子树中并且没有左孩子。则将y移出原来的位置进行拼接，并替换数中的z。
- 如果y是z的右孩子，那么用y替换z，并且仅留下y的右孩子。


伪码：
```
TRANSPLANT(T,u,v)
    if u.p == NIL
        T.root = v
    else if u == u.p.left
        u.p.left = v
    else u.p.right = v
    if v != NIl
        v.p = u.p
        
TREE-DELETE(T,z)
	if z.left == NIL
    	TRANSPLANT(T,z,z.right)
	else if z.right == NIL
    	TRANSPLANT(T,z,z.left)
    else y = TREE-MINIMUM(z.right)
    	if y.p != z
        	TRANSPLANT(T,y,y.right)  # 删除y
            y.right = z.right
            y.right.p = y
        TRANSPLANT(T,z,y)
        y.left = z.left
        y.left.p = y
```

> 定理12.3 在一颗高度为`h`的二叉搜索树上，实现动态集合操作`INSERT`和`DELETE`的运行时间均为$O(h)$。

## 随机构建二叉搜索树

二叉查找树各种操作时间均是$O(h)$，构建二叉查找树时，一般只用插入函数，这样便于分析，如果按严格增长顺序插入，那么构造出来的树就是一个高度为`n-1`的链。另一方面练习`B.5-4`说明了`h≥lgn`.这里我特别证明下。

证明：一个有n个结点的非空二叉树的高度至少为`lgn`。

对于一个高度为`h`的二叉树总结点数至多为`n≤2^h-1`(等于的情况就是完全二叉树)，所以给这个不等式适当变型得：`h≥lg(n+1)≥lgn`,所以对于`n`个结点的数高度至少为`lgn`。虽然没有用归纳法，但是这种方法感觉简单易懂。

> 定理12.4 一棵有`n`个不同关键字的随机构建二叉搜索树(`random built binary search tree`)的期望高度为`O(lgn)`。


## 参考资料

- 算法导论 第三版 中文版
- [算法导论第十二(12)章 二叉查找树](http://blog.csdn.net/z84616995z/article/details/28880407)
- [算法导论 第12章 二叉查找树](http://blog.csdn.net/mishifangxiangdefeng/article/details/7718917)
- [《算法导论》第12章 二叉查找树](http://blog.csdn.net/luming_xml/article/details/51277023)
- [二叉树的递归与非递归实现](http://blog.csdn.net/z84616995z/article/details/20854381)
- [对于二叉树三种非递归遍历方式的理解](http://blog.csdn.net/sdulibh/article/details/50573036)
