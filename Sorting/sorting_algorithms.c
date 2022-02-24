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

int sorted[10];
void merge(int *list, int left, int mid, int right){
  int i, j, k, l;
  i = left;
  j = mid+1;
  k = left;

  while(i<=mid && j<=right){
    if(list[i]<=list[j])
      sorted[k++] = list[i++];
    else
      sorted[k++] = list[j++];
  }

  while (i <= mid)
	  sorted[k++] = list[i++];

  while (j <= right)
	  sorted[k++] = list[j++];

  for(l=left; l<=right; l++)
    list[l] = sorted[l];
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


void quick_sort(int *num_arr, int L, int R){
	int left = L, right = R;
	int pivot = num_arr[(L + R) / 2];

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
		if (L < right) //아직 끝까지 정렬하지 못함
			quick_sort(num_arr, L, right);
		if (left < R)
			quick_sort(num_arr, left, R);
	}
}


int main() {
	int n = 10;
	int *num_arr = (int *)malloc(sizeof(int) * 10);
	for (int i = 0; i < 10; i++){
		num_arr[i] = rand() % 100;
	}

	//selection_sort(num_arr, n);
	//insertion_sort(num_arr, n);
	//merge_sort(num_arr, 0, n-1);
	//bubble_sort(num_arr, n);
	quick_sort(num_arr, 0, n-1);

	for (int i = 0; i < n; i++)
		printf("%d ", num_arr[i]);
}
