import java.io.*;
import java.util.*;
public class Tree implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int n = (int)in.nval;
			in.nextToken();
			int m = (int)in.nval;
			int[][]a = new int[m+1][n+1];
			int[][]b = new int[n+1][4];
			a[1][1] = -1;
			for(int i=0; i<n-1; i++)
			{
				in.nextToken();
				int x = (int)in.nval;
				in.nextToken();
				int y = (int)in.nval;
				in.nextToken();
				if(a[1][y]!=0)
				{
					int temp = x;
					x = y;
					y = temp;
				}

				if(b[x][0]==0)
					{b[x][0]=y; b[x][1]=(int)in.nval;}
				else
					{b[x][2]=y; b[x][3]=(int)in.nval;}
				if(a[1][x]<(int)in.nval)
					a[1][x] = (int)in.nval;
				a[1][y] = -1;
			}
			
			
			for(int i=2; i<=m; i++)
				for(int j=1; j<=n; j++)
					for(int k=0; k<=i; k++)
					{
						int r = k;
						int l = i-k;
						int v = 0;
						if(l!=0)
							v += b[j][1]+a[l-1][b[j][0]];
						if(r!=0)
							v += b[j][3]+a[r-1][b[j][2]];
						//System.out.println(i+" "+j+" "+v);
						if(a[i][j]<v)
							a[i][j] = v;
						
					}
			System.out.println(a[m][1]);
		
		}
		catch(IOException e)
		{e.printStackTrace();}

	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Tree()).start();
	}

}
