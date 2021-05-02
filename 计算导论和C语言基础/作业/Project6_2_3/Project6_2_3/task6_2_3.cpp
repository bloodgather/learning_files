#include <iostream>
using namespace std;

int main() {
	// 1. ÊäÈë
	int n;
	int grades[100];
	int max = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> grades[i];
	}
	for (int i = 0; i < n; i++) {
		if (grades[i] > max) {
			max = grades[i];
		}
	}
	// 2. Êä³ö
	cout << max << endl;
	return 0;
}