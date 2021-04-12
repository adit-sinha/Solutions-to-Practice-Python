#uppercase, lowercase, numbers and symbols
import random
lc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['1','2','3','4','5','6','7','8','9','0']
sym = ['!','@','$','%','^','&','*']
pw = lc + uc + num + sym
password = random.choice(lc) + random.choice(lc) + random.choice(uc) + random.choice(uc) + random.choice(num) + random.choice(num) + random.choice(sym) + random.choice(sym)
print("Your 8-digit password is",password)
 
