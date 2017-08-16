import java.io.*;
import java.util.*;
public class FlipGame implements Runnable {

	final static byte[] W = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
	final static byte[] B = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1};
	int min = 17;//if avaliable the max is 16
	public void run() {
		// TODO Auto-generated method stub
		try
		{
			byte[] a = new byte[16];
			byte[] b = new byte[16];
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			for(int i=0; i<4; i++)
			{
				String line = in.readLine();
				for(int j=0; j<4; j++)
					a[4*i+j] = line.charAt(j)=='b'?(byte)1:0;
			}
			search(a, b, 0);
			if(min == 17)
				System.out.println("Impossible");
			else System.out.println(min);
		}
		catch(IOException e)
		{e.printStackTrace();}
	}
	public void search(byte[] a, byte[] b, int n)
	{
		if(n==16)
		{
			if(Arrays.equals(a, W) || Arrays.equals(a, B))
			{
				//for(int i=0; i<16; i++)
				//System.out.println(a[0]);
				int c = 0;
				for(int i=0; i<16; i++)
					if(b[i]==1) c++;
				if(min>c) min = c;
			}
		}
		else
		{
			b[n] = 0;
			search(a, b, n+1);
			b[n] = 1;
			flip(a, n);
			search(a, b, n+1);
			flip(a, n);
		}
	}
	public void flip(byte[] a, int n)
	{
		a[n] = (byte)(1-a[n]);
		if(n+4<=15)
			a[n+4] = (byte)(1-a[n+4]);
		if(n-4>=0)
			a[n-4] = (byte)(1-a[n-4]);
		if(n%4>0)
			a[n-1] = (byte)(1-a[n-1]);
		if(n%4<3)
			a[n+1] = (byte)(1-a[n+1]);
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new FlipGame()).start();
	}

}
