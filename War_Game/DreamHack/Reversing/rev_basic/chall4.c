#include <iostream>

using namespace std;

int main()
{
	// 28,
	// 첫번째 인덱스를 >> 4한 값,
	// 두번째 인덱스를 << 4한 값을 F0과 and연산
	// 첫번째, 두번째 인덱스를 or연산

	char arr[256] = {0,};
	int sad[28] = {0x24, 0x27, 0x13, 0xC6, 0xC6, 0x13, 0x16, 0xE6, 0x47, 0xF5, 0x26, 0x96, 0x47, 0xF5, 0x46, 0x27,
		0x13, 0x26, 0x26, 0xC6, 0x56, 0xF5, 0xC3, 0xC3, 0xF5, 0xE3, 0xE3};
	int x = 0, c = 0;


	for(int i = 0; i < 28; i++)
	{
		for(int a = 33; a < 127; a++)
		{
			if(((a >> 4) | ((a << 4) & 0xF0)) == sad[i])
			{
				arr[i] = a;
				break;
			}
		}
	}


	cout << arr << endl;

	return 0;
}
