#include <iostream> 

#include <iomanip> 

using namespace std;



int main()

{

	int n;//nΪ�������˵���Ŀ 

	cin >> n;

	int stage1 = 0, stage2 = 0, stage3 = 0, stage4 = 0;

	for (int i = 0; i < n; i++)

	{

		int temp;//temp�洢����Ĳ��˵����� 

		cin >> temp;

		if (temp <= 18)

			stage1++;

		else if (temp <= 35)

			stage2++;

		else if (temp <= 60)

			stage3++;

		else if (temp > 60)

			stage4++;

	}

	double sum = (stage1 + stage2 + stage3 + stage4) / 100.0;

	//Ϊ����������������ȡ����������ѡȡdouble�� 

	cout << fixed << setprecision(2)

		<< "1-18: " << stage1 / sum << "%" << endl

		<< "19-35: " << stage2 / sum << "%" << endl

		<< "36-60: " << stage3 / sum << "%" << endl

		<< "60-: " << stage4 / sum << "%" << endl;



	return 0;
}