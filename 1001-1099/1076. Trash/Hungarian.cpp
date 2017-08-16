Hungarian.cpp : �������̨Ӧ�ó������ڵ㡣

#include <stdio.h>
#include <string.h>

int n1, n2, m, ans;
int result[101]; //��¼V2�еĵ�ƥ��ĵ�ı��
bool state [101]; //��¼V2�е�ÿ�����Ƿ�������
bool data[101][101];//�ڽӾ��� true�����б�����
void init()
{
	int t1, t2;
	memset(data, 0, sizeof(data));
	memset(result, 0, sizeof(result));
	ans = 0;
	scanf("%d%d%d", &n1, &n2, &m);
	for (int i = 1; i <= m; i++)
	{
		scanf("%d%d", &t1, &t2);
		data[t1][t2] = true;
	}
	return;
}
bool find(int a)
{
	for (int i = 1; i <= n2; i++)
	{
		if (data[a][i] == 1 && !state[i]) //����ڵ�i��a���ڲ���δ�����ҹ�
		{
			state[i] = true; //���iΪ�Ѳ��ҹ�
			if (result[i] == 0 //���iδ��ǰһ��ƥ��M��
				|| find(result[i])) //i��ƥ��M�У����Ǵ���i���ڵĽڵ��������������·
			{
				result[i] = a; //��¼���ҳɹ���¼
				return true; //���ز��ҳɹ�
			}
		}
	}
	return false;
}

int main()
{
	init();
	for (int i = 1; i <= n1; i++)
	{
		memset(state, 0, sizeof(state)); //����ϴ�����ʱ�ı��
		if (find(i)) 
			ans++; //�ӽڵ�i������չ
	}
	printf("%d\n", ans);
	for (int i = 0; i < n1; i++)
		printf("%d %d\n", result[i], i);
	getchar();
	getchar();
	return 0;
}