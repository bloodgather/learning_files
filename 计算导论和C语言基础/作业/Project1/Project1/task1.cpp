#include <iostream>
using namespace std;

int main() {
	int n, a[1000];
	cin >> n;	// 输入n个数
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	// 冒泡
	for (int i = 0; i < n; i++) {
		for (int j = 1; j < n - i; j++) {
			if (a[j - 1] > a[j]) {
				int temp = a[j];
				a[j] = a[j - 1];
				a[j - 1] = temp;
			}
		}
	}
	// 输出整个数组
	for (int i = 0; i < n; i++) {
		cout << a[i] << endl;
	}
	return 0;
}