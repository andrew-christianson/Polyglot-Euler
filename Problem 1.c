#include <stdio.h>

int main() {
  int res = 0;

  for (int i = 0; i <= 1000; ++i) {
    ((i % 3 == 0) || (i % 5 == 0)) && (res += i);
  }

  printf("The answer to Euler Problem 1 is %i\n", res);

  return 1;
}
