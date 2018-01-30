
本文是《算法导论》第三章：函数的增长的学习笔记。
没有涉及到具体的算法。
主要内容有：
- 五种渐近记号的表示
- 常用的函数与标记

<!-- more-->
## 3.1 渐近记号
$\Theta、 \text{O}和\Omega $三种记号的图示：
![image](http://ws3.sinaimg.cn/large/c38a0784ly1fnz09knlnbj20l407vgmp.jpg)

### 先看第一幅图(a)——$\Theta$记号

若存在正常量$c_1,c_2,n_0$，使得对所有$n\geqslant n_0$，有$0\leqslant c_1g(n)\leqslant f(n) \leqslant c_2g(n)$，则$f(n)$属于集合$\Theta(g(n))$，
可以记为$f(n)\in \Theta(g(n))$，我们通常用$f(n)=\Theta(g(n))$表达相同的概念。

上述公式的含义：函数f(n)能“夹入”$c_1g(n)$和$c_2g(n)$之间。换句话说，对所有的$n\geqslant n_0$，函数$f(n)$在一个常量因子内等于$g(n)$，我们称$g(n)$是$f(n)$的一个渐近紧确界(asymptotically tight bound)。

实例：可以用上述的形式化定义来证明：$\frac{1}{2}n^2-3n =\Theta(n^2)$，以及$6n^3 \neq \Theta(n^2)$。

渐近正函数就是对足够大的n均为正的函数。

直觉上，一个渐近正函数的低阶项 在确定渐近确界时可以被忽略，因为对于大的n，它们是无足轻重的。

一般来说，对任意多项式$p(n)=\sum_{i=0}^d a_i n^i$，其中$a_i$为常量且$a_d>0$（最高阶的系数大于零），则有$p(n)=\Theta(n_d)$。

### 接着看图(b)——$\text{O}$记号

$\Theta$记号渐近地给出了一个函数的上界和下届。当只有一个*渐近上界*时，使用$\text{O}$记号。

$\text{O}(g(n))=\{f(n)：$存在正常量$c,n_0$，使得对所有$n\geqslant n_0$，有$0\leqslant  f(n) \leqslant cg(n)\}$

我们记$f(n)=\text{O}(g(n))$表示$f(n)$是集合$\text{O}(g(n))$的成员。注意$f(n)=\Theta(g(n))$蕴含了$f(n)=\text{O}(g(n))$，因为$\Theta$记号是一个比$\text{O}$记号更强的概念。

使用$\text{O}$记号，我们常常可以仅仅通过检查算法的总体结构来描述算法的运行时间。$\text{O}$记号描述上界，对插入排序算法的最坏情况运行时间的界$\text{O}(n^2)$也适合于该算法对每个输入的运行时间。该算法对每个输入的运行时间都有一个界，这就是综合性描述。

### 最后看图(c)——$\Omega$记号

正如$\text{O}$记号提供了渐近上界，$\Omega$记号提供了渐进下界。

$\Omega(g(n))=\{f(n)：$存在正常量$c,n_0$，使得对所有$n\geqslant n_0$，有$0\leqslant  cg(n) \leqslant f(n)\}$

于是，由此引出了定理3.1。

#### 定理 3.1

对任意两个函数$f(n)$和$g(n)$，我们有$f(n)=\Theta(g(n))$，当且仅当$f(n)=\text{O}(g(n))$且$f(n)=\Omega(g(n))$。

当一个算法的运行时间为$\Omega(g(n))$时，我们意指不管n是什么规模，只要n足够大，对那个输入的运行时间至少是$g(n)$的常数倍。

### 等式和不等式中的渐近记号

当渐近记号出现在某个公式中时，我们将其解释为代表某个我们不关注名称的匿名函数。

例如：$2n^2+3n+1 = 2n^2 +\Theta(n)$。

按这种方式使用渐记号可以帮助消除一个等式中无关紧要的细节与混乱。

例如：归并排序的最坏情况运行时间：
$$T(n) = 2T(n/2)+\Theta(n)$$
如果只对T(n)的渐近行为感兴趣，就没必要准确说明所以低阶项，它们都被理解为包含在由项$\Theta(n)$表示的匿名函数中。

在某些例子中，渐近记号出现在等式的左边，如：
$$2n^2+\Theta(n) = \Theta(n^2) $$

无论怎么选择等号左边的匿名函数，总有一种办法来选择等号右边的匿名函数使等式成立。

### $\text{o}$记号

$\text{o}$记号，非渐近紧确的上界。

$\text{o}(g(n))=\{f(n)：$对任意正常量$c>0$，存在正常量$n_0>0$，使得对所有$n\geqslant n_0$，有$0\leqslant  f(n) < cg(n)\}$。

$\text{O}$记号与$\text{o}$记号类似，主要的区别 是在$f(n)=\text{O}(g(n))$中，界$0\leqslant  f(n) \leqslant cg(n)$对某个常量$c>0$成立，但在$f(n)=\text{o}(g(n))$中，界$0\leqslant  f(n) < cg(n)$对所有常量$c>0$成立。

直观上，在$\text{o}$记号中，当n趋向于无穷时，函数$f(n)$相对于$g(n)$来说变得微不足道了，即：
$$\lim_{n\rightarrow \infty} \frac{f(n)}{g(n)} = 0$$

### $\omega$记号

非渐近紧确下界。

$\omega (g(n))=\{f(n)：$对任意正常量$c>0$，存在正常量$n_0>0$，使得对所有$n\geqslant n_0$，有$0\leqslant cg(n) <  f(n) \}$。

$$\lim_{n\rightarrow \infty} \frac{f(n)}{g(n)} = \infty $$

### 渐近运算的运算性质  
传递性、自反性、对称性与转置对称性：
![image](http://ws3.sinaimg.cn/large/c38a0784ly1fnz0arjrhhj20fk06uabg.jpg)
![image](http://ws3.sinaimg.cn/large/c38a0784ly1fnz0b29ajej20f503fq3f.jpg)
而且：两个函数f和g的渐近比较关系可与实数a与b之间的比较做类比： 

- f(n)=O(g(n)) 类似于a<= b 
- f(n)=Ω(g(n)) 类似于a>= b 
- f(n)=Θ(g(n)) 类似于a= b 
- f(n)=o(g(n)) 类似于a< b 
- f(n)=w(g(n)) 类似于a> b

三分性：虽然实数具有三分性，即对于任意两个实数a、b，下列三种情况必须有一种成立：$a<b$，$a=b$或$a>b$。但是不是所有函数都可以渐近比较。

## 3.2 标准记号与常用函数

### 单调性
单调递增/单调递减：包含等号；严格递增/严格递减：不包含等号。

### 向下取整与向上取整
x的向下取整：$\lfloor x \rfloor$；x的向上取整：$\lceil x \rceil$。

### 模运算
对任意整数a和正整数n，$a\ \text{mod}\ n$ 的值就是商a/n的余数。
$$a\ \text{mod}\ n = a-n\lfloor a/n\rfloor $$

若$(a\ \text{mod}\ n)=(b\ \text{mod}\ n)$，则记$a\equiv b(\text{mod}n)$
### 多项式
给定一个非负整数d，n的d次多项式$p(n)$：
$$p(n)=\sum_{i=0}^d a_i n^i$$
其中，$a_d \neq 0 $。

多项式为渐近正的当且仅当$a_d > 0 $。对于一个d次渐近正的多项式$p(n)$，有$p(n)=\Theta(n^d)$

若对于某个常量k，有$f(n)=\text{O}(n^k)$，则称函数$f(n)$是多项式有界的。

### 指数

对所有使得$a>1$的实常量a和b，有
$$\lim_{n\rightarrow \infty} \frac{n^b}{a^n} = 0$$
据此可得：
$$n^b = \text{o}(a^n)$$

### 对数
以2为底的自然数：
$$\text{lg}n = \text{log}_2n$$
自然对数：
$$\text{ln}n = \text{log}_en$$
取幂：
$$\text{lg}^kn = (\text{lg}n)^k$$
复合：
$$\text{lg}\text{lg}n =\text{lg} (\text{lg}n)$$

一个重要的记号约定：对数函数只适用于公式中的下一项，所以$\text{lg}n+k$意思是指$(\text{lg}n)+k$

对于$a>0,b>0,c>0$和n，有
$$a = b^{\text{log}_ba}$$
$$\text{log}_c(ab) = \text{log}_ca +\text{log}_cb$$
$$\text{log}_b(a^n) = n\text{log}_ba$$
$$\text{log}_ba =\frac{\text{log}_ca}{\text{log}_cb} $$
$$\text{log}_b(1/a) =- \text{log}_ba $$
$$\text{log}_ba =\frac{1}{\text{log}_ab} $$
$$a^{\text{log}_bc} = c^{\text{log}_ba}$$
其中，上述等式的对数底不为1。

对任意常量a，有
$$\text{log}^bn = \text{o}(n^a)$$
表示任意正的多项式函数都比任意多对数函数增长得快。

### 阶乘
$n!$，读作“n的阶乘”。其定义为对整数$n \geqslant 0$：
$$n! = \begin{cases}
1 & 若n=0\\
n\cdot (n-1)! & 若n>0
\end{cases}$$

阶乘函数的一个弱上界是$n! \leqslant n^n$，因为在阶乘中，n项的每项最多为n。

#### 斯特林(Stirling)近似公式
$$n!=\sqrt{2\pi n}(\frac{n}{e})^n(1+\Theta(\frac{1}{n})) $$

由上述公式可以证明：
$$n! = o(n^n)$$
$$n! = \omega(2^n)$$
$$\text{lg}n! = \Theta(n\text{lg}n)$$

### 多重函数
记号$f^{(i)}(n)$表示f(n)重复i次作用于一个初值n上。对非负整数i，我们递归地定义：
$$f^{(i)}(n)=\begin{cases}
n & 若i=0 \\
f(f^{(i-1)}(n)) & 若i>0
\end{cases}$$
### 多重对数函数
$\text{lg}^*n$表示多重对数，多重对数增长非常慢。

### 斐波那契数
斐波那契数的递归定义：
$$F_0 = 0$$
$$F_1 = 1$$
$$F_i = F_{i-1}+F_{i-2}, i \geqslant 2$$


