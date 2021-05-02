#include <iostream>
using namespace std;

int main() {
	char s[80];
	int n_a, n_e, n_i, n_o, n_u;
	n_a = n_e = n_i = n_o = n_u = 0;
	cin.getline(s, 80);
	
	for (int i = 0; s[i] != '\0'; i++)
	{
		if (s[i] == 'a')
		{
			n_a++;
			continue;
		}if (s[i] == 'e')
		{
			n_e++;
			continue;
		}if (s[i] == 'i')
		{
			n_i++;
			continue;
		}if (s[i] == 'o')
		{
			n_o++;
			continue;
		}if (s[i] == 'u')
		{
			n_u++;
			continue;
		}
	}
	cout << n_a << " ";
	cout << n_e << " ";
	cout << n_i << " ";
	cout << n_o << " ";
	cout << n_u << endl;
	return 0;
}