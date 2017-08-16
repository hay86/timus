import java.io.*;
public class Cryptography implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			boolean[] nature = new boolean[163842];
			int[] prime = new int[15000];
			int p = 0;
			for(int i=2; i<163842; i++)
			{
				if(!nature[i])
				{
					prime[p++] = i;
					//p++;
					//System.out.println(p+" "+i);
					
					int t = 163841/i;
					for(int j=2; j<=t; j++)
						nature[j*i] = true;
				}
			}
			
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int n = (int)in.nval;
			for(int i=0; i<n; i++)
			{
				in.nextToken();
				System.out.println(prime[(int)in.nval-1]);
			}
				
		}
		catch(IOException e)
		{e.printStackTrace();}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Cryptography()).start();
	}

}
