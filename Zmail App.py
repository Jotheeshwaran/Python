def check_id(user_name):
    global new_user
    if len(new_user)==0:
        return True
    else:
        for k,v in new_user.items():
            if k==user_name:
                return False
        return True
    
def check_the_id_and_pw(user_name,pass_word):
    global new_user
    for k,v in new_user.items():
        if k==user_name and v==pass_word:
            return True
    return False

print("...............Welcome to Zmail...............")
print("""
    1. New account
    2. Login
    3. Exit""")
    
n1=0
new_user={}
stack={}
message_Id=1000

while n1!=3:
    n1=int(input("Enter the number: "))
    if n1==1:
        user_name=input("Enter the User Id: ")
        pass_word=input("Enter the Pass word: ")
        if check_id(user_name):
            new_user[user_name]=pass_word
            stack[user_name]=[[],[]]
            print("Account Successfully created....!")
        else:
            print("User Id already exists....!")
        print(new_user)
        print("""
    1. New account
    2. Login
    3. Exit""")
    
    if n1==2:
        user_name=input("Enter the login Id: ")
        pass_word=input("Enter the pass_ward: ")
        if check_the_id_and_pw(user_name,pass_word):
            print("%s Successfully Logged In"%(user_name))                                                     # Compose and Inbox 
            n2=0
            while n2!=6:
                print("""
            1. Compose
            2. List Mails
            3. List sent Mails
            4. Delete Mails
            5. Delete sent Mails
            6. Logout""")
                n2=int(input("Enter the number: "))
                if n2==1:                           # Compose   
                    to=list(map(str,input("Sent to :").split(",")))
                    sub=input("Subject: ")
                    msg=input("Message: ")
                    for i in to:
                        if check_id(i)==False:
                            d2={}
                            d2["message_Id"]=message_Id
                            d2["From"]=user_name
                            d2["To"]=i
                            d2["sub"]=sub
                            d2["msg"]=msg
                            stack[user_name][0].append(d2)
                            stack[i][1].append(d2)
                            message_Id+=1
                        else:
                            print("%s User Id not valid......!"%(i))
                    print(stack)

                    
                elif n2==2:
                    print("Inbox")
                    if len(stack[user_name][1])==0:
                        print(".....Empty.....")
                    else:
                        for i in stack[user_name][1]:       # inbox
                            print(i)

                elif n2==3:                         # sent mails
                    print(".....Sent Mails.....")
                    if len(stack[user_name][0])==0:
                        print("......Empty......")
                    else:
                        for i in stack[user_name][0]:
                            print(i)
                            
                elif n2==4:
                    print(".....Delete Inbox Mails.....")
                    if len(stack[user_name][1])==0:
                        print("There is no mail to delete")
                    else:
                        e=input("Enter the delete mail: ")
                        f=0
                        for i in stack[user_name][1]:
                            if i["From"]==e:
                                stack[user_name][1].remove(i)
                                f=1
                                break
                        if f==1:
                            print("Mail Successfully Deleted.....!")
                        else:
                            print("Mail Id not found")
                
                elif n2==5:
                    print(".....Delete the sent mail.....")
                    if len(stack[user_name][0])==0:
                        print("There is no mail to delete")
                    else:
                        f=0
                        e=input("Enter the delete mail: ")
                        for i in stack[user_name][0]:
                            if i["To"]==e:
                                stack[user_name][0].remove(i)
                                f=1
                                break
                        if f==1:
                            print("Mail Successfully Deleted.....!")
                        else:
                            print("Mail Id not found")
                        
                elif n2==6:
                    print("Successfully Loggedout")
                    break
        else:
            print("Check the User Id and Password....!")
        print("""
    1. New account
    2. Login
    3. Exit""")
    if n1==3:
        print("Successfully Existed.....!")
        break
            
            
