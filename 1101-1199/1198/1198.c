#include <stdio.h>
#include <string.h>

int n;
short m[2000][2000];
short v[2000];
short v2[2000];
int visit;

void dfs(int i)
{
	v[i] = 1;
	v2[i] = 1;
	visit ++;
	for (int j=0; j<n; j++)
		if (m[i][j] && !v[j])
			dfs(j);
}

void rdfs(int i)
{
	v[i] = 1;
	for (int j=0; j<n; j++)
		if (m[j][i] && !v[j])
			rdfs(j);
}

int rdfs_once(int i)
{
	v2[i] = 1;
	for (int j=0; j<n; j++)
		if (m[j][i] && !v2[j])
			return rdfs_once(j);
	return i;
}

int main()
{
	scanf("%d", &n);
	memset(m, 0, sizeof(m));

	char b[65535];
	int t, x = -1, i = 0, j = 0;
	while ((t = fread(b, 1, 65535, stdin)) > 0)
	{
		for (j=0; j<t; j++)
		{
			if (b[j] < '0')
			{
				if (x != -1)
				{
					if (x == 0) i++; 
					else m[i][x-1] = 1;
					x = -1;
				}
			}
			else
			{
				if (x == -1) x = b[j] - 48;
				else x = (x<<1) + (x<<3) + b[j] - 48;
			}
		}
	}

	memset(v2, 0, sizeof(v2));
	int root = -1, start = -1;
	
	while (1)
	{
		while (++start < n && v2[start]);
		if (start == n)
			break;

		root  = rdfs_once(start);
		memset(v, 0, sizeof(v));
		visit = 0;
		dfs(root);

		if (visit == n)
			break;
	}
	if (start == n)
	{
		printf("0\n");
	}
	else
	{
		memset(v, 0, sizeof(v));
		rdfs(root);

		for (int i=0; i<n; i++)
			if (v[i]) printf("%d ", i+1);
		
		printf("0\n");
	}
}
