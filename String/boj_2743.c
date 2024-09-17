#include <stdio.h>

int main(void)
{
	char word[101];
	int str_len;

	str_len = 0;
	scanf("%s", word);
	while (word[str_len]) {
		str_len++;
	}
	printf("%d", str_len);
}