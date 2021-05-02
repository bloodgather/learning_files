#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	int b = 100;
	int a = 1;
	int num = 0;
	for (int i = 0; i <6; i++) {
		cin >> num;
		if (num % 2 == 0 && num < b && num > 0) {
			b = num;
		}
		else if (num % 2 == 1 && num > a && num < 100){
			a = num;
		}
	}
	cout << abs(a - b) << endl;
	return 0;
}