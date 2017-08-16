

public class Timus_1102 {
	static short[] line = new short[10000000];
	static int i = 0;
	static boolean lastline = false;
	static short ch;
	static void readline() throws Exception{
		ch = (short)System.in.read();
		while (ch == '\r' || ch == '\n')
			ch = (short)System.in.read();
		i = 0;
		while (ch != '\r' && ch != '\n' && ch != -1){
			line[i++] = ch;
			ch = (short)System.in.read();
		}
		if (ch == -1)
			lastline = true;
	}
	public static void main(String[] args) throws Exception {
		readline();
		while (!lastline){
			readline();
			i -= 1;
			while (i >= 0){
				if (line[i] == 'e'){
					if (i >= 2 && line[i-1] == 'n' && line[i-2] == 'o') i -= 3;
					else break;
				}
				else if (line[i] == 'n'){
					if (i >= 1 && line[i-1] == 'i') i -= 2;
					else if (i >= 4 && line[i-1] == 'o' && line[i-2] == 't' && line[i-3] == 'u' && line[i-4] == 'p') i -= 5;
					else break;
				}
				else if (line[i] == 't'){
					if (i >= 2 && line[i-1] == 'u')
					{
						if (line[i-2] == 'o') i-= 3;
						else if (line[i-2] == 'p'){
							if (i >= 4 && line[i-3] == 'n' && line[i-4] == 'i') i -= 5;
							else if (i >= 5 && line[i-3] == 't' && line[i-4] == 'u' && line[i-5] == 'o') i -= 6;
							else break;
						}
						else break;
					}
					else break;
				}
				else break;
			}
			if (i < 0)
				System.out.println("YES");
			else
				System.out.println("NO");
		}
	}

}
