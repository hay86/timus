/*
 * KM_Algo.cpp
 * Created by Kaifeng Xu on 2010-06-30
 */

#include <stdio.h>
#include <string.h>

#define min(x,y) x<=y?x:y
#define MAX_INT 999999999

int n = 4; //input size

int data[150][150]= {{62, 41, 86, 94},
					{73, 58, 11, 12},
					{69, 93, 89, 88},
					{81, 40, 69, 13}}; // input weight

// to ensure x[i]+y[j] >= data[i][j]
int x[150];
int y[150];

int slack[150]; // slcak on array y, the smallest is d
int result[150]; // linked idx of array x
bool xstate[150];
bool ystate[150];


// find augmenting path
bool find(int a){
	xstate[a] = true;
	for(int j=0; j<n; j++){
		if(x[a]+y[j]==data[a][j] && !ystate[j]){
			//printf("%d %d %d\n", x[a], y[j], result[j]);
			ystate[j] = true;
			slack[j] = MAX_INT;
			if(result[j]==-1 || find(result[j])){
				result[j] = a;
				return true;
			}
		}
		else if(x[a]+y[j] > data[a][j])
			slack[j] = min(slack[j], x[a]+y[j]-data[a][j]);
	}
	return false;
}

/* utility */
void arrayCopy(int n, bool det[], const bool res[]){
	for(int i=0; i<n; i++)
		det[i] = res[i];
}

void arrayFill(int n, int det[], int val){
	for(int i=0; i<n; i++)
		det[i] = val;
}

void arrayFill(int n, bool det[], bool val){
	for(int i=0; i<n; i++)
		det[i] = val;
}

/* get input */
void input(){
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			scanf("%d", &data[i][j]);
		}
	}
}

/* main */
int main(){

	input();

	// init x & y
	arrayFill(n, y, 0);
	for(int i=0; i<n; i++){
		int max = 0;
		for(int j=0; j<n; j++)
			if(data[i][j]>max)
				max = data[i][j];
		x[i] = max;
	}

	// km algorithm
	while(true){
		int success = 0;
		int mind = MAX_INT;
		bool min_xstate[150], min_ystate[150];
		arrayFill(n, result, -1);
		for(int i=0; i<n; i++){
			arrayFill(n, xstate, false);
			arrayFill(n, ystate, false);
			arrayFill(n, slack, MAX_INT);
			if(find(i))
				success ++;
			else{
				for(int j=0; j<n; j++)
					if(mind > slack[j]){
						mind = slack[j];
						arrayCopy(n, min_xstate, xstate);
						arrayCopy(n, min_ystate, ystate);
						
					}
			}
		}

		if(success == n)
			break;
		else{
			for(int i=0; i<n; i++){
				if(min_xstate[i])
					x[i] -= mind;
				if(min_ystate[i])
					y[i] += mind;
			}
		}
	}

	// output
	int sum = 0;
	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
			if(result[j] != i)
				sum += data[i][j];
	printf("%d\n", sum);

	//getchar();
	return 0;
}