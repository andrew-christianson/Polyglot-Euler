#include <stdio.h>

#ifndef MAX_VAL
#define MAX_VAL 4000000
#endif

int main(int argc, char const *argv[])
{
	int i_m1 = 1;
	int i_m2 = 0;
	int cur;
	int res = 0;
	
	do
	{
		cur = i_m1 + i_m2;
		i_m2 = i_m1;
		i_m1 = cur;
		((cur & 1) == 0) && (res += cur);
	} while (cur < MAX_VAL);

	printf("The answer to Euler Problem 2 is %i\n", res);

	return 0;

}