#include <stdio.h>
#include <stdlib.h>

void swap(int *arr, int i, int j) {
	int tmp;

	tmp = arr[i];
	arr[i] = arr[j];
	arr[j] = tmp;
}

void merge(int *num_arr, int left, int mid, int right) {
	int l, r, k, i;
	int *sorted;
	l = left;
	r = mid + 1;
	i = 0;
	sorted = (int *)malloc(sizeof(int) * (right - left + 1));

	while (l <= mid && r <= right) {
		if (num_arr[l] <= num_arr[r])
			sorted[i++] = num_arr[l++];
		else
			sorted[i++] = num_arr[r++];
	}

	while (l <= mid)
		sorted[i++] = num_arr[l++];

	while (r <= right)
		sorted[i++] = num_arr[r++];

	for (i = 0; i < (right - left + 1); i++)
		num_arr[left + i] = sorted[i];
}


void merge_sort(int *num_arr, int left, int right) {
	int mid;

	if (left < right) {
		mid = (left + right) / 2;
		merge_sort(num_arr, left, mid);
		merge_sort(num_arr, mid+1, right);
		merge(num_arr, left, mid, right); //여기서 정렬
	}
}

int main() {
	int n;
	scanf("%d", &n);

	int *num_queue;
	num_queue = (int *)malloc(sizeof(int) * n);

	int i = 0;
	while (i < n) {
		scanf("%d", &num_queue[i]);
		merge_sort(num_queue, 0, i);
		printf("%d\n", num_queue[i/2]);
		i++;
	}
}
