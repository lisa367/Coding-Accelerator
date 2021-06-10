import sys

def recursive_factorial(num):
    if num > 0 :
        num_list = list(range(1, num+1))
        factorial = 1
        for i in num_list:
            factorial = factorial * i
        return print(factorial)
    else:
        return 0

recursive_factorial(int(sys.argv[1]))

#Tests :
#recursive_factorial(3)
#recursive_factorial(7)