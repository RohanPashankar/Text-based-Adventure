def start():
    #Starting of the game
    print("\nYou are standing in a dark room")
    print("\nThere are two doors in front of you. Which do you want to choose l or r")
    #Player input to be converted to a lower case
    answer = input(">").lower()
    if "l" in answer:
        bear_room()
        elif "r" in answer:
        monster_room()
        else
        game_over("\nDon't you know how to type something properly?")
        start()

        #Bear Room
        def bear_room():
        print("\nYou have entered the bear room.")
        print("\nThere is a big bear here")
        print("\nThere is a door behind the bear")
        print("\nThe bear is eating some honey. What will you do?")
        print("\n 1. Take the honey.")
        print("\n 2. Try to sneak around the bear.")
        answer = input(">")
        if answer == "1":
            game_over("\nYou were killed by the bear")
            elif answer == "2"
            print("\nThe bear was more interested in the honey than you. You were able to get to the next door")
            diamond_room()
            else:
                game_over("So many years worth of education was completely wasted on you. Don't you know how to type a number?")

       #Monster room
       def monster_room():
       print("\nYou have entered the monster room.")
        print("\nThere is a big disgusting monster here")
        print("\nThe monster sees you enter the room and gets up.")
        print("\nIt roars and starts moving towards you. What will you do?")
        print("\n 1. Run like hell to the next door.")
        print("\n 2. Pick up the sword next to you and try to fight it.")
        answer = input(">")
        if answer == "2":
            game_over("\nYou were killed by the moster in one swipe")
            elif answer == "1"
            print("\nThe monster was surprised at how fast you managed to run past. You were able to get to the next door")
            diamond_room()
            else:
                game_over("Go and learn how to type a number you idiot")   

        #Diamond Room
        def diamond_room():  
            print("\nYou enter a big room  which seems completely empty to you")
            print("\nYou look around and notice a small pile of glowing rocks. When you go closer you see that they are diamonds")
            print("\nYou can see a door in front of you. What do you do?")
            print("\n 1. Ignore the diamonds and go past them to the next room")
            print("\n 2. Pick up the diamonds")
            answer = input(">")
            if answer == "1":
            print("\n Nice you are a honest man. You have completed the game")
            play_again()
            elif answer == "2":
                game_over("\n They were cused diamonds. You have died")
            else:
                game_over("\n Learn to type a number moron")
        
        #Game Over function
        def game_over(reason):
            print("\n" + reason)
            print("Game Over!")
            play_again()
        
        #Play Again function
        def play_again():
            print("\nDo you want to play again? (y or n)")
            answer = input(">").lower()
            if "y" in answer:
                start()
                else:
                    exit()
    
