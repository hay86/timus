import java.io.*;
import java.util.*;

public class Nikifor2 implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try {
			StreamTokenizer in = new StreamTokenizer(new BufferedReader(
					new InputStreamReader(System.in)));
			PrintWriter out = new PrintWriter(
					new OutputStreamWriter(System.out));
			in.nextToken();
			int x = (int) in.nval;
			in.nextToken();
			int y = (int) in.nval;

			// filter
			boolean[] escape = new boolean[x + 1];
			int up = (int) Math.sqrt(x);
			for (int i = 2; i <= up; i++) {
				if (!escape[i]) {
					int temp = i * i;
					while (temp <= x) {
						escape[temp] = true;
						temp = temp * i;
					}
				}
			}

			// check
			int xlen, ylen, xdigit, ydigit;
			int i, x0, y0;
			for (i = 2; i <= x; i++) {
				if (!escape[i]) {
					x0 = x;
					y0 = y;
					xlen = 0;
					ylen = 0;
					//calculate the digit num
					while(x0 != 0)
					{
						x0 /= i;
						xlen++;
					}
					while(y0 != 0)
					{
						y0 /= i;
						ylen++;
					}
					x0 = x;
					y0 = y;
					while (xlen >= ylen && ylen != 0) {
						ydigit = y0 % i;
//						 if(i == 2) System.out.print(ydigit);
						y0 = y0 / i;
						ylen--;
						do {
							xdigit = x0 % i;
//							 if(i == 2) System.out.print(" "+xdigit);
							x0 = x0 / i;
							xlen--;
						} while (xdigit != ydigit && xlen >= ylen);
					}
					if (xlen >= ylen)
						break;
				}

			}
			if (i <= x)
				out.print(i);
			else
				out.print("No solution");

			out.flush();

		} catch (IOException e) {
			System.out.print(e.toString());
		}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Nikifor2()).start();
	}

}
