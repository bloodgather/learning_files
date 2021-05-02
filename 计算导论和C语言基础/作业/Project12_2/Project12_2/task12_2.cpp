#include <iostream>
using namespace std;

int main() {
	int n;
	while (cin >> n)
	{
		if (n % 3 == 0 && n % 5 == 0 && n % 7 == 0)
		{
			cout << "3" << " ";
			cout << "5" << " ";
			cout << "7" << endl;
		}
		if (n % 3 == 0 && n % 5 == 0 && n % 7 != 0)
		{
			cout << "3" << " ";
			cout << "5" << endl;
			
		}
		if (n % 3 == 0 && n % 5 != 0 && n % 7 == 0)
		{
			cout << "3" << " ";
			
			cout << "7" << endl;
		}
		if (n % 3 != 0 && n % 5 == 0 && n % 7 == 0)
		{
			
			cout << "5" << " ";
			cout << "7" << endl;
		}
		if (n % 3 != 0 && n % 5 != 0 && n % 7 == 0)
		{
			
			cout << "7" << endl;
		}
		if (n % 3 != 0 && n % 5 == 0 && n % 7 != 0)
		{
			
			cout << "5" << endl;
			
		}
		if (n % 3 == 0 && n % 5 != 0 && n % 7 != 0)
		{
			cout << "3" << endl;
			
		}
		if (n % 3 != 0 && n % 5 != 0 && n % 7 != 0)
		{
			cout << 'n' << endl;
			
		}
	}
	return 0;
}