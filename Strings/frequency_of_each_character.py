text="banana"
printed=""
for ch in text:
    if ch not in printed:
        print(ch,"=", text.count(ch))
        printed+=ch
