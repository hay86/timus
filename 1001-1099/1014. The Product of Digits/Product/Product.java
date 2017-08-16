import java.io.*;
import java.util.*;
public class Product implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
			in.nextToken();
			int n = (int)in.nval;
			if(n == 0)
				out.print(10);
			else if(n == 1)
				out.print(1);
			else
			{
				int[] digit = new int[10];
				for(int i=9; i>1; i--)
				{
					while(n%i == 0)
					{
						n /= i;
						digit[i]++;
					}
				}
				if(n == 1)
				{
					for(int i=2; i<=9; i++)
						for(int j=digit[i]; j>0; j--)
							out.print(i);
				}
				else out.print(-1);
			}
			out.flush();
			
		}
		catch(IOException e)
		{System.out.print(e.toString());}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Product()).start();
	}

}
