import random

def guessnum(num, numrag, count):
    print('guess a number between 1 and '+ str(numrag) + ', try ' + str(count) + ' times')
    c = 0
    while (c < count):
        guess = int(input())
        c = c + 1
        if (guess < num):
            print("too small")
            continue
        elif (guess > num):
            print("too big")
            continue
        else:
            break

    if (c < count or (c==count and guess == num)):
        print('well done, clever boy!')
        return True;
    else:
        print('keep trying')
        return False

numrange = 50
number = random.randint(1,numrange)
guessnum(number, numrange, 10)



