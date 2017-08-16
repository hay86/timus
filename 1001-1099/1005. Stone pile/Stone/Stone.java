import java.io.*;
import java.util.*;

public class Stone implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
			PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
			in.nextToken();
			int n = (int)in.nval;
			int[] stone = new int[n];
			ArrayList[] belong = new ArrayList[n]; 
			int sum = 0, half;
			for(int i=0; i<n; i++)
			{
				in.nextToken();
				sum += in.nval;
				stone[i] = (int)in.nval;
				belong[i] = new ArrayList();
			}
			
			half = sum/2;
			boolean[] weight = new boolean[half+1];
			int max = 0;
			for(int i=1; i<=half; i++)
			{
				for(int j=0; j<n; j++)
				{
					if(i == stone[j])
					{
						max = i;
						weight[i] = true;
						belong[j].add(new Integer(i));
						break;
					}
					else if(i>stone[j] && weight[i-stone[j]] && !belong[j].contains(new Integer(i-stone[j])))
					{	
						max = i;
						weight[i] = true;
						for(int k=0; k<n; k++)
							if(belong[k].contains(new Integer(i-stone[j])))
								belong[k].add(new Integer(i));
						belong[j].add(new Integer(i));
						break;
					}
				}
			}
			
			int min = sum - 2*max;
			out.print(min);
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
		new Thread(new Stone()).start();
	}

}
