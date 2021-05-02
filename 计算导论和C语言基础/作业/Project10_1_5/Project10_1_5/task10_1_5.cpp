#include <iostream>
using namespace std;

int main() {
	int N, sum = 0;
	int ct[100][100];
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> ct[i][j];
		}
	}
	for (int i = 1; i < N - 1; i++)
	{
		for (int j = 1; j < N - 1; j++)
		{
			int num = ct[i][j] + 50;
			if (num <= ct[i-1][j] && num <= ct[i+1][j] && num <= ct[i][j-1]
				&& num <= ct[i][j+1])
			{
				sum++;
			}
		}
	}
	cout << sum << endl;
	return 0;
}