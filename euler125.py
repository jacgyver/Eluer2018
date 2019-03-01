# The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.
# There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.
# Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.


from CommonLib import isParlindrom
import time
import math


def euler125():
    stime = time.time()

    Start = 961
    for i in range(Start,0,-1):
        SqrtNum = round(math.sqrt(i))
        temp = 0

        while(SqrtNum>0):
            temp = temp + SqrtNum*SqrtNum
            if i == temp:
                print (SqrtNum)
                return i
            if i < temp:
                break

            SqrtNum-=-1


    print(str(time.time() - stime))


print (euler125())
