#include <stdio.h>

int main()
{
	int N, K;
	int i, j, k;
	scanf("%d%d", &N, &K);
	
	int a[N];
	for (i=0; i<N; i++)
		scanf("%d", a+i);
	
	int m[N][N], p[K][N];
	for (i=0; i<N; i++)
	{
		int w = 0, b = 0;
		for (j=i; j<N; j++)
		{
			if (a[j] == 0) w++;
			else b++;
			m[i][j] = w*b;
			if (i == 0) p[i][j] = m[i][j];
			else if (i < K) p[i][j] = 1000000;
		}
	}

	for (i=1; i<K; i++)
		for (j=i; j<N; j++)
			for (k=j; k>=i; k--)
				if (p[i-1][k-1] + m[k][j] < p[i][j])
					p[i][j] = p[i-1][k-1] + m[k][j];

	printf("%d", p[K-1][N-1]);
	return 0;
}
