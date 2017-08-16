import java.io.*;
import java.util.*;

public class GT {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try{
			//initial
			StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
			in.nextToken();
			int num = (int)in.nval;
			
			TreeNode[] tree = new TreeNode[num];
			Stack stack = new Stack();
			int input;

			for(int i=0; i<num; i++)
				tree[i] = new TreeNode(num);
			
			//build graphic
			for(int i=0; i<num; i++)
			{
				in.nextToken();
				input = (int)in.nval-1;
				
				while(input != -1)
				{
					tree[i].children[tree[i].cnum++] = input;
					tree[input].anum++;
					
					in.nextToken();
					input = (int)in.nval-1;
				}
			}
			
			//find 0-indegree node
			for(int i=0; i<num; i++)
				if(tree[i].anum == 0) stack.push(new Integer(i));
			
			
			int temp1, temp2, output;
			//topological sort
			while(!stack.empty())
			{
				temp1 = ((Integer)stack.pop()).intValue();
				output = temp1+1;
				System.out.print(output);
				
				for(int i=0; i<tree[temp1].cnum; i++)
				{
					temp2 = tree[temp1].children[i];
					tree[temp2].anum--;
					if(tree[temp2].anum == 0) stack.push(new Integer(temp2));
				}
				if(!stack.empty()) System.out.print(' ');
			}
		
		}
		catch(IOException e){System.out.print(e.toString());}
	}

}

class TreeNode
{
	public int[] children;
	public int cnum;
	public int anum;
	public TreeNode(int nodenum)
	{
		children = new int[nodenum];
		cnum = 0;
		anum = 0;
	}
}