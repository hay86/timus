import java.io.*;
import java.util.*;
public class QuickSort implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			StreamTokenizer read = new StreamTokenizer(in);
			read.nextToken();
			int n = (int)read.nval;
			int[] a = new int[n];
			for(int i=0; i<n; i++)
			{
				read.nextToken();
				a[i] = (int)read.nval;
				//System.out.println(a[i]);
			}
			read.nextToken();read.nextToken();read.nextToken();
			read.nextToken();
			int m = (int)read.nval;
			//System.out.println(m);
			if(m>=50)
				Arrays.sort(a);
			for(int i=0; i<m; i++)
			{
				read.nextToken();
				int q = (int)read.nval;
				if(m>=50)
					System.out.println(a[q-1]);
				else
					System.out.println(select(a, 0, n-1, q));
			}
		}
		catch(IOException e)
		{e.printStackTrace();}
	}
	
	private int select(int[] a, int low, int high, int k)
	{
		if(low == high)
			return a[low];
		else
		{
			int mid = partition(a, low, high);
			//System.out.println(low+" "+high+" "+mid+" "+k);
			if(k == mid-low+1)
				return a[mid];
			else if(k<mid-low+1)
				return select(a, low, mid-1, k);
			else
				return select(a, mid+1, high, k-(mid-low+1));
		}
	}
	
	private int partition(int[] a, int low, int high)
	{
		int t = a[low];
		int i = low;
		for(int j=low+1; j<=high; j++)
		{
			if(a[j]<=t)
			{
				i++;
				if(i != j)
				{
					int temp = a[i];
					a[i] = a[j];
					a[j] = temp;
				}
			}
		}
		int temp = a[low];
		a[low] = a[i];
		a[i] = temp;
		return i;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new QuickSort()).start();
	}

}
