#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef INFILE_NAME
#define INFILE_NAME "Problem 22 Line-Orient.txt"
#endif

// From http://stackoverflow.com/q/1733881
void free_array(int **a, int m) {
  int i;
  for (i = 0; i < m; ++i) {
    free(a[i]);
  }
  free(a);
}

int count_lines(FILE *fp) {
  int ch;
  int lines = 0;

  while (EOF != (ch = getc(fp))) {
    // printf("%i\n", ch);
    if (ch == '\n') {
      lines++;
    }
  }
  rewind(fp);

  return lines;
}

void zero_array(char *arr) {
  int size = sizeof(arr) / sizeof(arr[0]);
  for (int i = 0; i < size; ++i) {
    arr[i] = 0;
  }
}

int len_name(char *name) {
  int len = 20;
  int real_len = 0;
  for (int i = 0; i < len; ++i) {
    // printf("%s\n", &name[i]);
    if (name[i] > 0) {
      real_len++;
    }
  }
  return real_len;
}

char **name_array(FILE *fp) {
  int n_names = count_lines(fp);
  int counter = 0;
  char name[20];
  char **names = malloc(n_names * sizeof(char *));

  zero_array(name);

  while (EOF != fscanf(fp, "%s", name)) {
    // printf("%s\n", name);
    names[counter] = (char *)malloc(len_name(name) * sizeof(char));
    for (int i = 0; i < len_name(name); ++i) {
      names[counter][i] = name[i];
    }
    counter++;
  }
  rewind(fp);
  return names;
}

int _strcmp(const void *p1, const void *p2) {
  printf("%i\n", strcmp(p1, p2));
  return strcmp(p1, p2);
}

int main(int argc, char const *argv[]) {
  FILE *finfile;
  char **n_array;
  int n_names = 120;

  finfile = fopen(INFILE_NAME, "r");
  n_names = count_lines(finfile);
  n_array = name_array(finfile);
  printf("%i\n", n_names);
  qsort(*n_array, n_names, sizeof(char *), _strcmp);
  for (int i = 0; i < n_names; ++i) {
    printf("%s\n", n_array[i]);
  }
  return 0;
}
