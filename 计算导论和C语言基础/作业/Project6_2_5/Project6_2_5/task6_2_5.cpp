#include <iostream>
using namespace std;

int main() {
	// 1. ����
	int n;
	cin >> n;
	// 2. ����
	int a = n / 100;
	int b = n / 10 % 10;
	int c = n % 10;
	// 3. ���
	cout << a << endl;
	cout << b << endl;
	cout << c << endl;
	return 0;
}