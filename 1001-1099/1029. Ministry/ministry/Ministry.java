import java.io.*;
public class Ministry implements Runnable {

	public void run() {
		// TODO Auto-generated method stub	
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int M = (int)in.nval;
			in.nextToken();
			int N = (int)in.nval;
			long[][] a = new long[M][N];
			short[][] b = new short[M][N];
			for(int i=0; i<M; i++)
				for(int j=0; j<N; j++)
				{
					in.nextToken();
					a[i][j] = (long)in.nval;
				}
			long[] c = new long[N];
			for(int i=0; i<M; i++)
			{
				c[0] += a[i][0]; 
				for(int j=1; j<N; j++)
				{
					if(c[j-1] < c[j])
					{
						c[j] = c[j-1]+a[i][j];
						b[i][j] = 1;
					}
					else
					{
						c[j] += a[i][j];
						for(int k=j; k>0; k--)
						{
							if(c[k]+a[i][k-1]<c[k-1])
							{
								c[k-1]=c[k]+a[i][k-1];
								b[i][k-1] = -1;
							}
							else break;
						}
					}
				}
			}
			long min=Long.MAX_VALUE;
			int n=-1;
			for(int i=0; i<N; i++)		
				if(min>c[i])
				{
					min = c[i];
					n = i;
				}
			print(b, M-1, n);
		}
		catch(IOException e)
		{e.printStackTrace();}
	}
	
	public void print(short[][] b, int m, int n)
	{
		if(m > 0)
		{
			if(b[m][n]==0)
				print(b, m-1, n);
			else
				print(b, m, n-b[m][n]);
		}
		System.out.print(n+1);
		System.out.print(" ");
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Ministry()).start();
	}

}
