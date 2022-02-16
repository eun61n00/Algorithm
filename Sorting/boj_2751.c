#include <stdio.h>
#include <stdlib.h>

void swap(int *arr, int i, int j){
	int tmp;

	tmp = arr[i];
	arr[i] = arr[j];
	arr[j] = tmp;
}

void selection_sort(int *num_arr, int arr_len){
	int min_idx;

	for (int idx = 0; idx < arr_len; idx++)
	{
		min_idx = idx;
		for (int i = idx; i < arr_len; i++)
		{
			if (num_arr[i] <= num_arr[min_idx])
				min_idx = i;
		}
		swap(num_arr, idx, min_idx);
	}
}

void bubble_sort(int *num_arr, int arr_len){
	int j;
	while (arr_len > 0)
	{
		j = 0;
		while (j < arr_len - 1)
		{
			if (num_arr[j] > num_arr[j + 1])
				swap(num_arr, j, j+1);
			j++;
		}
		arr_len--;
	}
}

void insertion_sort(int *num_arr, int arr_len){

	int i, j, key;

	if (arr_len == 1)
		return;

	for (i = 1; i <= arr_len; i++){
		key = num_arr[i];
		for (j = i-1; j >= 0 && num_arr[j]>key; j--){
			num_arr[j + 1] = num_arr[j];
		}
		num_arr[j + 1] = key;
	}
}

void quick_sort(int *num_arr, int L, int R){
	int left = L, right = R;
	int pivot = num_arr[(L + R) / 2];
	int tmp;

	while (left <= right)
	{
		while (num_arr[left] < pivot)
			left++;
		while (num_arr[right] > pivot)
			right--;
		if (left <= right)
		{
			swap(num_arr, left, right);
			left++;
			right--;
		}
		if (L < right)
			quick_sort(num_arr, L, right);
		if (left < R)
			quick_sort(num_arr, left, R);
	}
}

void merge_sort(int *num_arr){

}


int main() {
	int n = 10;
	int num_arr[10] = {7,3,1,6,9,4,2,5,8,0};
	//scanf("%d", &n);
	//int *num_arr= (int *)malloc(sizeof(int) * n);

	//for (int i = 0; i < n; i++)
	//	scanf("%d", &num_arr[i]);
	
	//selection_sort(num_arr, n);
	insertion_sort(num_arr, n);
	//bubble_sort(num_arr, n);
	//quick_sort(num_arr, 0, n-1);

	for (int i = 0; i < n; i++)
		printf("%d ", num_arr[i]);
}
