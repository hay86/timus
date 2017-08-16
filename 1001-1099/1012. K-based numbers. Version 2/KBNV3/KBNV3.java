import java.io.*;
import java.math.*;

public class KBNV3 implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int N = (int)in.nval;
			in.nextToken();
			int K = (int)in.nval;
			BigInteger n1 = new BigInteger(String.valueOf(K-1)),
					   n2 = new BigInteger(String.valueOf(K*(K-1))),
					   K_1 = new BigInteger(String.valueOf(K-1)),
					   result = n2;
			
			for(int i=2; i<N; i++)
			{
				result = n1.add(n2).multiply(K_1);
				n1 = n2;
				n2 = result;
			}
			System.out.print(result.toString());
		}
		catch(IOException e)
		{System.out.print(e.toString());}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new KBNV3()).start();
	}

}
