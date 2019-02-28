# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# 1. Loop 1,000,000 from reverse
# 2. Divide two part, 몫과 나머지
# 3. Find Parlindromic number

def revnum(num):
    reverse = 0
    while(num>0):
        rem = num % 10
        reverse = reverse*10 + rem
        num = num // 10
    return reverse

def euler004():
    set = []
    for i in range(999,0,-1):
        for j in range(999,0,-1):
            nominator = i * j
            quotient = nominator // 1000
            remainder = nominator % 1000

            if quotient == revnum(remainder):
                set.append(nominator)

    print(max(set))

euler004()

