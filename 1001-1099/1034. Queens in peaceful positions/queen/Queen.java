import java.io.*;
public class Queen implements Runnable {

	/**
	 * @param args
	 */
	private boolean isLeagel(int[] a, int l1, int l2, int l3)
	{
		for(int i=0; i<a.length; i++)
		{
			if(i != l1 && Math.abs(a[l1]-a[i])==Math.abs(l1-i))
				return false;
			if(i != l2 && Math.abs(a[l2]-a[i])==Math.abs(l2-i))
				return false;
			if(i != l3 && Math.abs(a[l3]-a[i])==Math.abs(l3-i))
				return false;
		}
		return true;
	}
	public void run()
	{
		try
		{
			StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
			in.nextToken();
			int n = (int)in.nval;
			int[] pos = new int[n];
			for(int i=0; i<n; i++)
			{	
				in.nextToken();
				int temp = (int)in.nval;
				in.nextToken();
				pos[temp-1] = (int)in.nval-1;
			}
			int counter = 0;
			//C(3,n),swap(a,b,c),check
			for(int i=0; i<n-2; i++)
				for(int j=i+1; j<n-1; j++)
					for(int k=j+1; k<n; k++)
						for(int t=0; t<3; t++)
						{
							int temp = pos[i];
							pos[i] = pos[j];
							pos[j] = pos[k];
							pos[k] = temp;
							if(t!=2 && isLeagel(pos, i, j, k))
								counter++;
						}
						
			System.out.println(counter);
		}
		catch(IOException e)
		{e.printStackTrace();}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		new Thread(new Queen()).start();
	}

}
