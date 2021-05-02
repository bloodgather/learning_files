#include <iostream>
using namespace std;

int main() {
	// 1. 输入
	int n;
	int id[100];
	double rate[100];

	cin >> n;
	for (int i = 0; i < n; i++) {
		int initial, final;
		cin >> id[i] >> initial >> final;
		rate[i] = (double)final / initial;
	}
	// 2. rate排序（冒泡降序）
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n - i - 1; j++) {
			if (rate[j + 1] > rate[j]) {
				int tempId = id[j];
				id[j] = id[j + 1];
				id[j + 1] = tempId;
				double tempRate = rate[j];
				rate[j] = rate[j + 1];
				rate[j + 1] = tempRate;
			}
		}
	}
	// 3. 找差别最大的组
	double maxDiff = 0;
	int maxDiffIndex = 0;
	for (int i = 0; i < n - 1; i++) {
		double diff = rate[i] - rate[i + 1];
		if (maxDiff < diff) {
			maxDiff = diff;
			maxDiffIndex = i;
		}
	}
	// 4. 输出
	cout << maxDiffIndex + 1 << endl;
	for (int i = maxDiffIndex; i >= 0; i--) {
		cout << id[i] << endl;
	}
	cout << n - maxDiffIndex - 1 << endl;
	for (int i = n - 1; i >= maxDiffIndex + 1; i--) {
		cout << id[i] << endl;
	}
	return 0;
}