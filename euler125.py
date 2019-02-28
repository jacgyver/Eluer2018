# The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.
# There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.
# Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.


import time

#123
def Reverse(num):
    res = 0
    while(num>10):
        rem = num % 10
        res = res*10 + rem
        num = num // 10

def isPalindrom(num):

    return False


def euler125():
    stime = time.time()

    print(str(time.time() - stime))
