# An adventure game
from time import sleep
def room1():
    print("Pick a name young one")
    name = input("name, ")
    print("is that your real name?")
    answer = input("your reply, ")
    if answer == "yes":
        print("ok then welcome to the wonderful world of me saying things and you replying for things")
        print("welcome", name)
    elif answer == "no":
        print("well it does not matter there is no save so...")
        print("welcome", name)
    print("well lets jump right in!")
    print("you find yourself in a dark room")
    print("what will you do?")
    print("1. stay down and wait")
    print("2. get up and look for the light switch")
    print("3. stop breathing")
    answer = input("your action, ")
    if answer == "1":
        print("some time passed and now you fell asleep")
        print("and you never woke up")
    if answer == "2":
        print("you found you light switch after a few minutes")
        print("you switch the switch to find yourself in a room")
        print("you see a door.")
        print("do you go though?")
        answer = input("yes? or no?, ")
        if answer == "yes":
            room2()
        else:
            print("you look down and you see a sword in your stomach and you life is falling out of your body")
            quit()
    if answer == "3":
        print("you lived the rest of your life in peace and was very happy with it even if it was only 3 minutes long")
def room2():
    print("you look around the room and you find three Corridors.")
    print("slow motion activate")
    sleep(2)
    print("which corridor will you go down")
    sleep(2)
    print("1")
    sleep(2)
    print("2")
    sleep(2)
    print("3")
    sleep(2)
    answer = input("1,2 or 3, ")
    if answer == "1":
        print("you see a monster coming after you behind you")
        print("you make a run for it")
        print("you make it into a other room and close the door behind you")
        room4()
    else:
        print("a monster jumps you and you die!")
        print("""  _________))                ((__________
                  /.-------./\\    \    /    //\.--------.\
                 //#######//##\\   ))  ((   //##\\########\\
                //#######//###((  ((    ))  ))###\\########\\
               ((#######((#####\\  \\  //  //#####))########))
                \##' `###\######\\  \)(/  //######/####' `##/
                 )'    ``#)'  `##\`->oo<-'/##'  `(#''     `(
                         (       ``\`..'/''       )
                                    \""(
                                     `- )
                                     / /
                                    ( /\  
                                    /\| \
                                   (  \
                                       )
                                      /""")
def room4():
    print("you see a table in front of you and three doors")
    print("what do you do?")
    print("1.grab one of the balls")
    print("2.go though door one")
    print("3.go though door two")
    print("4.go though door three")
    answer = input("1, 2, 3 or 4, ")
    if answer == "1":
        print("you look at the balls when a old man who gives these balls to little children for free as a living appears")
        print("the old man tells you to take one of the balls")
        print("which will you take")
        print("1.Bulbasaur")
        print("2.Charmander")
        print("3.Squirtle")
        answer = input("1, 2 or 3, ")
        if answer == "1":
            print("you with your new friend open the door in which you came though and challenged it to a battle")
            sleep(2)
            print("the monster sent out mewtwo")
            sleep(2)
            print("bulbasaur stands no chance against mewtwo")
            sleep(2)
            print("bulbasaur charges towards it's death mewtwo does nothing wait is mewtwo scared?")
            sleep(2)
            print("bulbasaur hits mewtwo and explodes with such power i will call it a nuclear bomb")
            sleep(2)
            print("and world war 2 is over we thank you bulbasaur for killing for too many people")
            sleep(2)
            print("you should know that you died int the blast a war hero")
            sleep(2)
            print("rest in peace lord bulbasaur")
# 
# _____ = randint(1,2) == 50% chance
# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()

# the monster copy and paste it


#     _________))                ((__________
#      /.-------./\\    \    /    //\.--------.\
#     //#######//##\\   ))  ((   //##\\########\\
#    //#######//###((  ((    ))  ))###\\########\\
#   ((#######((#####\\  \\  //  //#####))########))
#    \##' `###\######\\  \)(/  //######/####' `##/
#     )'    ``#)'  `##\`->oo<-'/##'  `(#''     `(
#             (       ``\`..'/''       )
#                        \""(
#                         `- )
#                         / /
#                        ( /\  
#                        /\| \
#                       (  \
#                           )
#                          /

    
