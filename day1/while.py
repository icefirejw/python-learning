
def TestWhile():
    num = 23
    isRunning=True
    print ('hhhhhh %s' %isRunning)
    while (isRunning):
        guess=int(input('Enter an integer:'))
        if (guess == num):
            print ('well done!')
            isRunning=False
        elif (guess < num):
            print ('it is too lower')
        else:
            print ('it is too higher')
    else:
        print ('while loop is ending')

TestWhile()

