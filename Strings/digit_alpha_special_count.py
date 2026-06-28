text="@radhika#2019!"
digit=0
alpha=0
special=0
for ch in text:
    if ch. isdigit():
        digit+=1
    elif ch. isalpha():
        alpha+=1
    elif not ch.isalnum() and not ch.isspace():
        special+=1
print("Nnumber of digits=",digit)
print("Number of alphabets=", alpha)
print("Number of special characters=", special)
