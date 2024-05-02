from os import system 

while(True):
    x = input("Start (s), exit (e) : ")
    if x == 's':
        size = 0
        counter = 0
        round = 1
        turn = 0
        character = []
        temp = []
        while(True):
            y = input("Char name, 'c' to complete, 'd' to delete : ")
            if(y == 'c'):
                size = len(character)
                break
            elif(y == 'd'):
                character.pop()
            elif(y != ''):
                character.append(y)
            else:
                print("Error Entry")
        while(True):
            system('cls')
            for i in range(size):
                if turn == i:
                    print(str(i)+ '  ' + str(character[i]) + ' *')
                else:
                    print(str(i)+ '  ' + str(character[i]))
            print()
            z = input("'d'-dead 'e'-exit 'a'-add ' '-next: ")
            if(z == 'd'):
                a = input("Dead character index: ")
                character.pop(int(a))
                size-=1
            elif (z == 'e'):
                break
            elif (z == 'a'): 
                a = input("New character name: ")
                b = input("New character index: ")
                character.insert(int(b), a)
                size+=1
            elif (z == 'r'):
                turn = 0
            else:
                if (turn == size-1) or (size <= 1):
                    turn = -1
                turn+=1
    elif x == 'e':
        break
    else:   
        x = ''         