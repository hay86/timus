import java.io.*;
import java.text.*;

public class GL implements Runnable{

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new GL()).start();
	}
	
	public void run()
	{
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int num = (int)in.nval;
			in.nextToken();
			double A = in.nval;
			
			//use the formula Hn=(n-1)(n-2+H2) H1=0
			//deal the right
			int n = (int)Math.sqrt(A);
			double h2 = A/n - (n-1);
			if(h2>2)
			{
				n++;
				h2 = A/n - (n-1);
			}
			//System.out.print(h2+" "+n);
			//deal the left
			if(num>n+1)
			{
				h2 = 2 - h2;
				n = num - n;
				double B = (n-1)*(n-2+h2);
				DecimalFormat df = new DecimalFormat("0.00");
				String output = df.format(B);
				System.out.print(output);
			}
			else System.out.print("0.00");
			
		}
		catch(IOException e)
		{System.out.print(e.toString());}
	}
}
