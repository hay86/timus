import java.io.*;
public class Buttons implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int k = (int)Math.sqrt(in.nval);
			boolean[] a = new boolean[k+1];
			long res = 0;
			if((long)in.nval%2==0)
				res = (long)in.nval/2-1;
			if(res <2)
				res = (long)in.nval-1;
			for(int i=3; i<=k; i++)
			{
				if(!a[i])
				{
					if((long)in.nval%i==0)
					{
						res = i-1; 
						break;
					}
					else 
						for(int j=1; j*i<=k; j++)
							a[i*j]=true;
					
				}
			}
			System.out.println(res);
		}
		catch(IOException e)
		{e.printStackTrace();}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Buttons()).start();
	}

}
