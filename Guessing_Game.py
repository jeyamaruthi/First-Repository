secret = 9
i = 0

while i<3:
    if(i==2):
            l = int(input("Last Attempt:"))
            if(l==secret):
                print("u win!!")
                exit()
    l = int(input('Guess:'))
    if(l==secret):
        print("u win!!")
        exit()
    i = i+1;

print("U lose")