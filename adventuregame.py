
print('Welcome to your first game')

name = input('What is your name? ')
print()
age = int(input('What is your age? '))

# Health will gauge if the player has won or lost.  When health hits 0, Player loses
health = 10

# added a age requirement
if age >= 18: 
    print("You are old enough to play!")

    wants_to_play = input('Do you want to play? yes/no ')
         
# Giving the player an option to play or not
    if wants_to_play == "yes":
        print(f'You are starting with {health} health')
        print('Lets play!')

# included this weapon choice to make conditional statements further in the game
        weapon = input("Pick a weapon(sword/gun/taser): ").lower()

        #Printing different statements depending on weapon choice
        if weapon == "gun":
            print("That should help!")
            

        elif weapon == "sword":
            print("You have a chance")
        

        elif weapon == "taser":
            print("Wrong choice! You wouldn't stand a chance! Play again")
            exit()

        else:
            print("No such weapon, play again!")
            exit()

# First choice in the game!
        left_or_right = input('First choice.. "Left" or "Right" ' ).lower()

        # Comparing conditional statements of left_or_right and choice of weapon. 

        if left_or_right == "left" and weapon == "gun":
                ans = input("Nice, you followed the path with your gun and reached a lake... Do you swim across or go around (across/around) " )
                if ans == "around":
                    print('You went around with your gun and reached the other side of the lake')
        elif left_or_right == "right" and weapon == "gun":
                ans = input("Nice, you followed the path with your gun and reached a lake... Do you swim across or go around (across/around) " )
                if ans == "across":
                    print('You managed to get across, but were bit by a alligator and lost 5 health.')
                    health -= 5

        
        elif left_or_right == "left" and weapon == "sword":
                ans = input("Nice, you followed the path with your sword and reached a lake... Do you swim across or go around (across/around) " )
                if ans == "across":
                    print('You managed to get across, but were bit by a alligator and lost 5 health.')
                    health -= 5
                elif ans == "around":
                    print('You went around with your sword and reached the other side of the lake')

        elif left_or_right == "right" and weapon == "sword":
            ans = input("Nice, you followed the path with your sword and reached a lake... Do you swim across or go around (across/around) " )
            if ans == "across":
                print('You managed to get across, but were bit by a alligator and lost 5 health.')
            elif ans == "around":
                    print('You went around with your sword and reached the other side of the lake')

        
        ans2 = input('You notice a house and a river, which do you go to? (river/house)? ')
        if ans2 == "house":
                print("You go to the house and are greated by the owner... He doesn't like you so he shoots you in the leg. Resulting in losing 5 health, but you end up killing him")
                health -= 5

        if health <= 0:
                print('You now have 0 health and you lost the game')
        else:
                print('You have survived. you WIN!')
                
        if ans2 == "river":
                print('You fell in the river and lost...')

    if wants_to_play == "no":
        print('See ya')
        
if not age >= 18: 
    print("You are not old enough to play!")
    




