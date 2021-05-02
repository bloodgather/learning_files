#include <iostream>
using namespace std;

int main() {
	int n, k, num[1000];
	bool flag = false;
	cin >> n >> k;
	for (int i = 0; i < n; i++)
	{
		cin >> num[i];
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = i + 1; j < n; j++)
		{
			int sum = num[i] + num[j];
			if (sum == k)
			{
				flag = true;
				break;
			}
		}
	}
	if (flag == false)
	{
		cout << "no" << endl;
	}
	else
	{
		cout << "yes" << endl;
	}
	return 0;
}