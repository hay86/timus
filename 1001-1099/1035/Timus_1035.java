import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Timus_1035 {
	
	static int n, m;
	static int[] degree, father, rank, thread;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] p = br.readLine().split(" ");
		n = Integer.parseInt(p[0]);
		m = Integer.parseInt(p[1]);
		
		int size = (n+1)*(m+1);
		degree = new int[size];
		father = new int[size];
		rank = new int[size];
		thread = new int[size];
		
		Arrays.fill(degree, 0);
		Arrays.fill(rank, 0);
		Arrays.fill(thread, -1);
		for (int i=0; i<size; i++)
			father[i] = i;
		
		int[] inc = new int[]{1, -1};
		for (int k: inc) {
			for (int i=0; i<n; i++) {
				String chs = br.readLine();
				for (int j=0; j<m; j++) {
					if (chs.charAt(j) == '\\' || chs.charAt(j) == 'X') {
						int a = id(i, j);
						int b = id(i+1, j+1);
						update_degree(a, b, k);
						update_union(a, b);
					}
					if (chs.charAt(j) == '/' || chs.charAt(j) == 'X') {
						int a = id(i+1, j);
						int b = id(i, j+1);
						update_degree(a, b, k);
						update_union(a, b);
					}
				}
			}
		}
		
		for (int i=0; i<size; i++) {
			int j = root(i);
			if (i != j) {
				if (thread[j] == -1)
					thread[j] = Math.abs(degree[j]);
				thread[j] += Math.abs(degree[i]);
			}
		}

		int total = 0;
		for (int i=0; i<size; i++) {
			if (thread[i] == 0)
				total += 1;
			else if (thread[i] > 0)
				total += thread[i]/2;
		}
		System.out.println(total);
	}
	
	static int root(int x) {
		if (father[x] == x)
			return x;
		else {
			father[x] = root(father[x]);
			return father[x];
		}
	}

	static void update_union(int a, int b) {
		int x = root(a);
		int y = root(b);
		if (rank[x] > rank[y])
			father[y] = x;
		else {
			father[x] = y;
			if (rank[x] == rank[y])
				rank[y] += 1;
		}
	}

	static void update_degree(int a, int b, int inc) {
		degree[a] += inc;
		degree[b] += inc;
	}

	static int id(int i, int j) {
		return i*(m+1)+j;
	}
}
