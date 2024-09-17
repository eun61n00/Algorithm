#include <stdio.h>
#include <stdlib.h>

check_build(int x, int y){
	
}

int main() {
	int n;
	scanf("%d", &n);

	int **profile;
	profile = (int **)malloc(sizeof(int *)*3);
	for (int i = 0; i < n; i++){
		int x, y;
		scanf("%d %d" &x, &y);
		profile[i][0] = x;
		profile[i][1] = y;
		check_buiild(x, y);
	}
}
