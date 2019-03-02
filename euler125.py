# The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.
# There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.
# Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.


from CommonLib import isParlindrom
import time
import math


def euler125():
    stime = time.time()

    resultSet = []
    # 2중 for loop으로 주어진 숫자의 제곱의 합들을 구한다.
    # 주어진 숫자는 자신의 거듭제곱근의 숫자의 제곱보다 클 수 없다.
    for p in range(100000000,0,-1):
        SqrtNum = round(math.sqrt(p)) + 1
        tempsrt = str(p) + " = "
        for i in range(1, SqrtNum):
            total = 0
            tempsrt = ""

            for j in range(1, i):
                total = total + j*j
                tempsrt = tempsrt + str(j) + " + "
                if total > p :
                    tempsrt = ""
                    #print(tempsrt)
                    break

            if  p == total:
                print(tempsrt)
                resultSet.append(p)
                break

        print(p, str(time.time() - stime))
        stime = time.time()

    print(resultSet,'>>>>',sum(resultSet))



euler125()
