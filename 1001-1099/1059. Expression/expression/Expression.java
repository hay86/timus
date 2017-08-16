import java.io.*;
public class Expression implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
			in.nextToken();
			int n = (int)in.nval;
			out.println('0');
			for(int i=1; i<=n; i++)
			{
				out.println('X');
				out.println('*');
				out.println(i);
				out.println('+');
				out.flush();
			}
		}
		catch(IOException e)
		{e.printStackTrace();}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Expression()).start();
	}

}
