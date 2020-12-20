#include <iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
#define N 10010
int n,m;
vector<int>ed[N];
bool vis[N][N];
int pa[100010],t;
void dfs(int u){   
     int i;
    for(i = 0 ;i < (int)ed[u].size() ; i++){
        int v = ed[u][i];
        if(!vis[u][v]){
            vis[u][v] = 1;
            dfs(v);
        }
    }
    t++;
    pa[t] = u;    
    return ;
}
int main(){
    int i,j,u,v;
    scanf("%d",&n);
    int sum=0;
    for(i = 1; i <= n ; i++){
        scanf("%d",&m);
        sum+=m;
        scanf("%d",&u);
        for(j = 1 ; j <= m ; j++)
        {
            scanf("%d",&v);
            ed[u].push_back(v);
            u = v;
        }
    }
    dfs(1);
    if(sum!=t-1)
        printf("0\n");
    else{
    printf("%d\n",t-1);
    for(i = t; i > 1 ; i--)
    printf("%d ",pa[i]);
    printf("%d\n",pa[1]);
    }
    return 0;
}
