#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <cstring>
using namespace std;

int main() {
    int t, i;
    char in[30], ch[4];
    int last = 1;
    int used[30001];
    memset(used, -1, sizeof(used));
    vector<int> unused;
    deque<int> access;

    while (gets(in))
    {
        sscanf(in, "%d %s %d", &t, ch, &i);

        while(!access.empty() && access[0]+600 <= t)
        {
            int tt = access.front();
            access.pop_front();
            int ii = access.front();
            access.pop_front();
            if (used[ii]+600 <= t)
            {
                unused.push_back(ii);
                push_heap(unused.begin(), unused.end(), greater<int>());
            }
        }

        if (ch[0]=='+')
        {
            if (unused.empty())
            {
                i = last;
                last += 1;
            }
            else
            {
                pop_heap(unused.begin(), unused.end(), greater<int>());
                i = unused.back();
                unused.pop_back();
            }
            used[i] = t;
            access.push_back(t);
            access.push_back(i);
            printf("%d\n", i);
        }
        else if (ch[0]=='.')
        {
        	if (used[i] < 0 || used[i]+600 <= t)
        	{
        	    puts("-");
        	}
		    else
		    {
		        used[i] = t;
		        access.push_back(t);
                access.push_back(i);
                puts("+");
		    }
        }
    }

    return 0;
}