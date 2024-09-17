#include <stdio.h>
#include <stdlib.h>

int	bin_tile(int n)
{
	int *dp;
	int i = 3;
	int res;

	dp = (int *)malloc(sizeof(int) * (n + 1));
	dp[0] = 0;
	dp[1] = 1;
	dp[2] = 2;
	while (i <= n)
	{
		dp[i] = dp[i - 1] + dp[i - 2];
		i++;
	}
	res = dp[n];
	free(dp);

	return res;

}

int main(void)
{
	int n;

	scanf("%d", &n);
	printf("%d", bin_tile(n)%15746);
}