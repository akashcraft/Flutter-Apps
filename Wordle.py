#Made by AkashCraft
import time,random
def startup():
    print("+","-"*53,"+",sep="")
    print("|"," "*17,"Welcome to Wordle"," "*19,"|",sep="")
    print("+","-"*53,"+",sep="")
    print("+","-"*53,"+",sep="")
    print("|"," "*15,"Coded by Akash Samanta"," "*16,"|",sep="")
    print("+","-"*53,"+",sep="")
def instructions():
    print()
    print("You have 6 guesses to guess a random five letter word.")
    print("Correct Alphabets entered with exact matching position will appear as 2.")
    print("Correct Alphabets entered with incorrect position will appear as 1.")
    print("However Incorrect Alphabets entered, which are not in the word will appear as 0.")
    print()
    print("ATTENTION! Please save the code in the folder it came with. Or else the game will not run correctly.")
    print("Type /quit to stop the game.")
    print("Type /credit to show credits.")
    print("Type /restart to get a new word and restart the game.")
    print("Type /help to get these instructions back.")
    print()
def credit():
    print()
    print("+","-"*53,"+",sep="")
    print("|"," "*15,"Coded by Akash Samanta"," "*16,"|",sep="")
    print("+","-"*53,"+",sep="")
    print()
def getrandom():
    f1=open("Answers.txt","r")
    s=f1.read()
    L=s.split('\n')
    tot=len(L)
    #Remove hash for debugging
    #print("Correctly fetched",tot,"words")
    ran=random.randint(0,tot-1)
    cword=L[ran]
    #print("The random selected word is",cword)
    cword=cword.upper()
    f1.close()
    return cword
def getallowable():
    f1=open("Allowable.txt","r")
    s=f1.read()
    L=s.split('\n')
    f1.close()
    return L
def getanswer():
    f1=open("Answers.txt","r")
    s=f1.read()
    L=s.split('\n')
    f1.close()
    return L
def inputcheck():
    L2=['/QUIT','/HELP','/CREDIT','/RESTART']
    while True:
        ans1=input("Enter your guess: ")
        ans1=ans1.upper()
        if ans1 in L2:
            if ans1=='/QUIT':
                q='/quit'
                return q
            elif ans1=='/CREDIT':
                credit()
            elif ans1=='/RESTART':
                print("Game restarted")
                print()
                main()
            else:
                instructions()
        else:
            if len(ans1)==5:
                return ans1
            else:
                print("Please enter a five letter word only. No Guesses deducted. Try again.")
def printbox(w):
    print()
    print("+","-","+"," ","+","-","+"," ","+","-","+"," ","+","-","+"," ","+","-","+")
    print("|",w[0],"|"," ","|",w[1],"|"," ","|",w[2],"|"," ","|",w[3],"|"," ","|",w[4],"|")
    print("+","-","+"," ","+","-","+"," ","+","-","+"," ","+","-","+"," ","+","-","+")
    print()
def printbox1():
    print()
    print("+","-","+"," ","+","-","+"," ","+","-","+"," ","+","-","+"," ","+","-","+")
    print("|",' ',"|"," ","|",' ',"|"," ","|",' ',"|"," ","|",' ',"|"," ","|",' ',"|")
    print("+","-","+"," ","+","-","+"," ","+","-","+"," ","+","-","+"," ","+","-","+")
    print()
def printliner(w):
    print(" ",w[0]," "," "," ",w[1]," "," "," ",w[2]," "," "," ",w[3]," "," "," ",w[4]," ")
    print()
def restart():
    ans2=input("Do you want to restart the game?: ")
    while ans2.upper() not in ['YES','NO','N','Y']:
        print("Please enter YES/NO: ")
        ans2=input("Do you want to restart the game?: ")
    if ans2.upper() in ['YES','Y']:
        print("Game restarted")
        print()
        main()
    else:
        return '/quit'
startup()
instructions()
def main():
    cword=getrandom()
    print("Word Ready. Start guessing!")
    printbox1()
    ans=''
    lives=6
    L3=getallowable()
    L6=getanswer()
    L3=L3+L6
    L4=[]
    keyboard=[]
    for i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        keyboard.append(i)
    while ans!='/quit':
        if lives==0:
            print("You ran out of guesses! The word was",cword)
            printbox(cword)
            ans=restart()
            if ans=='/quit':
                continue
        else:
            ans=inputcheck()
            if ans.lower() not in L3:
                print("This is not a word. No Guesses deducted. Try again.")
                continue
            else:
                if ans==cword:
                    print("Congragulations! You got the word. It was",cword)
                    printbox(cword)
                    ans=restart()
                    if ans=='/quit':
                        continue
                else:
                    lives=lives-1
                    Liner=[]
                    for i in range(5):
                        if ans[i] in cword:
                            lock=i
                            if ans[lock]==cword[lock]:
                                Liner.append(2)
                            else:
                                Liner.append(1)
                        else:
                            Liner.append(0)
                            if ans[i] not in L4:
                                q=keyboard.index(ans[i])
                                L4.append(ans[i])
                                keyboard[q]=' '
                    printbox(ans)
                    printliner(Liner)
                    print('Available Guesses: ',lives)
                    print("Available keyboard characters: ")
                    for j in range(len(keyboard)):
                        if j in [9,18,25]:
                            print(keyboard[j],end='\n')
                        else:
                            print(keyboard[j],end=' ')
                    print()
    else:
        print("Thank you playing!")
        quit()
main()


