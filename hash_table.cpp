#include<iostream>
#include<cstring> // for memset

using namespace std;
 
#define Null -1
#define DELETED -2
/*
 * 算法导论习题11.4-1 开放寻址法实现散列表。
 * 顺便也实现了搜索与删除。
 * 
 * Linux下g++5.4.0编译通过。
 * 命令：
 *   $ g++ -o hash_table.out hash_table.cpp -std=c++11
 *   $ ./hash_table.out
 */
const int m = 11;  //槽位数量
const int c1 = 1;
const int c2 = 3;

void Print(int *T)
{
    int i;
    for(i = 0; i < m; i++)
        cout << T[i] << ' ';
    cout << endl;
}

int h(int k) {
    return k % m;
}

// 线性探查
int linear_probing(int key, int i) {
    return (key + i) % m;
}

//二次探查
int quadratic_probing(int key, int i) {
    return (key + c1 * i + c2 * i * i) % m;
}

//双重散列
int double_hashing(int key, int i) {
    return (key + i * (1 + key % (m - 1))) % m;
}

using PF = int (*) (int, int);   //函数指针
PF hash_functions[3] = {linear_probing, quadratic_probing, double_hashing};

// 判断探查的状态：当槽为空或者已到末尾时，为True
bool probe_state(int T[], int j) {
    return T[j] == Null || T[j] == DELETED || T[j] == 0;
}

int hash_insert(int T[], int key, PF hash_function) {
    int k = key;
    int i = 0;
    do
    {
        int j = hash_function(k, i);  //这里通过函数指针，可以在调用时选择线性、二次及双重探查。关于函数指针的简单介绍，可以查看http://wangwlj.com/2018/01/06/CPP_06/
        if (probe_state(T, j))
        {
            T[j] = k;
            return j;
        }
        else ++i;
    } while (i != m);

    cerr << "hash table overflow" << endl;
}

int hash_search(int T[], int k, PF hash_function) {
    int i = 0, j = 0;
    do
    {
        j = hash_function(k, i);  //这里可以替换成二次，双重探查。插入，查找，删除函数同时被替换  
        if (T[j] == k)
        {
            return j;
        }
        else ++i;
    } while (!probe_state(T, j));
    return Null;
}

void hash_delete(int T[], int k, PF hash_function)  
{  
    int j = hash_search(T, k, hash_function);  //首先先找到该关键字k  
    if (j != Null)  
    {  
       T[j] = DELETED;  //如果找到了，那么设置其为空。  
       cout << "关键字：" << k << " 删除成功！" << endl;  
    }  
    else cout << "待删除的数据不在表中！" << endl;  
}

int main() {
    int key[9] = {10, 22, 31, 4, 15, 28, 17, 88, 59};	
    static int T[11];
   
    for (int i = 0; i < 3; ++i) { 
        memset(T, 0, sizeof(T));  // 初始化T为全零
    	for (int j = 0; j < 9; ++j) {
            hash_insert(T, key[j], hash_functions[i]); 
        }
	    Print(T);
	    cout << "搜索关键字：88，返回结果：" << hash_search(T, 88, hash_functions[i]) << endl;
	    hash_delete(T, 88, hash_functions[i]);
	    cout << "删除 88 之后元素为：";
	    Print(T);
	    cout << endl;
    }
	return 0;
}
