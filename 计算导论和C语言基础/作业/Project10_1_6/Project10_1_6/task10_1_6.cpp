#include <iostream>
using namespace std;

int main() {
	int n, m;
	int num[100];
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		cin >> num[i];
	}
	for (int i = 0; i < n; i++)
	{
		if (i <= n - m - 1)
		{
			num[i + 11] = num[i];
		}
		else
		{
			num[i - n + m] = num[i];
		}
	}
	for (int i = m; i < n; i++)
	{
		num[i] = num[i + n - m];
	}
	for (int i = 0; i < n; i++)
	{
		cout << num[i] << " ";
	}
	 
	return 0;
}