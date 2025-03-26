def isdivisible(binarystr):
    return int(binarystr,2)%5==0
binarynum=input("Enter comma-separated 4-digit binary numbers: ").split(',')
result=[num for num in binarynum if isdivisible(num)]
print(",".join(result))
