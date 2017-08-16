import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.HashMap;

public class Timus_1003_2 {

	/**
	 * @param args
	 * @throws Exception
	 */
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		StreamTokenizer st = new StreamTokenizer(new InputStreamReader(
				System.in));

		st.nextToken();
		int p = (int) st.nval;

		while (p != -1) {

			HashMap<Integer, Boolean> exist = new HashMap<Integer, Boolean>();
			HashMap<Integer, Boolean> odd = new HashMap<Integer, Boolean>();
			HashMap<Integer, Integer> start = new HashMap<Integer, Integer>();

			st.nextToken();
			int q = (int) st.nval;
			int answer = 0;

			for (int i = 0; i < q; i++) {
				st.nextToken();
				Integer s = Integer.valueOf((int) st.nval);

				st.nextToken();
				Integer e = Integer.valueOf((int) st.nval);

				st.nextToken();
				Boolean v = Boolean.valueOf(st.sval.equals("odd"));

				if (answer == 0) {

					if (!(1 <= s && s <= e && e <= p && add(s, e, v, exist,
							odd, start))) {

						answer = i;
					}
				}

			}
			System.out.println(answer == 0 ? q : answer);
			
			st.nextToken();
			p = (int) st.nval;
		}
	}

	public static boolean add(int s, int e, boolean v,
			HashMap<Integer, Boolean> exist, HashMap<Integer, Boolean> odd,
			HashMap<Integer, Integer> start) {
		
		if(!exist.containsKey(e)){
			
			exist.put(e, true);
			odd.put(e, v);
			start.put(e, s);
			return true;
		}
		else{
			
			int ss = start.get(e);
			if(ss == s){
				
				return odd.get(e).equals(v);
			}
			else if(ss < s){
				
				return add(ss, s-1, !odd.get(e).equals(v), exist, odd, start);
			}
			else{
			
				return add(s, ss-1, !odd.get(e).equals(v), exist, odd, start);
			}
		}

	}

}
