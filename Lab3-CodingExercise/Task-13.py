text=input("Enter string: ")
letter_count=0
digit_count=0
for char in text:
    if char.isalpha():
        letter_count+=1
    elif char.isdigit():
        digit_count+=1
print("Letters",letter_count)
print("Digits",digit_count)