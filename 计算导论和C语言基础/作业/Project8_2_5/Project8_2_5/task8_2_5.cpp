#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	
	for (int i = 10; i < n + 1; i++)
	{
		int n10 = i / 10;
		int n1 = i % 10;
		int sum = n10 + n1;
		if (i % sum == 0)
		{
			cout << i << endl;
		}
	}
	return 0;
}