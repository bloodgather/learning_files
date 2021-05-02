#include <iostream>
#include<math.h>
using namespace std;

int main() {
	// 1. ÊäÈë
	float n, x, y;
	float left;
	cin >> n >> x >> y;
	// 2. ¼ÆËã
	left = n - y / x;
	// 3. Êä³ö
	if (left >= 0) {
		cout << floor(left) << endl;
	}
	else {
		cout << 0 << endl;
	}
	
	return 0;
}