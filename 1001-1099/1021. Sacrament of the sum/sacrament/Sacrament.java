import java.io.*;
public class Sacrament implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int n = (int)in.nval;
			int[] N = new int[n];
			for(int i=0; i<n; i++)
			{
				in.nextToken();
				N[i] = (int)in.nval;
			}
			in.nextToken();
			int m = (int)in.nval;
			int[] M = new int[m];
			for(int i=0; i<m; i++)
			{
				in.nextToken();
				M[i] = (int)in.nval;
			}
			
			int p=0, q=0;
			while(p<n && q<m)
			{
				if(N[p]+M[q]>10000)
					q++;
				else if(N[p]+M[q]<10000)
					p++;
				else break;
			}
			if(p<n && q<m)
				System.out.println("YES");
			else System.out.println("NO");
		}
		catch(IOException e)
		{e.printStackTrace();}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Sacrament()).start();
	}

}
