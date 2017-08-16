
public class HeapSort {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = {4,3,5,2,1};
		int[] b = {1,2,3,4,5};
		HeapSort.sort(a, b, 5);
		for(int i=0; i<5; i++)
			System.out.print(b[i]+" ");
		
	}
	/***************************sort int[] by int[]*********************************/
	public static void sort(int[] according, int[]sortelem, int n)
	{
		int temp;
		buildHeap(according, sortelem, n);

		for(int i= n-1; i>=1; i--)
		{
//			exchange according
			temp = according[i];
			according[i] = according[0];
			according[0] = temp;
//			exchange sortelem
			temp = sortelem[i];
			sortelem[i] = sortelem[0];
			sortelem[0] = temp;
			
			if(i != 1)buildHeap(according, sortelem, i);
		}
		
	}
	static void buildHeap(int[] according, int[]sortelem, int n)
	{
		int N = n/2, fbigloc, temp, bbigloc;

		if(n%2 == 0)
			fbigloc = n-1;
		else
			fbigloc = according[N*2-1] > according[N*2]? N*2-1 : N*2;

		for(int i=N-1; i>=0; i--)
		{
//			exchange the front
			if(according[fbigloc] > according[i])
			{
//				exchange according
				temp = according[i];
				according[i] = according[fbigloc];
				according[fbigloc] = temp;
//				exchange sortelem
				temp = sortelem[i];
				sortelem[i] = sortelem[fbigloc];
				sortelem[fbigloc] = temp;
			}
			
//			exchange the back
			bbigloc = 2*(fbigloc+1);
			if(bbigloc+1 <= n)
				bbigloc = according[bbigloc-1] > according[bbigloc] ? bbigloc-1 : bbigloc;
			else if(bbigloc == n)
				bbigloc--;
			else bbigloc = n;
			while(bbigloc<n)
			{
				if(according[fbigloc] < according[bbigloc])
				{
//					exchange according
					temp = according[fbigloc];
					according[fbigloc] = according[bbigloc];
					according[bbigloc] = temp;
//					exchange sortelem
					temp = sortelem[fbigloc];
					sortelem[fbigloc] = sortelem[bbigloc];
					sortelem[bbigloc] = temp;
				}
				
				fbigloc = bbigloc;
				bbigloc = 2*(fbigloc+1);
				if(bbigloc+1 <= n)
					bbigloc = according[bbigloc-1] > according[bbigloc] ? bbigloc-1 : bbigloc;
				else if(bbigloc == n)
					bbigloc--;
				else bbigloc = n;
			}
			
			if(i != 0)fbigloc = according[i*2-1] > according[i*2]? i*2-1 : i*2;
		}
	}
	
	
	/***************************sort int[][] by int[]*********************************/
	public static void sort(int[] according, int[][] sortelem, int n)
	{
		int temp1;
		int[] temp2;
		buildHeap(according, sortelem, n);

		for(int i= n-1; i>=1; i--)
		{
//			exchange according
			temp1 = according[i];
			according[i] = according[0];
			according[0] = temp1;
//			exchange sortelem
			temp2 = sortelem[i];
			sortelem[i] = sortelem[0];
			sortelem[0] = temp2;
			
			if(i != 1)buildHeap(according, sortelem, i);
		}
	}
	static void buildHeap(int[] according, int[][] sortelem, int n)
	{
		int N = n/2, fbigloc, temp1, bbigloc;
		int[] temp2;

		if(n%2 == 0)
			fbigloc = n-1;
		else
			fbigloc = according[N*2-1] > according[N*2]? N*2-1 : N*2;

		for(int i=N-1; i>=0; i--)
		{
//			exchange the front
			if(according[fbigloc] > according[i])
			{
//				exchange according
				temp1 = according[i];
				according[i] = according[fbigloc];
				according[fbigloc] = temp1;
//				exchange sortelem
				temp2 = sortelem[i];
				sortelem[i] = sortelem[fbigloc];
				sortelem[fbigloc] = temp2;
			}
			
//			exchange the back
			bbigloc = 2*(fbigloc+1);
			if(bbigloc+1 <= n)
				bbigloc = according[bbigloc-1] > according[bbigloc] ? bbigloc-1 : bbigloc;
			else if(bbigloc == n)
				bbigloc--;
			else bbigloc = n;
			while(bbigloc<n)
			{
				if(according[fbigloc] < according[bbigloc])
				{
//					exchange according
					temp1 = according[fbigloc];
					according[fbigloc] = according[bbigloc];
					according[bbigloc] = temp1;
//					exchange sortelem
					temp2 = sortelem[fbigloc];
					sortelem[fbigloc] = sortelem[bbigloc];
					sortelem[bbigloc] = temp2;
				}
				
				fbigloc = bbigloc;
				bbigloc = 2*(fbigloc+1);
				if(bbigloc+1 <= n)
					bbigloc = according[bbigloc-1] > according[bbigloc] ? bbigloc-1 : bbigloc;
				else if(bbigloc == n)
					bbigloc--;
				else bbigloc = n;
			}
			
			if(i != 0)fbigloc = according[i*2-1] > according[i*2]? i*2-1 : i*2;
		}
	}
	
}
