print('> type help, if you are new to this game:')
l = 'start'
started = False
stopped = False
while l!=quit:
    l = input('>').lower()
    if l=='start':
        if started:
            print('Car is already started')
        else:
            started = True
            print('Car has been started !!!!')

    elif l == 'stop':
        if stopped:
            print('Car is already stopped')
        elif started:
            print('Car stopped')
            stopped = True
        else:
            print('Car can be stopped only if itz already started')
        x = 0
    elif l == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to quit the car')
    elif l =='quit':
        print('Byeee.... !!')
        exit()
    else:
        print("I dont understand what you have typed..... !! please type the ri8 command")
