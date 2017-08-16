import java.io.*;

public class Hanio implements Runnable{

	/**
	 * @param args
	 */
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Hanio()).start();
	}
	
	public void run()
	{
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			byte n = (byte)in.nval;
			byte[] D = new byte[n];
			for(byte i=0; i<n; i++)
			{
				in.nextToken();
				D[i] = (byte)in.nval;
			}
			
			byte from = 1, to = 2, temp = 3, transfer;
			int times = 0;
			boolean movable = false;
			for(int i=n-1; i>-1; i--)
			{
				if(D[i] == from) movable = true;
				else if(D[i] == to)
				{
					times += Math.pow(2, (byte)i);
					transfer = from;
					from = temp;
					temp = transfer;
					movable = false;
				}
				else if(D[i] == temp && movable)
				{
					times += Math.pow(2, (byte)i);
					transfer = from;
					from = to;
					to = temp;
					temp = transfer;
					movable = false;
				}
				else
				{
					times = -1;
					break;
				}
			}
			System.out.print(times);
		}
		catch(IOException e)
		{
			System.out.print(e.toString());
		}
	}
}
