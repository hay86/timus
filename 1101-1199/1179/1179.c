#include <stdio.h>

int main()
{
	int a[37];
	int b[37];
	int c, i;
	for (i=2; i<=36; i++) 
	{
		a[i] = 0;
		b[i] = 0;
	}
	while ((c = getchar()) != EOF)
	{
		if ((int)'0' <= c && c <= (int)'9')
			c -= (int)'0';
		else if ((int)'A' <= c && c <= (int)'Z')
			c -= (int)'A' - 10;
		else
			c = 9999;
		for (i=2; i<=36; i++)
		{
			if (c < i)
			{
				if (a[i] == 0)
				{
					b[i] ++;
					a[i] = 1;
				}
			}
			else
			{
				if (a[i] == 1)
					a[i] = 0;
			}
		}
	}
	int maxbase = 0, maxnum = 0;
	for (i=2; i<=36; i++)
	{
		if (b[i] > maxnum)
		{
			maxbase = i;
			maxnum = b[i];
		}
	}
	printf("%d %d", maxbase, maxnum);
}
