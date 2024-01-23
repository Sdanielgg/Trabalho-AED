from tkinter import*
import home
import signUp
def loggedChecker():
    f=open("files\\users.txt","r",encoding="utf-8")
    lines=f.readlines()
    f.close()
    x=0
    for line in lines:
        content=line.strip().split(";")
        print(content[3])
        if  (content[3]=="Logged"):
            x=+1
    if x==1:
        home.main()
    else:
        signUp.main()
                    
loggedChecker()

