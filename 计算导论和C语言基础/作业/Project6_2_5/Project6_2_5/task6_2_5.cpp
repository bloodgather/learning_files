#include <iostream>
using namespace std;

int main() {
	// 1. ÊäÈë
	int n;
	cin >> n;
	// 2. ·ÖÀë
	int a = n / 100;
	int b = n / 10 % 10;
	int c = n % 10;
	// 3. Êä³ö
	cout << a << endl;
	cout << b << endl;
	cout << c << endl;
	return 0;
}