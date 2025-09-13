'''your friend is throughing a birthday party and she
is confused about finalising the guests for the 
birthday party.
write a simple program to organize the guest list
where
1.To view the guest list
2.To add the guest
3.To check the particular guest is attending the 
party or not
4.Remove a guest from guest list
5.To print the finalized guest list and exit.'''




Guest_list=[]
while(True):
    print("______Guest List Menu______")
    print("1.To view the Guest List")
    print("2.To Add a Guest")
    print("3.Check the guest is attending the party or not")
    print("4.To Remove a Guest")
    print("5.Print Finalized Guest List")
    choice=int(input('Enter Your Choice :'))
    if(choice==1):
        if(len(Guest_list)==0):
            print("Guest List is Empty")
        else:
            print("Guest List :")
            print(Guest_list)
        print()
    elif(choice==2):
        guest=input("Enter the Guest Name :")
        Guest_list.append(guest)
        print(f"{guest} is added to the guest list.....!")
        print()
    elif(choice==3):
        guest=input("Enter the guest name to check the status of the guest:")
        if guest in Guest_list:
            print(f"{guest} is Attending the party......!")
        else:
            print(f"{guest} is Not Attending the party......!")
        print()
    elif(choice==4):
        guest=input("Enter the name of the guest who's not attending the party")
        if guest in Guest_list:
            Guest_list.remove(guest)
            print(f"{guest}'s name is removed from the guest list.....!")
        print()
    elif(choice==5):
        print("Finalized Guest List:")
        print()
        print(Guest_list)
        break