#include<iostream>
#include<stack>

using namespace std;

struct BST_Node
{
	int key;
	int data;
	BST_Node *left;
	BST_Node *right;
	BST_Node *p;

	BST_Node(int x):key(x),data(x),left(NULL),right(NULL),p(NULL){}  
};

class BST_Tree
{
private:
	BST_Node *root;
	void Transplant(BST_Node *u, BST_Node *v);
public:
	BST_Tree():root(NULL){}	                            //默认构造函数
	BST_Node *getRoot();                                //返回根节点
	//遍历操作
	void Preorder_Tree_Walk(BST_Node *x);               //先序遍历
	void Inorder_Tree_Walk(BST_Node *x);                //中序遍历
	void Postorder_Tree_Walk(BST_Node *x);              //后序遍历
	void Preorder_Iterative_Traverse(BST_Node *root);   //先序遍历的非递归实现
	void Inorder_Iterative_Traverse(BST_Node *root);    //中序遍历的非递归实现
	void Inorder_Iterative_Traverse_2(BST_Node *root);  //中序遍历的非递归实现--简洁
	//查找操作
	BST_Node *Iterative_Tree_Search(int k);             //迭代搜索
	BST_Node *Tree_Minimum(BST_Node *x);                //最小值
	BST_Node *Tree_Maximum(BST_Node *x);                //最大值
	BST_Node *Tree_Predecessor(BST_Node *x);            //前驱
	BST_Node *Tree_Successor(BST_Node *x);              //后继
	//插入与删除操作
	void Tree_Insert(BST_Node *z);                      //插入节点
	BST_Node *Tree_Delete(BST_Node *z);                 //删除节点
};

BST_Node* BST_Tree::getRoot()
{
    return root;
}

/*****12.1 遍历操作**********************************/
//递归的先序遍历：根在左右子树之前   
void BST_Tree::Preorder_Tree_Walk(BST_Node *x)    
{
    //x不是叶子结点
    if(x != NULL)
    {
        //访问当前结点
        cout << x->key << ' ';  // 可以用接口实现，比如现在想返回一个保存值的vector，而不是直接打印，岂不是要重写这个函数？
        //先序遍历当前结点的左子树
        Preorder_Tree_Walk(x->left);
        //先序遍历当前结点的右子树 
        Preorder_Tree_Walk(x->right);
    }
}
//递归的中序遍历：根在左右子树中间   
void BST_Tree::Inorder_Tree_Walk(BST_Node *x)    
{
    //x不是叶子结点
    if(x != NULL)
    {
        //中序遍历当前结点的左子树
        Inorder_Tree_Walk(x->left);
        //访问当前结点
        cout << x->key << ' ';
        //中序遍历当前结点的右子树
        Inorder_Tree_Walk(x->right);
    }
}
//递归的后序遍历：根在左右子树之后
void BST_Tree::Postorder_Tree_Walk(BST_Node *x)
{
    //x不是叶子结点
    if(x != NULL)
    {
        //后序遍历当前结点的左子树
        Postorder_Tree_Walk(x->left);
        //后序遍历当前结点的右子树
        Postorder_Tree_Walk(x->right);
        //访问当前结点
        cout << x->key << ' ';
    }
}

//先序遍历非递归过程  
void BST_Tree::Preorder_Iterative_Traverse(BST_Node *root)
{  //用C++STL——栈stack实现
    if (root == NULL) return;
    stack<BST_Node *>s;
    s.push(root);
    while (!s.empty()) {
        BST_Node *p = s.top();
        cout << p->key << " ";
        s.pop(); //出栈
        if (p->right != NULL)
        {
            s.push(p->right);
        }
        if (p->left != NULL)
        {
            s.push(p->left);
        }
    }
    cout << endl;
}
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
/*****12.2 查询操作**********************************/
//迭代版本的查找操作
BST_Node *BST_Tree::Iterative_Tree_Search(int k)
{
    BST_Node *x = root;
    while(x != NULL and k != x->key)
    {
        if(k < x->key)
            x = x->left;
        else
            x = x->right;
    }
    return x;
}
//递归地查找最小值
BST_Node *BST_Tree::Tree_Minimum(BST_Node *x)
{
    if(x->left != NULL) 
        return Tree_Minimum(x->left);
    else return x;
} 
//递归的查找最大值
BST_Node *BST_Tree::Tree_Maximum(BST_Node *x)
{
    if(x->right != NULL)
        return Tree_Maximum(x->right);
    else return x;
}
//查找中序遍历下x的前驱，即小于x的最大值    
BST_Node *BST_Tree::Tree_Predecessor(BST_Node *x)    
{
    //如果x的左子树非空
    if(x->left != NULL)
        //x的前驱是x的左子树的最大值
        return Tree_Maximum(x->left);
    //如果x的左子树为空且x有前驱y，那么y是x的最低祖先结点，且y的右儿子也是
    BST_Node *y = x->p;
    while(y != NULL && x == y->left)
    {
        x = y;
        y = y->p;
    }
    return y;
}
//查找中序遍历下x的后驱，即大于x的最小值
BST_Node *BST_Tree::Tree_Successor(BST_Node *x)
{
    //如果x的左子树非空
    if(x->right != NULL)
        //x的前驱是x的左子树的最大值
        return Tree_Minimum(x->right);
    //如果x的左子树为空且x有前驱y，那么y是x的最低祖先结点，且y的右儿子也是
    BST_Node *y = x->p; 
    while(y != NULL && x == y->right)
    { 
        x = y;
        y = y->p;
    }
    return y;
}/*****12.3 插入和删除操作**********************************/
//插入
void BST_Tree::Tree_Insert(BST_Node *z)
{
	BST_Node *x = getRoot(), *y = NULL;
	while(x != NULL)
	{
		y = x;
		if(z->key == x->key)
		{
			cout << "error:exist" << root->key << z->key << endl;
			return;
		}
		if(z->key < x->key)
			x = x->left;
		else
			x = x->right;
	}
	z->p = y;
	if(y == NULL){
		root = z;
	}
	else if(z->key < y->key)
		y->left = z;
	else y->right = z;
}

//删除
void BST_Tree::Transplant(BST_Node *u, BST_Node *v)
{
    if(u->p == NULL)
        root = v;
    else if(u == u->p->left)
        u->p->left = v;
    else
        u->p->right = v;
    if(v != NULL)
        v->p = u->p;
}
//删除
BST_Node *BST_Tree::Tree_Delete(BST_Node *z)
{
    BST_Node *y;
    if(z->left == NULL)
        Transplant(z, z->right);
    else if(z->right == NULL)
        Transplant(z, z->left);
    else 
    {
        y = Tree_Minimum(z->right);
        if(y->p != z)
        {
            Transplant(y, y->right);
            y->right = z->right;
            y->right->p = y;
        }
        Transplant(z, y);
        y->left = z->left;
        y->left->p = y;
    }
    return y;
}

 
int main() {
    //const int k[11] = {2, 3, 4, 6, 7, 9, 13, 15, 17, 18, 20};
    const int k[8] = {12, 5, 18, 2, 9, 15, 17, 19};  //图12.3
    BST_Tree *t = new BST_Tree(); 
    BST_Node *b;
    for (int i = 0; i < 8; ++i) {
        b = new BST_Node(k[i]); //动态创建，内存地址不同
        t->Tree_Insert(b);
    }
    cout << "root is: " << t->getRoot()->key << endl << "前序遍历：";
    t->Preorder_Tree_Walk(t->getRoot());
    cout << endl << "中序遍历：";
    t->Inorder_Tree_Walk(t->getRoot());
    cout << endl << "后序遍历：";
    t->Postorder_Tree_Walk(t->getRoot());
    cout << endl << "前序遍历（迭代）：";
    t->Preorder_Iterative_Traverse(t->getRoot());
    cout << "中序遍历（迭代）：";
    t->Inorder_Iterative_Traverse(t->getRoot());
    cout << "中序遍历2（迭代）：";
    t->Inorder_Iterative_Traverse_2(t->getRoot());
	
    cout << "最小值：" << t->Tree_Minimum(t->getRoot())->key << endl
        << "最小值：" << t->Tree_Maximum(t->getRoot())->key << endl;
    BST_Node * s = t->Iterative_Tree_Search(9);
    cout << "查找元素：" << s->key << "，其前驱为：" << t->Tree_Predecessor(s)->key 
         << "，后继为：" << t->Tree_Successor(s)->key << endl;
	
    t->Tree_Delete(s);
    cout << "删除元素：" << s->key <<" 后：";
    t->Inorder_Tree_Walk(t->getRoot());
    
    cout << endl;
    return 0;
}
