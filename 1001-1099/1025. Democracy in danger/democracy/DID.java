import java.io.*;
import java.util.*;

public class DID implements Runnable{

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new DID()).start();
		}

	public void run()
	{
		try {
			int[] groups;
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(
					System.in));

			in.nextToken();
			int num = (int) in.nval;
			int majority = (num+1)/2;
			int votes = 0;
			groups = new int[num];
			
			for(int i=0; i<num; i++)
			{
				in.nextToken();
				groups[i] = (int)in.nval;
			}
			
			Arrays.sort(groups);
			
			for(int i=0; i<majority; i++)
				votes += (groups[i]+1)/2;
			
			System.out.print(votes);
			
		} catch (IOException e) {
			System.out.print(e.toString());
		}
	}
}
