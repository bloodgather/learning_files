#include <iostream>
#include <iomanip>
#include<cmath>

using namespace std;

int main() {
	int n;
	double dis[100];
	double x[100], y[100];
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> x[i] >> y[i];
	}

	double max = 0;
	// 分别求两点间距离
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			dis[i] = sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]));
			// 求最大距离
			if (dis[i] > max)
			{
				max = dis[i];
			}
		}
	}

	cout << fixed << setprecision(4) << max << endl;
	return 0;
}