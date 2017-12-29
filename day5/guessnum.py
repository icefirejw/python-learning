import random

def guessnum(num, count):
    print('input the guess number');
    for i in range(1,count,1):
        guess = input()
        if (guess < num):
            print("too small")
        elif (guess > num):
            print("too big")
        else:
            break

    if (i <= count):
        print('well done, clever boy!')
        return True;
    else:
        print('keep trying');
        return False;

number = random.randint(1,10)
guessnum(number, 5)



