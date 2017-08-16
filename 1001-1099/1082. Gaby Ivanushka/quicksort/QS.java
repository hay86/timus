import java.io.*;
public class QS implements Runnable{

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//the souce file's program is just the quicksort algorithm
		//c is counter that record the left and right point's movement
		//if the input is not from min to max then the total c is (n+2)+(n+1)+...+3
		//= (n+5)n/2;
		//else c = (n+1)+n+...+3 = (n+4)(n-1)/2 just the requirement 
		//so just print 1 2 ... n
		new Thread(new QS()).start();
	}

	public void run()
	{
		StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
		try{in.nextToken();}catch(IOException e){}
		int N = (int)in.nval;
		for(int i=1; i<N; i++)
		{
			System.out.print(i);
			System.out.print(' ');
		}
		System.out.print(N);
		
	}
}
