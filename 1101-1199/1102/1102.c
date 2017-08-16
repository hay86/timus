#include <stdio.h>
#include <string.h>

int main()
{
	char line[10000000];
	gets(line);
	while (gets(line))
	{
		int i = strlen(line)-1;
		while (line[i] == '\r' || line[i] == '\n')
			i --;
		
		while (i >= 0)
		{
			if (line[i] == 'e')
			{
				if (i >= 2 && line[i-1] == 'n' && line[i-2] == 'o')
					i -= 3;
				else 
					break;
			}
			else if (line[i] == 'n')
			{
				if (i >= 1 && line[i-1] == 'i')
					i -= 2;
				else if (i >= 4 && line[i-1] == 'o' && line[i-2] == 't' && line[i-3] == 'u' && line[i-4] == 'p')
					i -= 5;
				else
					break;
			}
			else if (line[i] == 't')
			{
				if (i >= 2 && line[i-1] == 'u')
				{
					if (line[i-2] == 'o')
						i -= 3;
					else if (line[i-2] == 'p')
					{
						if (i >= 4 && line[i-3] == 'n' && line[i-4] == 'i')
							i -= 5;
						else if (i >= 5 && line[i-3] == 't' && line[i-4] == 'u' && line[i-5] == 'o')
							i -= 6;
						else
							break;
					}
					else
						break;
				}
				else
					break;
			}		
			else
				break;
		}

		if (i < 0)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
