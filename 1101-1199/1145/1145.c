#include <stdio.h>

int n, m, i, j, k, l, size;

void bfs(int i, int t[])
{
	int q1[size], q2[size];
	q1[0] = i;
	q2[0] = 0;

	int s=0, e=1;
	t[i] = 0;
	int x = 0;
	while (s < e)
	{
		j = q1[s];
		l = q2[s];
		s++;
		if (j%n != 0 && t[j-1] == 1)
		{
			t[j-1] = 0;
			q1[e] = j-1;
			q2[e] = l+1;
			e++;
		}
		if (j%n != n-1 && t[j+1] == 1)
		{
			t[j+1] = 0;
			q1[e] = j+1;
			q2[e] = l+1;
			e++;
		}
		if (j >= n && t[j-n] == 1)
		{
			t[j-n] = 0;
			q1[e] = j-n;
			q2[e] = l+1;
			e++;
		}
		if (j <= size-n-1 && t[j+n] == 1)
		{
			t[j+n] = 0;
			q1[e] = j+n;
			q2[e] = l+1;
			e++;
		}
	}
}

int main()
{
	scanf("%d %d", &n, &m);
	
	size = n*m;
	int a[size], b[size];
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
				k = i*n+j;
				a[k] = 1;
				b[k] = 1;
			}
			else
			{
				a[i*n+j] = 0;
				b[i*n+j] = 0;
			}	
		}
	}
	
	bfs(k, a);
	int f1 = l;
	bfs(j, b);
	int f2 = l;
	printf("%d", (f1 > f2) ? f1 : f2);
	return 0;
}
