#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	int n100 = n / 100;
	int n50 = (n - 100*n100) / 50;
	int n20 = (n - 100*n100 - 50*n50) / 20;
	int n10 = (n - 100 * n100 - 50 * n50 - 20 * n20) / 10;
	int n5 = (n - 100 * n100 - 50 * n50 - 20 * n20 - 10 * n10) / 5;
	int n1 = n - 100 * n100 - 50 * n50 - 20 * n20 - 10 * n10 - 5 * n5;
	cout << n100 << endl;
	cout << n50 << endl;
	cout << n20 << endl;
	cout << n10 << endl;
	cout << n5 << endl;
	cout << n1 << endl;
	return 0;
}