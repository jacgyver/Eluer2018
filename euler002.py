def fibonacci(to=10):
    one = 1
    two = 2
    solution = 2

    for i in range(1, to):
        three = one + two
        one = two
        two = three


        if three % 2 == 0:
            solution += three

        if three > 4000000:
            print (solution)
            exit()


        print(str(i+2) + " : ", three)

fibonacci(50)


