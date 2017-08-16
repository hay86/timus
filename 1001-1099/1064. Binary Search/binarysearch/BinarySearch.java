import java.io.*;
public class BinarySearch implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			
			in.nextToken();
			int I = (int)in.nval;
			in.nextToken();
			int L = (int)in.nval;
			int high = I;
			for(int i=0; i<L; i++)
				high = high*2+2;
			int low = (int)((I+0.5)/(1-Math.pow(0.5, L)));

			int sector = 0, prior = -1;
			int[] mem = new int[10000];
			
			for(int n=low; n<=high && n<=10000; n++)
			{
				int p = 0;
				int q = n-1;
				for(int j=0; j<L; j++)
				{
					int i = (p+q)/2;

					if(I>i) p = i+1;
					else if(I<i) q = i-1;
					else if(j==L-1)
					{
						if(n!=prior+1)
						{
							if(prior != -1)
								mem[2*sector-1] = prior;
							mem[2*sector] = n;
							sector++;
						}
						prior = n;
					}
					else break;
						
				}
			}
			if(sector>0)
				mem[sector*2-1] = prior;
			System.out.println(sector);
			for(int i=0; i<sector; i++)
			{
				System.out.println(mem[2*i]+" "+mem[2*i+1]);
			}
		}
		catch(IOException e)
		{e.printStackTrace();}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new BinarySearch()).start();
	}

}
