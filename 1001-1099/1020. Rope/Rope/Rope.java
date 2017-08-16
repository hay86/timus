import java.io.*;
import java.text.*;

public class Rope implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int N = (int)in.nval;
			in.nextToken();
			double R = in.nval;
			in.nextToken();
			double x0 = in.nval;
			in.nextToken();
			double y0 = in.nval;
			double x=x0, y=y0, x_, y_;
			double result = 0;
			for(int i=0; i<N; i++)
			{
				if(i==N-1)
				{
					x_ = x0;
					y_ = y0;
				}
				else
				{
					in.nextToken();
					x_ = in.nval;
					in.nextToken();
					y_ = in.nval;
				}
				result += Math.sqrt((x-x_)*(x-x_)+(y-y_)*(y-y_));
				x = x_; y = y_;
			}
			
			result += 2*Math.PI*R;
			DecimalFormat df = new DecimalFormat("0.00");
			String output = df.format(result);
			System.out.print(output);
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
		new Thread(new Rope()).start();
	}

}
