import java.io.*;

public class Sum implements Runnable{

	
	public static void main(String arg[])
	{
		new Thread(new Sum()).start();
	}
	public void run()
	{
		try{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int a = (int)in.nval;
			int sum = (a+1)*(Math.abs(a-1)+1)/2;
			System.out.print(sum);
		}
		catch(IOException e)
		{
			System.out.print(e.toString());
		}
	}
}
