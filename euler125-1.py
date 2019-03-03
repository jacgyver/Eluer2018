# The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.
# There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.
# Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.
# Change Plain Loop to another solution

from CommonLib import isParlindrom
import time
import math


def euler125():
    stime = time.time()

    resultSet = []
    # 2중 for loop으로 주어진 숫자의 제곱의 합들을 구한다.
    # 주어진 숫자는 자신의 거듭제곱근의 숫자의 제곱보다 클 수 없다.
    for p in range(1000,0,-1):
        SqrtNum = round(math.sqrt(p))
        tempsrt = str(p) + " = "
        for i in range(SqrtNum, 0, -1):
            total = 0
            count = 0
            tempsrt = ""

            for j in range(i, 0, -1):
                count += 1
                total = total + j*j
                # tempsrt = tempsrt + str(j) + " + "
                if total >= p:
                    # if total == p and isParlindrom(p):
                    #     print(p," : ",tempsrt)
                    # tempsrt = ""
                    break


            if p == total and isParlindrom(p) and count>1:
               resultSet.append(p)
               break

        if p%100 == 0:
            print(p, str(time.time() - stime))
            stime = time.time()

    print(resultSet,'>>>>',sum(resultSet))



euler125()

