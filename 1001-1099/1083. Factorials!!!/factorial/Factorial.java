import java.io.*;
public class Factorial implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			InputStream in = System.in;
			int read = in.read();
			int num = 0, counter = 0;
			while(read<'0' || read>'9')
				read = in.read();
			while(read>='0' && read<='9')
			{
				num = num*10 + (read - '0');
				read = in.read();
			}
			while(read != -1)
			{
				if(read == '!') counter++;
				read = in.read();
			}
			
			if(num<=counter) System.out.print(num);
			else
			{
				int output = 1;
				while(num>0)
				{
					output *= num;
					num = num-counter;
				}
				System.out.print(output);
			}
		}
		catch(IOException e)
		{System.out.print(e.toString());}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Factorial()).start();
	}

}
