/**
Problem 5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Solution:

Loop through multiples of 20, checking each time if there any non-factors
- if none, the number is the answer
(11639628 loops)

*/

public class Problem5 {
	public static void main(String[] args) {
	   int i = 20;
	   while(!isCommon(i)) {
		   i += 20;
	   }
	   System.out.println(i);
	}
	
	public static boolean isCommon(int n) {
		for (int i = 19; i > 0; i--) {
			if (n%i != 0) return false;
		}
		return true;
	}
	
}