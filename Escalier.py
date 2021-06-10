import sys

def escalier(num):
    for i in range(1, (num+1)):
        print(i*"#")

argument = int(sys.argv[1])
escalier(argument)





