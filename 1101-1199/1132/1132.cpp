// https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm
#include <cstdlib>
#include <iostream>
using namespace std;

// calculate a^b (mod p)
int pow_mod(int a, int b, int p){
	a %= p;
	int ret = 1;
	while (b){
		if (b&1) ret = (ret*a)%p;
		a = (a*a)%p;
		b>>=1;
	}
	return ret;
}

int solve(int a, int p){
	int q = p-1, s = 0;
	while (q%2 == 0){
		s++;
		q>>=1;
	}
	if (s==1) return pow_mod(a, (p+1)/4, p);
	int z;
	while (1){
		z = 1 + rand()%(p-1);
		if (pow_mod(z, (p-1)/2, p) != 1) break;
	}
	int c = pow_mod(z, q, p);
	int r = pow_mod(a, (q+1)/2, p);
	int t = pow_mod(a, q, p);
	int m = s, b, i;
	while (1){
		if (t%p == 1) break;
		for (i=1; i<m; i++)
			if (pow_mod(t, 1<<i, p) == 1)
				break;
		b = pow_mod(c, 1<<(m-i-1), p);
		r = (r*b)%p;
		c = (b*b)%p;
		t = (t*c)%p;
		m = i;
	}
	return r;
}

int main(){
	int k, a, n, r1, r2;
	cin >> k;
	while(k--){
		cin >> a >> n;
		a %= n;
		if (n == 2){
			if (a==1)
				cout << "1" << endl;
			else
				cout << "No root" << endl;
			continue;
		}
		if (pow_mod(a, (n-1)/2, n) != 1){
			cout << "No root" << endl;
			continue;
		}
		r1 = solve(a, n);
		r2 = n-r1;
		if (r1 == r2)
			cout << r1 << endl;
		else if (r1 < r2)
			cout << r1 << " " << r2 << endl;
		else
			cout << r2 << " " << r1 << endl;
	}
}


