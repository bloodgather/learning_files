#include <iostream>
using namespace std;

int main() {
	// 1. ÊäÈë
	float h, r;
	float bucket;
	const float Pi = 3.14159;
	cin >> h >> r;
	// 2. ¼ÆËã
	bucket = 20000 / Pi / r / r / h;
	// 3. Êä³ö
	cout << ceil(bucket) << endl;
	return 0;
}