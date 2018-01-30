
![](http://ww1.sinaimg.cn/large/c38a0784ly1fnva4kd9a0j20k50j5wjm.jpg)
本章介绍几种基本的结构：栈、队列、链表和有根树。

<!-- more -->

## 栈和队列（10.1，P129）
栈和队列都是动态集合。

### 栈stack

**概念定义**：栈采用**<font color=FA1C1C>先进后出</font>**策略（LIFO）。基本操作是**压入（PUSH）**和**弹出（POP）**。如果`s.top=0`，表示栈空，如果试图对空栈进行`POP`操作会发生下溢（`underflow`）。如果`s.top>n`,表示栈满，如果进行`PUSH`操作会发生上溢（`overflow`）。

栈的Python实现代码链接：[Introduction_to_Algorihtms/stack_my.py](https://github.com/qwerty200696/Introduction_to_Algorihtms/blob/master/stack_my.py)

### 队列queue
**概念定义**：队列采用**<font color=FA1C1C>先进先出</font>**策略（FIFO）。基本操作是**入队（enqueue）**和**出队（dequeue）**。如果`head=tail`，表示队列为空，如果试图对空队列进行`enqueue`操作会发生下溢（`underflow`）。如果`head=tail+1`,表示队列满，如果进行`dequeue`操作会发生上溢（`overflow`）。

队列的Python实现：[Introduction_to_Algorihtms/queue_my.py](https://github.com/qwerty200696/Introduction_to_Algorihtms/blob/master/queue_my.py)


## 链表（10.2，P131）

链表是一种物理存储单元上非连续、非顺序的存储结构，数据元素的逻辑顺序是通过链表中的指针链接次序实现的。链表由一系列结点（链表中每一个元素称为结点）组成，结点可以在运行时动态生成。

双向链表(`doubly linked list`)的每个结点包括两个部分：一个是存储数据元素的数据域，另一个是存储下一个(前一个)结点地址的指针域。 

未排序双向链表的Python实现代码：[Introduction_to_Algorihtms/list_my.py](https://github.com/qwerty200696/Introduction_to_Algorihtms/blob/master/list_my.py)

## 指针和对象的实现（10.3，P134）

当有些语言不支持指针和对象数据类型时，我们可以用数组和数组下标构造对象和指针。这种链表称为[静态链表](http://baike.baidu.com/link?url=GFeesiUYKbcXr0Q4vPTOK518GTn6z4DnzuBNxiplK80cT9bzyAVcqpX8G9Huw8yC)。

### 对象的多数组表示
用三个数组`next` `key` `prev` 分别表示链表的后继/数据/前驱。
多数组表示只能表示同构对象（所有对象有相同的属性）。而单数组表示可以表示异构对象（比如对象具有不同的长度）。

### 对象的单数组表示
用一个数组即可表示双链表，这种表示法比较灵活，因为它允许不同长度的对象存储于同一数组中。一般地我们考虑的数据结构多是由同构的元素构成，因此采用对象的多数组表示法足够满足我们的需求。

### 对象的分配与释放
把自由(`free`)对象保存在一个单链表中，称为自由表(`free list`)。

自由表只使用next数组，该数组只存储链表中的next指针。自由表的头存储在全局变量free中。

自由表的实现类似与栈：下一个被分配的对象就是最后被释放的对象（后进先出）。

## 有根树的表示（10.4，P137）
用链式结构表示有根树。

### 二叉树
二叉树`T`具有三个属性：`p`，`left`，`right`分别存放指向父节点、左孩子节点和右孩子节点的指针。
如果`x.p=NIL`，则`x`是根节点。属性`T.root`指向整棵树`T`的根节点。

更多关于二叉树的内容将在第12章中介绍。本次就暂不实现二叉树。

### 分支无限制的有根树
两种表示方法。一种是将`left`，`right`扩展为$child_1,\cdots,child_k$，这种方法的缺点是若`k`很大，但是多数节点只有少量的孩子，则会浪费大量存储空间。

第二种方法是左孩子右兄弟表示法(`left-child,right-sibling representation`)。每个节点除了父节点指针`p`，还有两个指针:
`x.left-child`表示节点`x`最左边的孩子节点；`x.right-sibling`表示右侧相邻的兄弟节点。


## 参考资料
1.算法导论 中文 第三版
2.[算法导论第十章基本数据结构](http://blog.csdn.net/z84616995z/article/details/19202773)