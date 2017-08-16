import java.io.*;

public class SG implements Runnable {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//if the first player wins in a perfect game
		//it means no matter the second player choose in the game
		//the first player will win as long as he choose the special stone in his first choose
		//if the second player wins in a perfect game
		//it measn no matter the first player choose in the game
		//the second player will win as long as he choose the special stone in his first choose
		new Thread(new SG()).start();
	}
	public void run()
	{
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int N = (int)in.nval;
			in.nextToken();
			int M = (int)in.nval;
			
			int[] k = new int[M];
			for(int i=0; i<M; i++)
			{
				in.nextToken();
				k[i] = (int)in.nval;
			}
			//use dp
			//winner[i] = 1
			//it means when N is i, the second player either lose the game
			//or can't move, then the player 1 win.
			//winner[i] = 2 as well
			
			int[] winner = new int[N+1];
			winner[0] = 1;
			
			for(int i=1; i<=N; i++)
			{
				for(int j=0; j<M; j++)
					if(i>k[j] && winner[i-k[j]]==2)
					{
						winner[i] = 1;
						break;
					}
				if(winner[i]==0) winner[i] = 2;
			}
			
			System.out.print(winner[N]);
		}catch(IOException e)
		{System.out.print(e.toString());}
	}
}
