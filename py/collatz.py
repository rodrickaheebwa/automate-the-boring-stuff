def collatz(num):
    if num%2 == 0:
        #print(num//2)
        return num//2
    else:
        #print(3*num+1)
        return 3*num+1


def output(num):
    if collatz(num) == 1:
        print(1)
        return 1
    else:
        print(collatz(num))
        return output(collatz(num))

number = input('Enter a number : ')

try:
    output(int(number))
except:
    print('Enter an integer.')
