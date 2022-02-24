#include <stdio.h>
#include <stdlib.h>

void merge(int *num_arr, int left, int mid, int right){
    int i, j, k;
    i = left;
    j = mid + 1;
    k = 0;
    int *sorted = (int *)malloc(sizeof(int) * (right - left + 1));
    
    while(i<= mid && j<=right){
        if (num_arr[i] <= num_arr[j])
            sorted[k++] = num_arr[i++];
        else
            sorted[k++] = num_arr[j++];
    }

    while (i <= mid)
        sorted[k++] = num_arr[i++];

    while (j <= right)
        sorted[k++] = num_arr[j++];

    k = 0;
    for (int a = left; a <= right; a++) {
        num_arr[a] = sorted[k++];
    }
}

void merge_sort(int *num_arr, int left, int right){

    int mid;

    if (left < right) {
        mid = (left + right) / 2;
        merge_sort(num_arr, left, mid);
        merge_sort(num_arr, mid+1, right);
        merge(num_arr, left, mid, right);
    }
}

int main() {
    int n;
	scanf("%d", &n);
	int *num_arr= (int *)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++)
		scanf("%d", &num_arr[i]);
	
	merge_sort(num_arr, 0, n-1);

	for (int i = 0; i < n; i++)
		printf("%d\n", num_arr[i]);
}