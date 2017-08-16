#include <stdio.h>

int n, m, k = 0;

void dfs(int i, int a[][n], int b[])
{
	int j;
	for (j=0; j<n; j++)
		if (i != j && a[i][j] == 0)
			{ a[i][j] = 1; dfs(j, a, b); }
	b[k++] = i;
}

int main()
{
	int i, j;
	scanf("%d %d", &n, &m);
	
	int a[n][n];
	int b[n*n];

	for (i=0; i<n; i++)
		for (j=0; j<n; j++)
			scanf("%d", &a[i][j]);
	
	dfs(m-1, a, b);
	
	for (i=k-1; i>0; i--)
		printf("%d %d\n", b[i]+1, b[i-1]+1);
			
	return 0;
}
