from stegano import lsb
import spy_details

chat=[]
def checkAge(age):
    "To constrain the age of the spy"
    while True:
        # the age should be numerical
        if age.isalpha() == True:
            age = input("Enter correct age: ")
            continue
        # the age should lie in 12,50
        elif int(age) not in range(12, 50):
            print("You are not of appropriate age")

        else:
            break
def checkRating(rating):
    "To constrain the age of the spy"
    while True:
        # the rating should be numerical
        if rating.isalpha() == True:
            rating = input("Enter correct rating: ")
            continue
        elif int(rating) >=8 and int(rating)<=10:
            print("***You are good ace***\n")
            break
        elif int(rating) <8 and int(rating)>=5:
            print("***You are average***\n")
            break
        elif int(rating) <5 and int(rating)>=1:
            print("***You can do better***\n")
            break
        elif int(rating) >10 or int(rating)<0:
            rating=input("Enter rating from 0 to 10")
            continue

#imports the name of the default user
user_name="Mr. Rohit"
user_age=14
user_rating=8
test=input("Do you want to continue as {}? (y/n)".format(user_name))
while True:
    if test.upper()=='Y':
        print("Welcome {}, glad to have you back! \n".format(user_name))
        break
    elif test.upper()=='N':
        user_name=input("Hi! Welcome to Spychat. What is your name? ")
        print("Welcome {}, glad to have you with us! \n".format(user_name))
        prefix = input("What should we call you?? (Mr/Ms) ")
        user_name = prefix + " " + user_name
        print("Alright {} \n ***I'd like to know more about you***\n".format(user_name))
        user_age = input("What's your age?: ")
        checkAge(user_age)
        # takes the rating of the user
        user_rating = input("What's your spy rating?(out of 10): ")
        checkRating(user_rating)
        print("***Authentication complete***\n")
        break
    else:
        test=input("Enter appropriate answer.\n")
        continue

#introduction of the user

print("Spy name: {}\n Spy age: {}\nSpy Rating: {}\n".format(user_name,user_age,user_rating))
#choose menu for different menu
print("Proud to have you onboard!! :\n")
while(True):
    action=input("What do you want to do?\n1. Add a status update\n2. View status \n3. Add a friend\n4. Send secret message\n5. Read secret message\n6. Read Chat history\n7. Close the Application\n")

    #update a status
    if action=='1':
        newstatus=""
        sts=input("1. Choose from existing status\n2. Enter a new status\n")
        status=["Busy","No calls, Spychat only","Sleeping","Coding"]
        if sts=='1':
            i=0
            while i<len(status):
                print("\n{}. {}".format(i+1,status[i]))
                i+=1
            sts1=int(input("\nWhich status you want to add?\n"))
            print("Your current status is now {}\n".format(status[sts1-1]))
            newstatus=status[sts1-1]
        elif sts=='2':
            newstatus=input("Enter a new status: \n")
            status.append(newstatus)
            print("Your current status is now {}\n".format(newstatus))
    elif action == '2':
        if newstatus!=None:
            print("Your current status is {} \n".format(newstatus))
        else:
            print("You dont have added status now\n")
    elif action == '3':
        spy_name=input("Enter the name of your spy friend\n")
        spy_age=input("Enter your friend's age \n")
        checkAge(spy_age)
        spy_rating=input("Enter your friend's rating(out of 10)\n")
        if int(spy_rating) < int(user_rating) or int(spy_rating)>10:
            print("You cannot add this friend\n")
            continue
        print("Spy friend's name: {}\nSpy friend's age: {}\nSpy friend's rating: {}\n".format(spy_name,spy_age,spy_rating))


    elif action == '4':
        print("Your friends are\n")
        for k in spy_details.friends:
            print("{}. {}".format(k,spy_details.friends[k][0]))
        k=int(input("\n Which friend you want to text\n"))
        print("Spy Friend name: {}\nSpy friend age: {}\nSpy friend rating: {}\n".format(spy_details.friends[k][0],spy_details.friends[k][1],spy_details.friends[k][2]))
        text = input("Enter the secret message\n")
        secret = lsb.hide("/home/lakshay/Downloads/test.jpg", text)
        secret.save("/home/lakshay/Downloads/test_decode.jpg")
        print("***  Secret message has been sent ***")
        a=[]
        a.append(spy_details.friends[k][0])
        a.append(text)
        chat.append(a)
    elif action == '5':
        print("Whose message you want to read\n")
        for k in spy_details.friends:
            print("{}. {}".format(k,spy_details.friends[k][0]))
        k = int(input("\n Which friend you want to text\n"))
        i=0
        while(i<len(chat)):
            if spy_details.friends[k][0] in chat[i]:
                print("{}: {}".format(chat[i][0],chat[i][1]))
                i=i+1
    elif action == '6':
        print("Your recent chats are\n")
        k=1
        while(k<=3):
            i=0
            while (i < len(chat)):
                if spy_details.friends[k][0] in chat[i]:
                    print("{}: {}".format(chat[i][0], chat[i][1]))
                    i = i + 1
            k=k+1
    elif action == '7':
        break

