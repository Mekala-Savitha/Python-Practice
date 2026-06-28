word="RiThAnyA"    
upper=0
lower=0
for ch in word:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
print("Number of uppercase letters=", upper)
print("Number of lowercase letters =", lower)
