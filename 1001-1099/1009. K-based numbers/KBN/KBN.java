import java.io.*;

public class KBN implements Runnable{

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new KBN()).start();
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
			int[] result = new int[N];
			result[0] = K-1; result[1] = K*(K-1);
			for(int i=2; i<N; i++)
				result[i] = (result[i-1]+result[i-2])*(K-1);
			System.out.print(result[N-1]);
		}
		catch(IOException e)
		{System.out.print(e.toString());}
		
	}

}
