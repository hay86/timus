import java.util.concurrent.ConcurrentLinkedQueue;
import java.io.*;

public class PN implements Runnable {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//此版本wa◎5  用的是bfs  至今不知道why 不过dp的版本通过了 
		new Thread(new PN()).start();

	}

	public void run() {
		try {
//			ByteArrayInputStream in = new ByteArrayInputStream(
//			"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111\r\n50\r\ni\r\nii\r\niii\r\niiii\r\niiiii\r\niiiiii\r\niiiiiii\r\niiiiiiii\r\niiiiiiiii\r\niiiiiiiiii\r\niiiiiiiiiii\r\niiiiiiiiiiii\r\niiiiiiiiiiiii\r\niiiiiiiiiiiiii\r\niiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\n-1"
//			.getBytes());
			InputStream in = System.in;
			int ch = in.read();
			int slen, dnum, order, rnum;
			int start, anum; //anum+1=answer's length
			int[] dlen;
			int[] answer;
			int [][] record;
			char[][] source, dic;			
			boolean march, succeed;			
			ConcurrentLinkedQueue curloc;

			while (ch != '-') {
				// initial
				answer = new int[100];
				record = new int[10000][2];
				source = new char[100][3];
				curloc = new ConcurrentLinkedQueue();
				slen = 0;
				dnum = 0;
				anum = 0;
				rnum = 0;
				order = -2;
				succeed = false;
				march = true;
				
				// read the call num
				while (ch != '\r') {
					if (ch == '0') {
						source[slen][0] = 'o';
						source[slen][1] = 'q';
						source[slen++][2] = 'z';
					} else if (ch == '1') {
						source[slen][0] = 'i';
						source[slen++][1] = 'j';
					} else if (ch == '2') {
						source[slen][0] = 'a';
						source[slen][1] = 'b';
						source[slen++][2] = 'c';
					} else if (ch == '3') {
						source[slen][0] = 'd';
						source[slen][1] = 'e';
						source[slen++][2] = 'f';
					} else if (ch == '4') {
						source[slen][0] = 'g';
						source[slen++][1] = 'h';
					} else if (ch == '5') {
						source[slen][0] = 'k';
						source[slen++][1] = 'l';
					} else if (ch == '6') {
						source[slen][0] = 'm';
						source[slen++][1] = 'n';
					} else if (ch == '7') {
						source[slen][0] = 'p';
						source[slen][1] = 'r';
						source[slen++][2] = 's';
					} else if (ch == '8') {
						source[slen][0] = 't';
						source[slen][1] = 'u';
						source[slen++][2] = 'v';
					} else if (ch == '9') {
						source[slen][0] = 'w';
						source[slen][1] = 'x';
						source[slen++][2] = 'y';
					}
					ch = in.read();
				}

				// read the dictionary num
				in.read();// get \n
				ch = in.read();
				while (ch != '\r') {
					dnum = dnum * 10 + (ch - '0');
					ch = in.read();
				}

				// read the dictionary
				dic = new char[dnum][50];
				dlen = new int[dnum];
				in.read();// get \n

				for (int i = 0; i < dnum; i++) {
					ch = in.read();
					while (ch != '\r') {
						dic[i][dlen[i]++] = (char) ch;
						ch = in.read();
					}
					in.read();// get '\n'
				}
				
				//start
				curloc.offer(new Integer(0));
				// check 
				// use the algorithm of BFS
				while (!curloc.isEmpty() && !succeed) {
					
					//System.out.print("out"+elem);
					start = ((Integer) curloc.poll()).intValue();
					order++;
					for (int i = 0; i < dnum; i++) {
						if (dlen[i] <= slen - start) {
							for (int j = 0; j < dlen[i]; j++) 
								if (!(source[start + j][0] == dic[i][j]
										|| source[start + j][1] == dic[i][j] || source[start + j][2] == dic[i][j])) {
									march = false;
									break;
								}
							if (march) {
								record[rnum][0] = i;
								record[rnum++][1] = order;
								
								if (dlen[i] == slen - start) {
									anum = record(answer, record, rnum-1);
									succeed = true;
									break;
								} else {
									curloc.offer(new Integer(start + dlen[i]));
									//System.out.print("in"+i+elem);
								}
							} else
								march = true;
						}
					}
				}
				
				
				// output
				if (succeed) {
					for (int i = 0; i <= anum; i++) {
						for (int j = 0; j < dlen[answer[i]]; j++)
							System.out.print(dic[answer[i]][j]);
						if (i != anum)
							System.out.print(' ');
					}
				} else
					System.out.print("No solution.");
				System.out.println();
				ch = in.read();
			}

		} catch (Exception e) {
			System.out.println(e.toString());
		}


	}
	int record(int[] answer, int[][] record, int order)
	{
		if(record[order][1] != -1)
		{
			int len;
			len = record(answer, record, record[order][1]);
			answer[++len] = record[order][0];
			return len;
		}
		else
		{
			answer[0] = record[order][0];
			return 0;
		}
	}

}
