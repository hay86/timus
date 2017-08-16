import java.io.*;
import java.text.*;

public class SC implements Runnable{

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//a1 - a0 = x
		//a2 - a1 = x + 2c1
		//...
		//an+1 - an = x + 2c1 + 2c2 +...+ 2cn
		//=>an+1 - a0 = (n+1)x + 2nc1 +...+ 2cn
		new Thread(new SC()).start();
	}
	public void run()
	{
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int N = (int)in.nval;
			in.nextToken();
			double a0 = in.nval;
			in.nextToken();
			double dif = in.nval - a0;//an+1 - a0
			
			for(int i=N; i>0; i--)
			{
				in.nextToken();
				dif -= 2*i*in.nval;
			}
			
			dif /= N+1;//x
			a0 +=dif;//a1
			
			DecimalFormat df = new DecimalFormat("0.00");
			String output = df.format(a0);
			System.out.print(output);
		}
		catch(IOException e)
		{System.out.print(e.toString());}
	}
}
