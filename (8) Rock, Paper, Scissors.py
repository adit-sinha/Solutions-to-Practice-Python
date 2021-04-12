a = 1
print("1 = Rock")
print("2 = Scissors")
print("3 = Paper")
while a == 1:
    b = 1
    user1 = int(input("Please make a choice 1/2/3. "))
    user2 = int(input("Please make a choice 1/2/3. "))
    if user1 == user2:
        print("The result is a draw.")
    elif user1 == 1 and user2 == 2:
        print("User 1 wins!")
    elif user1 == 2 and user2 == 3:
        print("User 1 wins!")
    elif user1 == 3 and user2 == 1:
        print("User 1 wins!")
    elif user2 == 1 and user1 == 2:
        print("User 2 wins!")
    elif user2 == 2 and user1 == 3:
        print("User 2 wins!")
    elif user2 == 3 and user1 == 1:
        print("User 2 wins!")
    elif user1 != 1 or user1 != 2 or user1 != 3 or user2 != 1 or user2 != 2 or user2 != 3:
        print("Invalid Reply.")
    else:
        print("Invalid Reply.")
    while b == 1:
     print("1 = Yes")
     print("2 = No")
     confirm = int(input("Would you like to play again? "))
     if confirm == 1:
        a = 1
        b = b + 1
     elif confirm == 2:
        a = a + 1
        b = b + 1
     else:
        print("Invalid Reply.")    
  
