import java.io.*;

public class Conductors implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		// more explanation from discuss
		/*
		 * The example 13 14.1 If there is only 1 person,you only can got 0% or
		 * 100%. If there is only 2 persons, you can got 0%,50%,100% and so on.
		 * You can notice that if the number of the people below 15,you can not
		 * got one number between 13% and 14.1%. But 15,you can got 13.333%
		 * (2/15).So this is the answer.
		 */
		try {
			//double和float都是trash 记得用Math.round
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(
					System.in));
			in.nextToken();
			int part1 = (int)Math.round(in.nval * 100);
			in.nextToken();
			int part2 = (int)Math.round(in.nval * 100 - part1);
			
			int counter = 0;
			if (part2 == 0) 
			{
				int temp = 0;
				do
				{
					counter++;
					temp += part1;
					if(temp >= 10000)
						temp -= 10000;
				}while(temp != 0);
				
			} else 
			{
				int temp1 = 0, temp2 = 0;
				while (!(temp1 + temp2 > 10000)) 
				{
					counter++;
					temp1 += part1;
					temp2 += part2;
					if (temp1 >= 10000)
						temp1 -= 10000;
				}
			}
			
			System.out.print(counter);
			
		} catch (IOException e) {
			System.out.print(e.toString());
		}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Conductors()).start();
	}

}
