import java.io.*;

public class Dice implements Runnable {

	public void run() {
		// TODO Auto-generated method stub
		try
		{
			StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
			PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
			in.nextToken();
			int N = (int)in.nval;
			int [][] record = new int[30][8],
			         index = {{2,3,4,5},{2,5,4,3},{0,5,1,3},{0,2,1,4},{0,3,1,5},{0,4,1,2}};
			int[] data = new int[6];
			int len = 0, loc1 = 0;
			Queue[] q = new Queue[30];
			for(int i=0; i<30; i++)
				q[i] = new Queue();
			
			for(int i=1, j, k, l; i<=N; i++)
			{
				//input
				for(j=0; j<6; j++)
				{
					in.nextToken();
					data[j] = (int)in.nval;
					if(in.nval == 1)
						loc1 = j;
				}
				//check
				for(j=0; j<len; j++)
				{
					for(k=0; k<4; k++)
						if(data[index[loc1][0]] == record[j][k])
							break;
					if(k<4)
					{
						for(l=1; l<4; l++)
							if(data[index[loc1][l]] != record[j][k+l])
								break;
						if(l == 4)
						{
							q[j].add(i);
							break;
						}
					}
				}
				if(j == len)
				{
					for(k=0; k<4; k++)
						record[len][k] = record[len][k+4] = data[index[loc1][k]];
					q[len++].add(i);
				}
			}
			//output
			out.println(len);
			int output;
			for(int i=0; i<len; i++)
			{	
				output = q[i].pop();
				while(output != -1)
				{
					out.print(output);
					out.print(' ');
					output = q[i].pop();
				}
				out.println();
			}
			out.flush();
		}
		catch(IOException e)
		{
			System.out.print(e.toString());
		}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Dice()).start();
	}

}

class Queue
{
	class Node
	{
		int elem;
		Node next;
		public Node(int elem, Node next)
		{
			this.elem = elem;
			this.next = next;
		}
	}
	Node head;
	Node tail;
	
	public Queue()
	{
		head = null;
	}
	public void add(int elem)
	{
		if(head == null)
		{
			head = new Node(elem, null);
			tail = head;
		}
		else
		{
			Node temp = new Node(elem, null);
			tail.next = temp;
			tail = temp;
		}
	}
	public int pop()
	{
		if(head == null)
			return -1;
		Node temp = head;
		head = head.next;
		return temp.elem;
	}
}