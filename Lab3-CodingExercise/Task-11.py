print("Enter lines(press enter on a blank line to stop)")
lines=[]
while True:
    line=input()
    if line=="":
        break
    lines.append(line.lower())

print("\nOutput")
for line in lines:
    print(line)