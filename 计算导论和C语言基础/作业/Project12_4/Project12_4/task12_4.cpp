#include <iostream>
using namespace std;

int main() {
	int n1, n2;
	char s;
	cin >> n1 >> n2 >> s;

	if (s == '+')
	{
		cout << n1 + n2 << endl;
	}
	if (s == '-')
	{
		cout << n1 - n2 << endl;
	}
	if (s == '*')
	{
		cout << n1 * n2 << endl;
	}
	if (s == '/')
	{
		if (n2 != 0)
		{
			cout << n1 / n2 << endl;
		}
		else
		{
			cout << "Divided by zero!" << endl;
		}
	}
	else
	{
		cout << "Invalid operator!" << endl;
	}
	return 0;
}