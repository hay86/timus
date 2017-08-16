import java.io.*;
public class Permutations implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int n = (int)in.nval;
			int[] a = new int [n];
			for(int i=0; i<n; i++)
			{
				in.nextToken();
				a[i] = (int)in.nval-1;
			}
			long res = 1;
			for(int i=0; i<n; i++)
			{
				int c = 1;
				int t = i;
				while(a[t]!=i)
				{
					t = a[t];
					c++;
				}
				if(res>c)
					res = res*c/gcd(res, c);
				else res = res*c/gcd(c, res);
			}
			System.out.println(res);
		}
		catch(IOException e)
		{e.printStackTrace();}
	}
	public long gcd(long a, long b)
	{
		long c = a%b;
		if(c == 0)
			return b;
		while(c != 0)
		{
			a = b;
			b = c;
			c = a%b;
		}
		return b;
		
		
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Permutations()).start();
	}

}
