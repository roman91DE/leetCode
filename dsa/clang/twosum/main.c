#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) { return (*(int *)a - *(int *)b); }

struct Solution {
  int fst;
  int scnd;
};

int twosum(int nums[], int len, int target, struct Solution buffer[]) {
  qsort(nums, len, sizeof(int), compare);

  int i = 0, j = len - 1, counter = 0;
  int current_sum;
  while (i < j) {
    current_sum = nums[i] + nums[j];
    if (current_sum == target) {
      buffer[counter].fst = nums[i];
      buffer[counter].scnd = nums[j];
      counter++;
      i++;
      j--;
    } else if (current_sum < target) {
      i++;
    } else {
      j--;
    }
  }
  return counter;
}

int main(int argc, char *argv[]) {

  printf("Two-Sum!\n");
  int test[] = {3, 3};
  size_t len = sizeof(test) / sizeof(test[0]);
  int target = 6;
  struct Solution *buffer =
      (struct Solution *)malloc(100 * sizeof(struct Solution));

  int ct = twosum(test, len, target, buffer);
  for (int i = 0; i < ct; i++) {
    printf("Pair %d: (%d, %d)\n", i + 1, buffer[i].fst, buffer[i].scnd);
  }

  return EXIT_SUCCESS;
}
