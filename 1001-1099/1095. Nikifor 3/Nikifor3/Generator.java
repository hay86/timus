
public class Generator {

	/**
	 * @param args
	 */
	int[] digits, loc;
	int radix, bits;
	long sum;
	boolean EOF;
	
	public Generator(int radix, int digits[])
	{
		EOF = false;
		bits = 0;//位数
		this.radix = radix;//基数
		this.digits = new int[radix];//每个基数的拥有个数
		for(int i=0; i<radix; i++)
		{
			this.digits[i] = digits[i];
			bits += digits[i];
		}
		loc = new int[bits];//记录组合的位置
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] digits ={1,1,1,1,1,0,0,0,0,0};
		Generator g = new Generator(10, digits);
		for(int i=0; i<120; i++)
		System.out.println(g.generateNext());
	}
	public long generateNext()
	{
		if(EOF) return -1;
		sum = 0;
		int[] tdigits = new int[radix];
		for(int i=0; i<radix; i++)
			tdigits[i] = digits[i];
		//add
		for(int i=0; i<bits; i++)
		{
			for(int j=loc[i]; j<radix; j++)
			{
				if(tdigits[j] != 0)
				{
					sum = sum*10 + j;
					tdigits[j]--;
					loc[i] = j;
					break;
				}	
			}
		}
		//rearrange the order
		int i = bits-1;
		for(; i>0; i--)
		{
			
			if(loc[i] > loc[i-1])
			{
				loc[i] = 0;
				loc[i-1]++;
				break;
			}
			else
				loc[i] = 0;
		}
		if(i == 0)  EOF= true;
		return sum;
	}
	
	
}
