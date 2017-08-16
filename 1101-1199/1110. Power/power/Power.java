import java.io.*;
public class Power implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try {
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
			in.nextToken();
			int N = (int)in.nval;
			in.nextToken();
			int M = (int)in.nval;
			in.nextToken();
			int Y = (int)in.nval;
			
			boolean a = false;
			for (int i = 0; i < M; i++) 
			{
				if(power(i, N, M)==Y)
					{out.append(i+" "); a = true;}
			}
			if(!a)
				out.append("-1");
			out.flush();
			
		} catch (Exception e) {
			e.printStackTrace();
		}

	}
	public int power(int x, int n, int m)
	{
		if(n==0)
			return 1;
		int res = power(x, n/2, m);
		res = (res*res)%m;
		if(n%2==0)
			return res;
		else 
			return (res*x)%m;
	}


	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Power()).start();
	}

}
