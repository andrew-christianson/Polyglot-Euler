#include <stdio.h>
#include <math.h>


#ifndef N
// N=600851475143
#endif

int isprime(long n){
	if (n & 1){
		return 1;
	} 
	for (long i = 3; i < sqrt(n); ++i)
	{
		if (n % i == 0){
			return 0;
		} 
	}
	return 1;
}


int main(int argc, char const *argv[])
{
	long max_factor = 0;
	long N=600851475143;

	for (long i = 3; i < sqrt(N); ++i)
	{
		if (N % i == 0){
			if (isprime(i)){
				max_factor = i;
			} else if (isprime(N/i)){
				max_factor = N/i;
			}
		}
	}
	printf("The answer to Euler Problem 3 is %lu", max_factor);
}