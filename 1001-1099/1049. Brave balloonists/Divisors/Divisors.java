import java.io.*;

public class Divisors implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			//fine the prime num
			//true isn't the prime and false is
			boolean[] num = new boolean[10001];
			num[0] = true; num[1] = true;
			int temp, pnum = 0;
			for(int i=2; i<=10000; i++)
			{
				if(!num[i])
				{
					pnum++;
					temp = 10000/i;
					for(int j=2; j<=temp; j++)
						num[i*j] = true;
				}
			}
			//input and record prime num
			int[] prime = new int[pnum];
			int input, order = 0;
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			for(int i=0; i<10; i++)
			{
				in.nextToken();
				input = (int)in.nval;
				for(int j=2; j<=10000; j++)
				{
					if(!num[j])
					{
						while(input%j == 0)
						{
							prime[order]++;
							input = input/j;
						}
						order++;
					}
				}
				order = 0;
			}
			//output
			int output = (prime[0]+1)%10;
			for(int i=1; i<pnum; i++)
				output = (output*(prime[i]+1))%10;
			System.out.print(output);
			
		}catch(IOException e)
		{System.out.print(e.toString());}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Divisors()).start();
	}

}
