#include <iostream>
#include<math.h>
using namespace std;

int main() {
	// 1. ����
	float n, x, y;
	float left;
	cin >> n >> x >> y;
	// 2. ����
	left = n - y / x;
	// 3. ���
	if (left >= 0) {
		cout << floor(left) << endl;
	}
	else {
		cout << 0 << endl;
	}
	
	return 0;
}