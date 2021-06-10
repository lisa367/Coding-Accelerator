import sys
input = int(sys.argv[1])

def recursive_factorial(num):
    if num > 0 :
        num_list = list(range(1, num+1))
        factorial = 1
        for i in num_list:
            factorial = factorial * i
        return factorial
    else:
        return 0

fact = recursive_factorial(input)
fact = str(fact)
#print(fact)


liste = []
for i in range(len(fact)):
    liste.append(fact[i])
liste = liste[::-1]
#print(liste)

output = []
count = 0
for i in range(len(liste)):
    output.append(liste[i])
    count += 1
    if count == 3:
        output.append(",")
        count = 0

output = output[::-1]
#print(output)
print("".join(output))
