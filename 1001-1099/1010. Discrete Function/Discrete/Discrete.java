import java.io.*;
import java.util.*;

public class Discrete implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		//the answer only accured in i and i+1 see what i mean
		try
		{
			PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
			StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
			in.nextToken();
			int n = (int)in.nval;
			
			in.nextToken();
			long y1 = (long)in.nval, y2;
			
			int x1 = 1, x2 = 2;
			long max = -1, inclination;
			
			for(int i=1; i<n; i++)
			{
				in.nextToken();
				y2 = (long)in.nval;
				
				inclination = Math.abs(y2 - y1);
				
				if(inclination > max)
				{
					max = inclination;
					x1 = i;
					x2 = i+1;
				}
				
				y1 = y2;
			}

			
			out.print(x1); out.print(' '); out.print(x2);
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
		new Thread(new Discrete()).start();
	}

}
