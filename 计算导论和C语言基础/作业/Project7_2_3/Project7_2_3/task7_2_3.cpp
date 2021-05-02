#include <iostream>
using namespace std;

int main() {
	int n, k, number[100];
	cin >> n;
	cin >> k;
	for (int i = 0; i < n; i++)
	{
		cin >> number[i];
	}
	int greater[100];
	for (int i = 0; i < n; i++)
	{
		greater[i] = 0;
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (number[j] > number[i])
			{
				greater[i]++;
			}
		}	
	}
	for (int i = 0; i < n; i++)
	{
		if (greater[i] == k - 1)
		{
			cout << number[i] << endl;
		}
	}
	return 0;
}