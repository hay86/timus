

public class Timus_1107 {

	public static int next() throws Exception {
		int ret = 0;
		int ch = System.in.read();
		while (ch != -1 && (ch < 48 || ch > 57)) {
			ch = System.in.read();
		}
		while (ch != -1 && ch >= 48 && ch <= 57) {
			ret = ret*10 + ch - 48;
			ch = System.in.read();
		}
		return ret;
	}
	
	public static void main(String[] args) throws Exception {
		int n = next();
		int k = next();
		int m = next();
		m = n + 1;
		
		System.out.println("YES");
		
		for (int i=0; i<k; i++) {
			int sum = 0;
			int l = next();
			for (int j=0; j<l; j++) {
				sum += next();
				sum %= m;
			}
			System.out.println(sum + 1);
		}
	}

}
