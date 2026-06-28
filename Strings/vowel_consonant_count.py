name="nivrithi"
vowels=0
consonants=0
for ch in name:
    if ch in "aeiouAEIOU":
        vowels+=1
    elif ch.isalpha():
        consonants+=1
print("Nnumber of vowels=",vowels)
print("Nnumber of consonants=",consonants)
