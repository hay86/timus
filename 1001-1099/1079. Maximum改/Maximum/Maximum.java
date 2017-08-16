import java.io.*;
import java.util.*;

public class Maximum implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			HashSet<Integer> set = new HashSet<Integer>();
			in.nextToken();
			int[] input = new int[10];
			input[0]  = (int)in.nval;
			int mValue = input[0], len = 0;
			while(true)
			{
				in.nextToken();
				if(in.nval==0)break;
				input[++len] = (int)in.nval;
				if(input[len]>mValue)
					mValue = input[len];
			}
			int[] res = new int[++len];
			int[] data = new int[mValue+1];
			data[0] = 0; data[1] = 1;
			int max = 0;
			for(int i=1; i<=mValue; i++)
			{
				if(i%2 == 0) data[i] = data[i/2];
				else data[i] = data[i/2]+data[i/2+1];
				if(max<data[i]) max = data[i];
				for(int j=0; j<len; j++)
					if(i==input[j])
						res[j] = max;
			}
			
			for(int i=0; i<len; i++)
				System.out.println(res[i]);
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
