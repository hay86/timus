#include <stdio.h>

int n, m, i, j, k, x, size;
int f1 = -1, f2;

int dfs(int i, int a[])
{
	a[i] = 0;
	int b[] = {-100000, -100000, -100000, -100000};
	if (i%n != 0 && a[i-1] == 1)
		b[0] = dfs(i-1, a);
	if (i%n != n-1 && a[i+1] == 1)
		b[1] = dfs(i+1, a);
	if (i >= n && a[i-n] == 1)
		b[2] = dfs(i-n, a);
	if (i <= size-n-1 && a[i+n] == 1)
		b[3] = dfs(i+n, a);
	for (j=0; j<3; j++)
		for (k=j+1; k<4; k++)
			if (b[j]+b[k]+2 > f1)
				f1 = b[j]+b[k]+2;
	int ret = -1;
	for (j=0; j<4; j++)
		if (b[j] > ret)
			ret = b[j];
	return ret+1;
}

int main()
{
	scanf("%d %d", &n, &m);
	
	size = n*m;
	int a[size];
	char ch;
	
	for (i=0; i<m; i++)
	{
		for (j=0; j<n; j++)
		{
			scanf("%c", &ch);
			while (ch != '.' && ch != '#')
				scanf("%c", &ch);
			if (ch == '.')
			{
				x = i*n+j;
				a[x] = 1;
			}
			else
				a[i*n+j] = 0;
		}
	}

	f2 = dfs(x, a);
	printf("%d", (f1 > f2) ? f1 : f2);
	return 0;
}
