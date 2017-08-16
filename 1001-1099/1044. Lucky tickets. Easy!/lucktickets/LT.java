import java.io.*;
public class LT implements Runnable{

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		new Thread(new LT()).start();
	}
	public void run()
	{
		//0.125s  good algorithm
		//input
		StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
		try{in.nextToken();}catch(IOException e){}
		
		int N = (int)in.nval;
		if(N%2 ==1) return;
		
		//initial
		N /= 2;
		int valuenum = N*9 +1;
		int[] digits = new int[N];
		int[] value = new int[valuenum];
		int sum = 0;//the sum of digits
		
		while(true)
		{
			//get the valuenum
			for(int j=0; j<10; j++)
				value[sum+j]++;
			
			sum += 10;
			//add
			digits[N-1] += 10;
			//check the carry
			for(int i=N-1; i>0; i--)
			{
				if(digits[i] == 10)
				{
					digits[i] = 0;
					digits[i-1]++;
					sum -= 9;
					
				}
				else break;
			}
			if(digits[0] == 10)break;
			
		}
		//output
		int total = 0;
		for(int i=0; i<valuenum; i++)
			total += value[i]*value[i];
		System.out.print(total);

	}

}
