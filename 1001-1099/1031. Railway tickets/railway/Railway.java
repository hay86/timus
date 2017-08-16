import java.io.*;
public class Railway implements Runnable {

	public void run() {
		// TODO Auto-generated method stub

		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			int[] L = new int[3];
			for(int i=0; i<3; i++)
			{
				in.nextToken();
				L[i] = (int)in.nval;
			}
			int[] C = new int[3];
			for(int i=0; i<3; i++)
			{
				in.nextToken();
				C[i] = (int)in.nval;
			}
			in.nextToken();
			int N = (int)in.nval;
			in.nextToken();
			int n = (int)in.nval-1;
			in.nextToken();
			int m = (int)in.nval-1;
			
			if(n>m)
			{
				int temp = n;
				n = m;
				m = temp;
			}
			
			int[] l = new int[N];
			for(int i=1; i<N; i++)
			{
				in.nextToken();
				l[i] = (int)in.nval;
				//System.out.println(l[i]);
			}
			
			int[] c = new int[m-n+1];
			
			for(int i=1; i<=m-n; i++)
			{
				c[i] = Integer.MAX_VALUE;
				for(int j=i-1; j>=0; j--)
				{
					int len = l[i+n]-l[j+n];
					int cost;
					//System.out.println(len);
					if(len<=L[0])
						cost = C[0]+c[j];
					else if(len<=L[1])
						cost = C[1]+c[j];
					else if(len<=L[2])
						cost = C[2]+c[j];
					else break;
					
					if(c[i]>cost)
						c[i] = cost;
				}
			}
			System.out.println(c[m-n]);
		}
		catch(IOException e)
		{e.printStackTrace();}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Railway()).start();
	}

}
