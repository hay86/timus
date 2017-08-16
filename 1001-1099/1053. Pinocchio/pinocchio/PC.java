import java.io.*;

public class PC implements Runnable{

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//此问题即为求n个int的最小公约数，所以不可能有IMPOSSIBLE，至少为1
		new Thread(new PC()).start();
	}
	
	public void run()
	{
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int num = (int)in.nval;
			int d = num/2, r = num%2;
			long[] array = new long[d+r];
			
			//input
			long temp1, temp2;
			for(int i=0; i<d; i++)
			{
				in.nextToken();
				temp1 = (long)in.nval;
				in.nextToken();
				temp2 = (long)in.nval;
				array[i] = min_CD(temp1, temp2);
			}
			if(r == 1)
			{
				in.nextToken();
				array[d] = (long)in.nval;
			}
			//分治
			num = d+r;
			d = (num)/2;
			r = (num)%2;
			while(!(d==0 && r==1))
			{
				for(int i=0; i<d; i++)
					array[i] = min_CD(array[2*i],array[2*i+1]);
				if(r == 1) array[d] = array[2*d];
				num = d+r;
				d = (num)/2;
				r = (num)%2;
			}
			
			//output
			System.out.print(array[0]);
			
		}
		catch(IOException e)
		{System.out.print(e.toString());}
	}
	
	long min_CD(long a, long b)
	{
		//exchange
		if(a < b)
		{
			long temp = a;
			a = b;
			b = temp;
		}
		
		if(a%b == 0)return b;
		else return min_CD(b, a%b);
	}
}
