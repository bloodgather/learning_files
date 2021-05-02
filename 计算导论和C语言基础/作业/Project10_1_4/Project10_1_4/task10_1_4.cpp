#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int n, m;
	int matrix[5][5];
	int temp[1][5];
	for (int i = 0; i < 5; i++)
	{		
		for (int j = 0; j < 5; j++)
		{
			cin >> matrix[i][j];
		}
	}
	cin >> n >> m;
	if (n < 5 && m < 5 && n >= 0 && m >= 0)
	{
		for (int i = 0; i < 5; i++)
		{
			temp[0][i] = matrix[n][i];
			matrix[n][i] = matrix[m][i];
			matrix[m][i] = temp[0][i];
		}
		for (int i = 0; i < 5; i++)
		{
			for (int j = 0; j < 5; j++)
			{
				cout << setw(4) << matrix[i][j];
				
			}
			cout << endl;
		}
		
	}
	else
	{
		cout << "error" << endl;
	}
	return 0;
}