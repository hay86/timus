import java.io.*;
public class Multiple implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int N = (int)in.nval;
			int[] a = new int[N];
			int[] b = new int[N];
			for(int i=0; i<N; i++)
				b[i] = -1;
			int remainder = 0;
			for(int i=0; i<N; i++)
			{
				in.nextToken();
				a[i] = (int)in.nval;
				remainder = (remainder+a[i])%N;
				
				
				if(remainder == 0)
				{
					System.out.println(i+1);
					for(int j=0; j<=i; j++)
						System.out.println(a[j]);
					return;
				}
				else if(b[remainder]!=-1)
				{
					System.out.println(i-b[remainder]);
					for(int j=b[remainder]+1; j<=i; j++)
						System.out.println(a[j]);
					return;
				}
				else
					b[remainder] = i;
						
			//	for(int j=0; j<N; j++)
			//		System.out.print(b[j]+" ");
			//	System.out.println(remainder);
				
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
		new Thread(new Multiple()).start();
	}

}
