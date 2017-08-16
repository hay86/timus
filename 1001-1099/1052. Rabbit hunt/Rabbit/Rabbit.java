import java.io.*;

public class Rabbit implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int N = (int)in.nval;
			int[] x = new int[N], y = new int[N];
			//input
			for(int i=0; i<N; i++)
			{
				in.nextToken();
				x[i] = (int)in.nval;
				in.nextToken();
				y[i] = (int)in.nval;
			}
			int w, h, counter = 0, output = 0;
			for(int i=0; i<=N-1; i++)
				for(int j=i+1; j<N; j++)
				{
					w = x[i] - x[j];
					h = y[i] - y[j];
					for(int k=0; k<N; k++)
						if(w*(y[j]-y[k])==h*(x[j]-x[k]))
							counter++;
					if(output<counter) output = counter;
					counter = 0;
				}
			System.out.print(output);
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
		new Thread(new Rabbit()).start();
	}

}
