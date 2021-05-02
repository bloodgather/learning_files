#include <iostream>
using namespace std;

int main() {
	int N, K;
	int year;
	
	while (cin >> N >> K)	// 不知道有多少行
	{
		float house = 200.0;
		for ( year = 1; year < 21; year++)
		{
			
			if (house <= N * year)
			{
				cout << year << endl;
				
				break;
			}
			house *= (1 + K / 100.0);
		}
		if (year == 21)
		{
			cout << "Impossible" << endl;
			
		}
	}
	return 0;
}