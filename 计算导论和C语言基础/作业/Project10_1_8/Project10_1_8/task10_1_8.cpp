#include <iostream>
using namespace std;

int main() {
	int L, M;
	int dots[10001] = { 0 };
	int start, end;
	cin >> L >> M;
	for (int i = 0; i < M; i++)
	{
		cin >> start >> end;
		// ��ǿ�������
		for (int i = start; i <= end; i++)
		{
			dots[i] = 1;
		}
	}
	

	// ʣ�¶�����
	int left_trees = 0;
	for (int i = 0; i <= L; i++)
	{
		if (dots[i] == 0)
		{
			left_trees++;
		}
	}
	
	cout << left_trees << endl;
	return 0;
}