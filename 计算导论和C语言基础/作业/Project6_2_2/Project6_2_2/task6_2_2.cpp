#include <iostream>
using namespace std;

int main() {
	// 1. ����
	float h, r;
	float bucket;
	const float Pi = 3.14159;
	cin >> h >> r;
	// 2. ����
	bucket = 20000 / Pi / r / r / h;
	// 3. ���
	cout << ceil(bucket) << endl;
	return 0;
}