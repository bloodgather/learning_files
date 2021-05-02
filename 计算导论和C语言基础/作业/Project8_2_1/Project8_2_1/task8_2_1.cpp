#include <iostream>
using namespace std;

int main() {
	int a, n, sum = 0;
	cin >> a;
	for (int i = 0; i < 5; i++)
	{
		cin >> n;
		if (n < a)
		{
			sum += n;
		}
	}
	cout << sum << endl;
	return 0;
}