#include <stdio.h>

int merge_sort(int d[], int tmp[], int l, int r)
{
	if (l == r)
		return 0;
	int k = (int)((l+r)/2);
	int a = merge_sort(d, tmp, l, k);
	int b = merge_sort(d, tmp, k+1, r);
	int p = l, p1 = l, p2 = k+1, q = 0;
	while (p1 <= k && p2 <= r) {
		if (d[p1] < d[p2]) {
			tmp[p++] = d[p1++];
		} else {
			tmp[p++] = d[p2++];
			q += k-p1+1;
		}
	}
	int i;
	if (p1 <= k) {
		for (i=p1; i<k+1; i++)
			d[r-k+i] = d[i];
	}
	for (i=l; i<p; i++)
		d[i] = tmp[i];

	return a + b + q;
}

int main()
{
	int n, k;
	scanf("%d%d", &n, &k);
	int d[n], tmp[n];

	int i,j,s;
	int max_r = -1, max_s = -1;
	for (i=1; i<=k; i++)
	{
		for (j=0; j<n; j++)
			scanf("%d", d+j);
		s = merge_sort(d, tmp, 0, n-1);
		if (s > max_s)
		{
			max_s = s;
			max_r = i;
		}
	}
	printf("%d\n", max_r);
	return 0;
}
