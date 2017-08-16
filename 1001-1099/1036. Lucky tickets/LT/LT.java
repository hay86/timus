import java.io.*;
import java.util.*;
import java.math.*;

public class LT implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int N = (int)Math.round(in.nval);
			in.nextToken();
			int S = (int)Math.round(in.nval);
			
			if(S%2 == 1 || N*18<S) System.out.print(0);
			else
			{
				ArrayList prior;
				ArrayList current = new ArrayList();
				BigInteger temp = new BigInteger("1");
				//initial
				for(int i=0; i<10; i++)
					current.add(temp);
				for(int i=2; i<=N; i++)
				{
					prior = current;
					current = new ArrayList(i*9+1);
					for(int j=0; j<=i*9; j++)
					{
						temp = new BigInteger("0");
						for(int k=0; k<=9; k++)
						{
							if(j-k>=0 && j-k<=(i-1)*9)
								 temp = temp.add((BigInteger)prior.get(j-k));
						}
						current.add(temp);
					}
				}
				temp = (BigInteger)current.get(S/2);
				temp = temp.multiply((BigInteger)current.get(S/2));
				System.out.print(temp);
			}
		}
		catch(IOException e)
		{System.out.print(e.toString());}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new LT()).start();
	}

}
