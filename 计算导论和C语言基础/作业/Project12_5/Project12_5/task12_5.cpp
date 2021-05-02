#include<iostream>
#include<string.h>

using namespace std;
int main()
{
	char str[20], substr[10];

	while (cin >> str >> substr)
	{
		int temp1 = 0, temp2 = 0, k1 = 0, k2 = 0, max = 0;
		for (int i = 0; str[i] != '\0'; i++)
		{
			if (str[i] > max)
			{
				max = str[i];
				temp1 = i;
			}
		}
		k1 = strlen(str);
		k2 = strlen(substr);

		for (int i = k1; i < k1 + k2; i++)
		{
			str[i] = substr[i - k1];
		}
		for (int i = k1 - 1; i > temp1; i--)
		{
			for (int j = 0; j < k2; j++)
			{
				temp2 = str[i + j];
				str[i + j] = str[i + j + 1];
				str[i + j + 1] = temp2;
			}
		}
		for (int i = 0; i < k1 + k2; i++)
		{
			cout << str[i];
		}
		cout << endl;
	}
	return 0;

}

