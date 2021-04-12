word=str(input("Please enter your word. "))
reverse=word[::-1]
#imp; [::-1] reads the word from the back
print(reverse)
if word == reverse:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")
