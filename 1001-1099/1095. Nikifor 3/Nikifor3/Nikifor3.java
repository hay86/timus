import java.io.*;
import java.util.*;

public class Nikifor3 implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			//check all the combination of 1234
			int[] remainder = new int[7];
			int[] digits = {0,1,1,1,1,0,0,0,0,0};
			Generator g = new Generator(10, digits);
			long combin = g.generateNext();
			while(combin != -1)
			{
				for(int i=0; i<7; i++)
				{
					if(remainder[i] == 0 && (i*10000+combin)%7 == 0)
						remainder[i] = (int)combin;
				}
				combin = g.generateNext();
			}
			for(int i=0; i<7; i++)System.out.println(remainder[i]);
			
			//check the int exclude 1234 each digit once
			for(int i=0; i<10; i++)
				digits[i] = 0;
			long sum;
			
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
			int read = in.read(), N = 0;
			while(read>='0' && read<='9')
			{
				N = N*10 + (read - '0');
				read = in.read();
			}
			
			for(int i=0; i<N; i++)
			{
				sum = 0;
				while(read<'0' || read>'9')
					read = in.read();
				while(read>='0' && read<='9')
				{
					digits[read-'0']++;
					read = in.read();
				}
				for(int j=1; j<5; j++)
					digits[j]--;
				for(int j=0; j<10; j++)
				{
					while(digits[j] != 0)
					{
						sum = sum*10 + j;
						digits[j]--;
					}
				}
				if(sum != 0)out.print(sum);
				out.println(remainder[(int)sum%7]);
			}
			out.flush();
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
		new Thread(new Nikifor3()).start();
	}

}
