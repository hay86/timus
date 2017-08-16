import java.io.*;
import java.util.*;

public class Maximum implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			int[] input = new int[10];
			int len = 0;
			while(true)
			{
				in.nextToken();
				if(in.nval == 0) break;
				else input[len++] = (int)in.nval;
			}
			Arrays.sort(input,0,len);

			int[] data = new int[input[len-1]+1];
			data[0] = 0; data[1] = 1;
			int temp = 0, max = 0;
			for(int i=1; i<=input[len-1]; i++)
			{
				if(i%2 == 0) data[i] = data[i/2];
				else data[i] = data[i/2]+data[i/2+1];
				if(max<data[i]) max = data[i];
				while(i == input[temp])
				{
					System.out.println(max);
					temp++;
				}
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
		new Thread(new Maximum()).start();
	}

}
