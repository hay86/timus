import java.io.*;
public class Sinusdances implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
			in.nextToken();
			printS(out, (int)in.nval, (int)in.nval);
		}
		catch(IOException e)
		{e.printStackTrace();}
	}
	
	public void printA(PrintWriter out, int i, int n)
	{
		if(i==n)
		{
			out.append("sin("+n+")");
			out.flush();
			return;
		}
		
		if(i%2==0)
			out.append("sin("+i+"+");
		else 
			out.append("sin("+i+"-");
		out.flush();
		printA(out, i+1, n);
		out.append(")");
		out.flush();
	}
	public void printS(PrintWriter out, int j, int n)
	{
		if(j==1)
		{
			printA(out, 1, 1);
			out.append("+"+n);
			out.flush();
			return;
		}
		out.append("(");
		out.flush();
		printS(out, j-1, n);
		out.append(")");
		printA(out, 1, j);
		out.append("+"+(n-j+1));
		out.flush();
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Sinusdances()).start();
	}

}
