#include <stdio.h>
#include <stdlib.h>

int is_valid(int idx, int val, int *puzzle)
{
    int i = 0;

    while (i < idx)
    {
        if (puzzle[i] == val) {
            return 0;
        }
        if (val - puzzle[i] == idx - i || val - puzzle[i] == i - idx) {
            return 0;
        }
        i++;
    }
    return 1;
}

void solve_queens(int n, int idx, int *puzzle, int *cnt)
{
    if (idx == n) {
        *cnt = *cnt + 1;

    }
    int val = 0;
    while (val < n)
    {
        if (is_valid(idx, val, puzzle)) {
            puzzle[idx] = val;
            solve_queens(n, idx + 1, puzzle, cnt);
        }
        val++;
    }
}

int main(void)
{
    int n;
    scanf("%d", &n);
    int idx = 0;
    int cnt = 0;
    int *puzzle = (int *)malloc(sizeof(int) * n);

    solve_queens(n, idx, puzzle, &cnt);
    printf("%d", cnt);
    return 0;
}