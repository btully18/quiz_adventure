# Our quiz!
count = 0
def question1():
    global count
    print("how old is the earth?")
    answer = input("answer; ")
    if answer == "no one knows":
        count = count + 1
        print("correct on to the next")
        question2()
    else:
        print("no one really knows")
        print("want to try again?")
        print("yes")
        print("no")
        answer = input("retry?, ")
        if answer == "yes":
            question1()
        elif answer == "no":
            question2()
        else:
            print("i have no time for you")
            quit()
def question2():
    print("who did you vote for? 1.donald trump, 2.hillary clinton or 3.non")
    print("use the numbers to answer")
    answer = input("answer; ")
    if answer == "1" or answer == "2" or answer == "3":
        print("cool time for the real question")
    else:
        print("sorry for asking")
    question3()
def question3():
    print("what do pokeballs do to pokemon? 1.trap them 2.enslave 3.make you friends")
    answer = input("careful pokemon may look friendly but they are very dangerous, ")
    answer = input("1 or 2 or 3, ")
    if answer == "2":
        print("i think so too!")
    else:
        print("do you really think humans would make friends with a animal that is as smart as a human but a lot more powerful")
        print("retry")
        print("time waits for no one")
        answer = input("retry?, ")
        if answer == "yes":
            print("you don't give up easy")
            question3()
        else:
            print("hahahahahahahahahahahahahahahahaha")
            question1()
    
# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    question1()
