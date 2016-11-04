#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#ifndef P_IDX
#define P_IDX 10001
#endif 
int isprime(int n, int * p_arr);

int isprime(int n, int * p_arr){
    int i = 0;

    // if ((n & 1) == 0)
    // {
    //     return 0;
    // }

    do
    {
        if (n % p_arr[i] == 0)
        {
            return 0;
        }

        i++;

    } while (p_arr[i] != 0 && p_arr[i] <= sqrt(n));

    return 1;
}

int main(int argc, char const *argv[])
{
    int * p_arr = malloc(P_IDX * sizeof(int));
    int candidate = 3;
    int p_idx = 1;

    p_arr[0] = 2;
    for (int i = 1; i < P_IDX; ++i)
    {
        p_arr[i] = 0;
    }
    do
    {
        if (isprime(candidate, p_arr))
        {
            // printf("%i\n", candidate);
            p_arr[p_idx] = candidate;
            p_idx++;
        }
        candidate += 2;
    } while (p_arr[P_IDX-1] == 0);

    printf("The answer to Euler Problem 7 is %i\n", p_arr[P_IDX-1]);

    free(p_arr);
    return 0;

}