"""
    Problem 4:
    
    A palindromic number reads the same both ways. The largest palindrome made from the
    product of two 2-digit numbers is 9009 = 91 × 99.
    
    Find the largest palindrome made from the product of two 3-digit numbers.
    
    Solution:
    
    Method checks palindrome by looping through and checking if the string is symmetrical
    
    Loop downwards from the maximum product of two n-digit numbers
    - if you find a palindrome:
    - check if it has two factors that are n-digit numbers
        (MISTAKE: didn't check the second factor, i/j)
"""

def isPalindrome(n):
    s = str(n)
        for i in range(0, len(s)):
            if s[i] != s[len(s)-1-i]: return False
        return True

def highestPalindrome(factorLength):
    for i in range((10**(factorLength)-1)**2, (10**(factorLength-1)-1)**2, -1):
        if isPalindrome(i):
            for j in range(10**(factorLength)-1,10**(factorLength-1)-1,-1):
                if (i%j == 0 and len(str(i/j)) == factorLength):
                    return i
                        break

print(highestPalindrome(1))