import java.io.*;

public class Staircase implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			//use dp
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int N = (int)in.nval;
			//answer[i][j] means the different nums of staircases of j(j>0) steps building by i bricks
			//and answer[i][0] means the max steps i bricks can make
			long[][] answer = new long[N+1][];
			answer[0] = new long[1];
			
			for(int i=1; i<=N; i++)
			{
				answer[i] = new long[(int)Math.sqrt(2*i)+1];
				answer[i][0] = (int)Math.sqrt(2*i);
				answer[i][1] = 1;
				for(int j=2; j<=answer[i][0]; j++)
				{
					if(j-1<=answer[i-j][0]) answer[i][j] += answer[i-j][j-1];
					if(j<=answer[i-j][0]) answer[i][j] += answer[i-j][j];
				}
			}
			
			long output = 0;
			for(int i=2; i<=answer[N][0]; i++)
			{
				output += answer[N][i];
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
		new Thread(new Staircase()).start();
	}

}
