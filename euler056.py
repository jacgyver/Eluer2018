# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
import math

def euler056():
    resultset = []
    for subscript in range(1,100):
        for superscript in range(1,100):
            multinum = subscript**superscript
            slice = list(str(multinum))
            totallist = list(map(int,slice))
            resultset.append(sum(totallist))

#    print(resultset)
    print(max(resultset))

euler056()
