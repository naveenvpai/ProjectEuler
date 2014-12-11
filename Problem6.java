/**
Problem 6: 
 
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Solution:
 
Wrote methods taking long for both sumOfSquares and squareOfSums, printed the difference when n = 100
- MISTAKE: Didn't realize the difference should be absolute value when it asks for difference between
 
*/

public class Problem6 {

    public static long sumOfSquares(long n) {
        long sum = 0;
        for (long i = 1; i <= n; i++) {
            sum += i*i;
        }
        return sum;
    }
    
    public static long squareOfSum(long n) {
        long sum = 0;
        for (int i = 1; i <=n; i++) {
            sum += i;
        }
        return sum*sum;
    }
    
    public static void main(String[] args) {
        long s1 = sumOfSquares(100);
        long s2 = squareOfSum(100);
        System.out.println(Math.abs(s1-s2));
    }

}