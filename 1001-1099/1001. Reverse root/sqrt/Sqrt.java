import java.io.*;
import java.text.*;

public class Sqrt implements Runnable {

	/**
	 * @param args
	 */

	DecimalFormat df;
	StreamTokenizer in;
	String output;
	double[] num;

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		new Thread(new Sqrt()).start();

	}

	public void run() {
		try {
			df = new DecimalFormat("0.0000");
			in = new StreamTokenizer(
					new StringReader(
							" 1427 0 \r\n\r\n 876652098643267843 \r\n5276538 \r\n \r\n\r\n100 "));
//			in = new StreamTokenizer(new InputStreamReader(System.in));
			int i = 0;
			num = new double[130000];
			while (in.nextToken() != StreamTokenizer.TT_EOF)
				num[i++] = in.nval;
			while(i != 0)
			{
				output = df.format(Math.sqrt((num[--i])));
				System.out.println(output);
			}
		} catch (IOException e) {
		}
	}
}
