import java.io.*;

public class PN implements Runnable {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//此版本通过  用的是dp
		new Thread(new PN()).start();
	}

	public void run() {
		try {
//			ByteArrayInputStream in = new ByteArrayInputStream(
//			"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111\r\n50\r\ni\r\nii\r\niii\r\niiii\r\niiiii\r\niiiiii\r\niiiiiii\r\niiiiiiii\r\niiiiiiiii\r\niiiiiiiiii\r\niiiiiiiiiii\r\niiiiiiiiiiii\r\niiiiiiiiiiiii\r\niiiiiiiiiiiiii\r\niiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\r\n-1"
//			.getBytes());
			
			//declaration
			InputStream in = System.in;
			int ch = in.read();
			
			//read variable
			int slen, dnum;
			int[] dlen;
			char[][] source, dic;
			
			//check variable
			int[][] answer;
			int[] alen;
			boolean march;
			int[] min_loc;

			while (ch != '-') {
				
				// initial
				source = new char[100][3];
				slen = 0;
				dnum = 0;
				
				/**********************read data*******************/
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
	
				/**********************check data*******************/
				//use dp
				//initial
				march = true;
				answer = new int[slen][];
				for(int i=0; i<slen; i++)
					answer[i] = new int[i+1];
				alen = new int[slen];
				min_loc = new int[2];
				
				//len = i+1
				for(int i=0; i<slen; i++)
				{
					min_loc[0] = 101; min_loc[1] = -1;
					for(int j=0; j<dnum; j++)
					{
						if(dlen[j]<=i+1)
						{
							for(int k=0; k<dlen[j]; k++)
								if(!(dic[j][k] ==source[slen-i-1+k][0]||
									 dic[j][k] ==source[slen-i-1+k][1]|| 
									 dic[j][k] ==source[slen-i-1+k][2]))
								{
									march = false;
									break;
								}
						}
						if(march)
						{
							if(dlen[j]-i-1==0)
							{
								alen[i] = 1;
								answer[i][0] = j;
								min_loc[1] = -1;//just for flag
								break;
							}
							else if(i+1-dlen[j]>0 && alen[i-dlen[j]]!=0 && alen[i-dlen[j]]+1<min_loc[0])
							{
								
								min_loc[0] = alen[i-dlen[j]]+1;
								min_loc[1] = j;
							}
						}
						else march = true;
					}
					if(min_loc[1]!=-1)
					{//System.out.print(min_loc[0]+" "+min_loc[1]);
						for(int j=0; j<min_loc[0]-1; j++)
							answer[i][j] = answer[i-dlen[min_loc[1]]][j];
						answer[i][min_loc[0]-1] = min_loc[1];
						alen[i] = min_loc[0];
					}
				}
				
				/**********************output data*******************/
				//output
				if(alen[slen-1] == 0)
					System.out.print("No solution.");
				else
				{
					for(int i=alen[slen-1]-1; i>-1; i--)
					{
						for(int j=0; j<dlen[answer[slen-1][i]]; j++)
							System.out.print(dic[answer[slen-1][i]][j]);
						if(i!=0) System.out.print(' ');
					}
				}
				System.out.println();
				ch = in.read();
			} 
		}catch (Exception e) 
		{System.out.print(e.toString());}
//		test.end();

	}
	
}
