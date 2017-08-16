import java.io.*;
import java.util.*;

public class Simple implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{//0.218s 807 KB 
			PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
			BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
			//input n
			int N = 0;
			int ch = read.read();
			while(ch>='0' && ch<='9')
			{
				N = N*10 + (ch-'0');
				ch = read.read();
			}
			//the trick
			int[] remainder = {3241,2341,2134,1234,1342,1324,1243};
			//input long
			int zero, rem;
			boolean[] donce = new boolean[4];
			for(int i=0; i<N; i++)
			{
				//initial
				rem = zero = 0;
				for(int j=0; j<4; j++)
					donce[j] = false;
				//filter
				while(ch<'0' || ch>'9')
					ch = read.read();
				while(ch>='0' && ch<='9')
				{
					if(!donce[0] && ch == '1')
						donce[0] = true;
					else if(!donce[1] && ch == '2')
						donce[1] = true;
					else if(!donce[2] && ch == '3')
						donce[2] = true;
					else if(!donce[3] && ch == '4')
						donce[3] = true;
					else
					{
						if(ch != '0')
						{
							out.print((char)ch);
							rem = (rem*10+(ch-'0'))%7;
						}
						else zero++;
					}
					ch = read.read();
				}
				//output
				if(donce[0]&&donce[1]&&donce[2]&&donce[3])
				{
					out.print(remainder[rem]);
					for(int j=0; j<zero; j++)
						out.print('0');
				}
				else out.print('0');
				out.println();
			}
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
		new Thread(new Simple()).start();
	}

}
