from random import randint

print("Welcome to Pythonic Rock,Papers and Scissors")
print("Instructions")
print("Press r for rock")
print("Press p for paper")
print("Press s for scissors")

choice = input('Enter your choice:')

while(True):
    if(choice == 'r'):
        print('O', end=' ')

    elif(choice == 'p'):
        print('___', end=' ')

    elif(choice == 's'):
        print('>8', end=' ')

    else:
        print('??')

    print('vs', end=' ')

    chosen = randint(1, 3)

    if(chosen == 1):
        computer = 'r'
        print('O')

    elif(chosen == 2):
        computer = 'p'
        print('___')

    else:
        computer = 's'
        print('>8')

    if(choice == computer):
        print('DRAW!')

    elif(choice == 'r' and computer == 's'):
        print('You win!')

    elif(choice == 'r' and computer == 'p'):
        print('Computer wins!')

    elif(choice == 'p' and computer == 'r'):
        print('You wins!')

    elif(choice == 'p' and computer == 's'):
        print('Computer win!')

    elif(choice == 's' and computer == 'p'):
        print('You win!')

    elif(choice == "s" and computer == 'r'):
        print('Computer wins!')

    else:
        print('Huh?')
}