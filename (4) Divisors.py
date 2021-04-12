usern = int(input("Enter your number."))
a = range(1,usern+1)
print("The factors of", usern, "are:")
for number in a:
    if usern%number==0:
        print(number)
