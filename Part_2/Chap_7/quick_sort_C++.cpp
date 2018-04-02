#include <iostream>
#include <vector>

using namespace std;

/*
 * 快速排序C++实现。g++编译通过。
 */

int Partition(vector<int> &v, int start, int end) {
    int k = start - 1;
    for (int i = start; i < end; ++i) {
        if (v[i] < v[end]) {
            k++;
            if (k != i) {
                swap(v[k], v[i]);
            }
        } 
    }
    ++k;
    swap(v[k], v[end]);
    return k;
}

void QuickSort(vector<int> &v, int start, int end) {
    if (start == end)
        return;
    int index = Partition(v, start, end);
    cout << index << endl;
    if (index > start) {
        QuickSort(v, start, index - 1);
    }
    if (index < end) {
        QuickSort(v, index + 1, end);
    }
}

int main () {
    vector <int> vi = {8, 5, 1, 0, 3, 4, 7, 2, 9, 6};
    QuickSort(vi, 0, vi.size() - 1);
    for (int i = 0; i < (int)vi.size(); ++i) {
        cout << vi[i] << " ";
    }
    cout << endl;
    return 0;
}
