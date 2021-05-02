#include <iostream>
#include <cstring>
using namespace std;

int main() {
	char s1[80], s2[80], result;
	int i = 0;
	cin.getline(s1, 80);
	cin.getline(s2, 80);

	for (int j = 0; j < 80; j++)
	{
		if (s1[j] >= 'A' && s1[j] <= 'Z')
		{
			s1[j] = s1[j] + 32;
		}if (s2[j] >= 'A' && s2[j] <= 'Z')
		{
			s2[j] = s2[j] + 32;
		}
	}
	while (s1[i] != '\0' && (s1[i] == s2[i]))
	{
		i++;
	}
	if (s1[i] > s2[i])
	{
		result = '>';
	}
	else if (s1[i] < s2[i])
	{
		result = '<';
	}
	else
	{
		result = '=';
	}
	cout << result << endl;
	return 0;
}