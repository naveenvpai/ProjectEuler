public class Problem1 {

	public static void main(String[] args) {
	
		int under = 1000;
		
		int sum = 0;
		int m3 = 3;
		int m5 = 5;
		while (m3 < under || m5 < under) {
			if (m3 < under) {
				sum += m3;
				m3 	+= 3;
			}
			if (m5 < under) {
				if (m5 %3 != 0) sum += m5;
				m5	+= 5;
			}
		}
		
		System.out.println(sum);
		//System.out.println("Hello World");
	}

}