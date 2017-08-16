import java.io.*;
import java.util.*;

public class Sum implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		//classical algorithm
		try
		{
			StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
			PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
			in.nextToken();
			int N = (int)in.nval;
			
			int op, output, zero = 0;
			in.nextToken();
			output = (int)in.nval;
			in.nextToken();
			output += (int)in.nval;
			
			for(int i=1; i<N; i++)
			{
				in.nextToken();
				op = (int)in.nval;
				in.nextToken();
				op += (int)in.nval;
				
				if(op==9) zero++;
				else if(op<9) 
				{
					out.print(output);
					for(int j=0; j<zero; j++)
						out.print(9);
					output = op;
					zero = 0;
				}
				else
				{
					output++;
					out.print(output);
					for(int j=0; j<zero; j++)
						out.print(0);
					output = op - 10;
					zero = 0;
				}
			}
			if(zero == 0)
				out.print(output);
			else
			{
				out.print(output);
				for(int j=0; j<zero; j++)
					out.print(9);
			}
			out.flush();
		}
		catch(IOException e)
		{
			System.out.print(e.toString());
		} 
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		new Thread(new Sum()).start();
		
	}

}
