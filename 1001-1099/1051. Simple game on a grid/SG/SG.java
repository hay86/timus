import java.io.*;

public class SG implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		//algorithm
		//if M=1 or N=1 then answer=(M+N)/2
		//else if M%3=0 or N%3=0 anser=2
		//else answer=1
		//but i can't prove it the test show that
		try
		{
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int M = (int)in.nval;
			in.nextToken();
			int N = (int)in.nval;
			int output = 1;
			
			if(M==1 || N==1) output = (M+N)/2;
			else if(M%3==0 || N%3==0) output = 2;
			System.out.print(output);
		}
		catch(IOException e)
		{System.out.print(e.toString());}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new SG()).start();
	}

}
