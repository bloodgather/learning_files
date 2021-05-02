#include <iostream>
using namespace std;

int main() {
	int N, num[15000];
	while (true)
	{
		cin >> N;
		if (N == 0)
		{
			break;
		}
		for (int i = 0; i < N; i++)
		{
			cin >> num[i];			
		}
		int greater[15000];
		for (int i = 0; i < N; i++)
		{
			greater[i] = 0;
		}
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if (num[j] > num[i])
				{
					greater[i]++;
				}
			}
		}
		
		int result;
		if (N % 2 == 1)
		{
			for (int i = 0; i < N; i++)
			{
				if (greater[i] == N / 2) {
					result = num[i];
					
				}
						
			}
			cout << result << endl;
		}
		else if(N % 2 == 0)
		{
			int r1, r2;
			for (int i = 0; i < N; i++)
			{
					
				if (greater[i] == N / 2)
				{
					r1 = num[i];
				}if (greater[i] == N / 2 - 1)
				{
					r2 = num[i];
				}
			}
			cout << (r1 + r2) / 2 << endl;
			
				
		}
		
	}
	
	return 0;
}