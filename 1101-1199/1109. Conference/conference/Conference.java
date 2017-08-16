import java.io.*;
import java.util.*;

public class Conference implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try {
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int M = (int)in.nval;
			in.nextToken();
			int N = (int)in.nval;
			in.nextToken();	
			int K = (int)in.nval;
			
			int[] mMat = new int[M];
			int[] nMat = new int[N];
			boolean[] chk = new boolean[N];
			Arrays.fill(mMat, -1);
			Arrays.fill(nMat, -1);
			int counter=M+N;
			boolean[][] g = new boolean[M][N];
			for(int i=0; i<K; i++)
			{
				in.nextToken();
				int m = (int)in.nval;
				in.nextToken();
				int n = (int)in.nval;
				g[m-1][n-1] = true;
//				Ì°ÐÄ
				if(mMat[m-1]==-1&&nMat[n-1]==-1)
				{
					mMat[m-1]=n-1;
					nMat[n-1]=m-1;
					counter--;
				}
			}


			//ÐÙÑÀÀûËã·¨
			for(int i=0; i<M; i++)
			{
				if(mMat[i]==-1)
				{
					Arrays.fill(chk, false);
					if(dfs(i, g, mMat, nMat, chk))
						counter--;
				}
			}
			System.out.println(counter);
		} catch (Exception e) {
			// TODO: handle exception
		}

	}
	public boolean dfs(int k, boolean[][]g, int[]m, int[]n, boolean[]chk)
	{
		for(int i=0; i<n.length; i++)
		{
			if(g[k][i]&&!chk[i])
			{
				chk[i] = true;
				if(n[i]==-1 || dfs(n[i], g, m, n, chk))
				{
					m[k] = i;
					n[i] = k;
					return true;
				}
			}
		}
		return false;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Conference()).start();
	}

}
