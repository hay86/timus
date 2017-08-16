import java.io.*;
public class Square implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int n = (int)in.nval;
			int [] a = new int[n+1];
			int m = (int)Math.sqrt(n);
			for(int i=1; i<=m; i++)
				a[i*i] = 1;
			if(a[n]!=0)
			{
				System.out.println(a[n]);
				return;
			}
			for(int i=2; i<n+1; i++)
			{
				if(a[i] == 0)
				{
					a[i] = Integer.MAX_VALUE;
					int k = (int)Math.sqrt(i);
					for(int j=k; j>0; j--)
					{
						if(a[j*j]+a[i-j*j]<a[i])
							a[i] = a[j*j]+a[i-j*j];
					}
				}
			}
			System.out.println(a[n]);
		}
		catch(IOException e)
		{e.printStackTrace();}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Square()).start();
	}

}
