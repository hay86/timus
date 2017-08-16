import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Timus_1099 {
	static int[] match;
	static boolean[][] g;
	static int[] prev;
	static int[] root;
	static boolean[] inq;
	static int[] que;
	static int qsize;
	static int qcur;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		g = new boolean[n+1][n+1];
		while(true) {
			String line = br.readLine();
			if (line == null || line.trim().equals(""))
				break;
			String[] p = line.split(" ");
			int a = Integer.parseInt(p[0]);
			int b = Integer.parseInt(p[1]);
			g[a][b] = g[b][a] = true;
		}
		
		match = new int[n+1];
		Arrays.fill(match, -1);
		prev = new int[n+1];
		root = new int[n+1];
		inq = new boolean[n+1];
		que = new int[n+1];
		
		int total = 0;
		for (int i=1; i<n+1; i++) {
			if (match[i] == -1 && augment(i, n))
				total += 2;
		}
		
		System.out.println(total);
		for (int i=1; i<n+1; i++)
			if (i < match[i])
				System.out.println(i + " " + match[i]);
	}
	
	static boolean augment(int s, int n) {
		Arrays.fill(prev, -1);
		Arrays.fill(que, -1);
		Arrays.fill(inq, false);
		for (int i=0; i<n+1; i++)
			root[i] = i;
		que[0] = s;
		inq[s] = true;
		qsize = 1;
		qcur = 0;
		
		while (qcur < qsize) {
			int u = que[qcur++];
			for (int v=1; v<n+1; v++) {
				if (!g[u][v] || root[u] == root[v] || match[u] == v)
					continue;
				if (v == s || (match[v] != -1 && prev[match[v]] != -1))
					contract(u, v, n);
				else if (prev[v] == -1) {
					prev[v] = u;
					if (match[v] != -1) {
						que[qsize++] = match[v];
						inq[match[v]] = true;
					}
					else {
						u = v;
						while (u != -1) {
							v = prev[u];
							int tmp = match[v];
							match[u] = v;
							match[v] = u;
							u = tmp;
						}
						return true;
					}
				}
			}
		}
		return false;
	}
	
	static void contract(int u, int v, int n) {
		int ancestor = findAncestor(u, v, n);
		boolean[] inFlower = new boolean[n+1];
		Arrays.fill(inFlower, false);
		reset(u, ancestor, inFlower);
		reset(v, ancestor, inFlower);
		if (root[u] != ancestor)
			prev[u] = v;
		if (root[v] != ancestor)
			prev[v] = u;
		for (int i=0; i<n+1; i++) {
			if (inFlower[i]) {
				root[i] = ancestor;
				if (!inq[i]) {
					que[qsize++] = i;
					inq[i] = true;
				}
			}
		}
	}
	
	static int findAncestor(int u, int v, int n) {
		boolean[] inPath = new boolean[n+1];
		Arrays.fill(inPath, false);
		while (true) {
			u = root[u];
			inPath[u] = true;
			if (match[u] == -1)
				break;
			u = prev[match[u]];
		}
		while (true) {
			v = root[v];
			if (inPath[v])
				return v;
			v = prev[match[v]];
		}
	}
	
	static void reset(int u, int a, boolean[] inFlower) {
		while (u != a) {
			int v = match[u];
			inFlower[root[u]] = true;
			inFlower[root[v]] = true;
			v = prev[v];
			if (root[v] != a)
				prev[v] = match[u];
			u = v;
		}
	}
}
