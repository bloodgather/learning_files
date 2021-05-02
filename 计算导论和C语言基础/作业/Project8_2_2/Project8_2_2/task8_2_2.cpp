#include <iostream>
using namespace std;

int main() {
	int n, meter[100];
	float s1, s2;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> meter[i];
	}
	for (int i = 0; i < n; i++)
	{
		s1 = 50 + meter[i] / 3.0;
		s2 = meter[i] / 1.2;
		if (s1 < s2)
		{
			cout << "Bike" << endl;
		}
		else if (s1 > s2)
		{
			cout << "Walk" << endl;
		}
		else
		{
			cout << "All" << endl;
		}
	}
	return 0;
}