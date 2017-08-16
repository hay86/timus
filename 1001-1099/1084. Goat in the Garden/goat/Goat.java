import java.io.*;
public class Goat implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int n = (int)in.nval;
			in.nextToken();
			int r = (int)in.nval;
			double res;
			if(r<=n/2)
				res = r*r*Math.PI;
			else if(r>=n*Math.sqrt(2)/2)
				res = n*n;
			else
			{
				double angle = 2*Math.acos((n+.0)/2/(double)r);
				
				res = r*r*Math.sin(angle)/2;
				res += r*r*Math.PI*((Math.PI/2-angle)/(2*Math.PI));
				res *= 4;
			}
			//System.out.println(res);
			long format = Math.round(res*1000);
			System.out.printf("%.3f", (format+.0)/1000);
		}
		catch(IOException e)
		{e.printStackTrace();}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Goat()).start();
	}

}
