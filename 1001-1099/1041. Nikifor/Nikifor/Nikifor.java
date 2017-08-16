import java.io.*;
import java.util.*;
import java.math.*;

public class Nikifor implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
			StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
			in.nextToken();
			int M = (int)in.nval;
			in.nextToken();
			int N = (int)in.nval;
			
			BigInteger[][] matrix = new BigInteger[M][N];
			for(int i=0; i<M; i++)
				for(int j=0; j<N; j++)
				{
					in.nextToken();
					matrix[i][j] = new BigInteger(String.valueOf((int)in.nval));
				}
			
			int[] price = new int[M];
			for(int i=0; i<M; i++)
			{
				in.nextToken();
				price[i] = (int)in.nval;
			}
			
			//sort
			int[] visit = new int[M];
			for(int i=0; i<M; i++)
				visit[i] = i;
			sort(price, visit, M);
			//相等的elem 保持原有order
			int beg = 0, elem = price[0];
			for(int i=1; i<M; i++)
			{
				if(elem != price[i])
				{
					if(i-beg>1)
						Arrays.sort(visit, beg, i);
					elem = price[i];
					beg = i;
				}
			}
			if(beg<M-1)
				Arrays.sort(visit, beg, M);
//			for(int i=0; i<M; i++)
//				System.out.println(visit[i]);
			//simplify the matrix
			int[] index = new int[N];
			int[] loc = new int[N];
			int len = 0;
			int tprice = 0;
			BigInteger temp1, temp2, zero = new BigInteger("0");
			for(int i=0; i<M; i++)
			{
				for(int j=0; j<len; j++)
				{
					if(matrix[visit[i]][loc[j]].compareTo(zero) != 0)
					{
						//common divisor
						temp1 = matrix[visit[i]][loc[j]].gcd(matrix[index[j]][loc[j]]);
						//避免用double 通过int公倍数消成0 temp1 temp2为2乘数
						temp2 = matrix[index[j]][loc[j]].divide(temp1);
						temp1 = matrix[visit[i]][loc[j]].divide(temp1);
						for(int k=0; k<N; k++)
						{
							matrix[visit[i]][k] = (matrix[visit[i]][k].multiply(temp2)).subtract(matrix[index[j]][k].multiply(temp1));
						}
					}
				}
				//检查是否全0
				for(int j=0; j<N; j++)
				{
					if(matrix[visit[i]][j].compareTo(zero) != 0)
					{

						index[len] = visit[i];
						loc[len++] = j;
						tprice += price[i];
						break;
					}
				}
				if(len == N) break;
			}
			
			//output
			if(len != N)out.print(0);
			else
			{
				out.println(tprice);
				Arrays.sort(index);
				for(int i=0; i<N; i++)
					out.println(index[i]+1);
			}
			out.flush();
			
		}
		catch(IOException e)
		{
			System.out.print(e.toString());
		}
	}
	
	/***************************sort int[] by int[]*********************************/
	void sort(int[] according, int[]sortelem, int n)
	{
		int temp;
		buildHeap(according, sortelem, n);

		for(int i= n-1; i>=1; i--)
		{
//			exchange according
			temp = according[i];
			according[i] = according[0];
			according[0] = temp;
//			exchange sortelem
			temp = sortelem[i];
			sortelem[i] = sortelem[0];
			sortelem[0] = temp;
			
			if(i != 1)buildHeap(according, sortelem, i);
		}
		
	}
	void buildHeap(int[] according, int[]sortelem, int n)
	{
		int N = n/2, fbigloc, temp, bbigloc;

		if(n%2 == 0)
			fbigloc = n-1;
		else
			fbigloc = according[N*2-1] > according[N*2]? N*2-1 : N*2;

		for(int i=N-1; i>=0; i--)
		{
//			exchange the front
			if(according[fbigloc] > according[i])
			{
//				exchange according
				temp = according[i];
				according[i] = according[fbigloc];
				according[fbigloc] = temp;
//				exchange sortelem
				temp = sortelem[i];
				sortelem[i] = sortelem[fbigloc];
				sortelem[fbigloc] = temp;
			}
			
//			exchange the back
			bbigloc = 2*(fbigloc+1);
			if(bbigloc+1 <= n)
				bbigloc = according[bbigloc-1] > according[bbigloc] ? bbigloc-1 : bbigloc;
			else if(bbigloc == n)
				bbigloc--;
			else bbigloc = n;
			while(bbigloc<n)
			{
				if(according[fbigloc] < according[bbigloc])
				{
//					exchange according
					temp = according[fbigloc];
					according[fbigloc] = according[bbigloc];
					according[bbigloc] = temp;
//					exchange sortelem
					temp = sortelem[fbigloc];
					sortelem[fbigloc] = sortelem[bbigloc];
					sortelem[bbigloc] = temp;
				}
				
				fbigloc = bbigloc;
				bbigloc = 2*(fbigloc+1);
				if(bbigloc+1 <= n)
					bbigloc = according[bbigloc-1] > according[bbigloc] ? bbigloc-1 : bbigloc;
				else if(bbigloc == n)
					bbigloc--;
				else bbigloc = n;
			}
			
			if(i != 0)fbigloc = according[i*2-1] > according[i*2]? i*2-1 : i*2;
		}
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Nikifor()).start();
	}

}
