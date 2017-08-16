import java.io.*;

public class Fibonacci implements Runnable{

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//case 1:
		//0 1
		//case 2:
		//00 01 10
		//case 3:
		//000 001 010 100 101
		//=>Fibonacci
		new Thread(new Fibonacci()).start();
	}
	
	public void run()
	{
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int N = (int)in.nval;
			in.nextToken();
			int K = (int)in.nval;
			
			//generate the Fibonacci array
			int[] fbnc = new int[N+1];
			fbnc[0] = 1; fbnc[1] = 2;
			for(int i=2; i<=N; i++)
				fbnc[i] = fbnc[i-1]+fbnc[i-2];
			
			if(K>fbnc[N])
				System.out.print(-1);
			else
			{
				for(int i=0; i<N; i++)
				{
					if(K>fbnc[N-i-1])
					{
						System.out.print(1);
						K -= fbnc[N-i-1];
					}
					else System.out.print(0);
				}
			}
		}
		catch(IOException e)
		{System.out.print(e.toString());}
	}
}
