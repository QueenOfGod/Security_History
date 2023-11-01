#include <iostream>
#include <sstream>

using namespace std;

int main() {
	long long Rand_Val = 0x0, Cmp_Val = 0x7d1c4b0a, key = 0x0;

	cin >> hex >> Rand_Val;

	key = Rand_Val ^ Cmp_Val;

	cout <<  key;
}