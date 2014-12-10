/**
 Problem 1:
 
 If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 
 Find the sum of all the multiples of 3 or 5 below 1000.
 
 Solution:
 Iterate through all multiples of 3 and 5, adding each to sum
 - NOTE: Multiples may overlap, so one variable needs to check against this
*/

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
	}

}