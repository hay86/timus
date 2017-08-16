import java.io.*;
public class Labyrinth implements Runnable {

	public void run() {
		// TODO Auto-generated method stub

		try
		{
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			int N = Integer.parseInt(in.readLine().trim());
			int[][] a = new int[N][N];
			for(int i=0; i<N; i++)
			{
				String line = in.readLine();
				for(int j=0; j<N; j++)
					a[i][j] = line.charAt(j);
			}
			visit(a, 0, 0);
			visit(a, N-1, N-1);
			int sum = 0;
			for(int i=0; i<N; i++)
				for(int j=0; j<N; j++)
					if(a[i][j]==0)
					{
						if(i==0 || a[i-1][j]==(int)'#')
							sum++;
						if(i==N-1 || a[i+1][j]==(int)'#')
							sum++;
						if(j==0 || a[i][j-1]==(int)'#')
							sum++;
						if(j==N-1 || a[i][j+1]==(int)'#')
							sum++;
					}
			//System.out.println(sum);
			sum -= 4;
			sum *= 9;
			System.out.println(sum);
		}
		catch(IOException e)
		{e.printStackTrace();}
	}
	
	public void visit(int[][] a, int x, int y)
	{
		a[x][y] = 0;
		if(x+1<a.length && a[x+1][y]==(int)'.')
			visit(a, x+1, y);
		if(x-1>-1 && a[x-1][y]==(int)'.')
			visit(a, x-1, y);
		if(y+1<a.length && a[x][y+1]==(int)'.')
			visit(a, x, y+1);
		if(y-1>-1 && a[x][y-1]==(int)'.')
			visit(a, x, y-1);
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Labyrinth()).start();
	}

}
