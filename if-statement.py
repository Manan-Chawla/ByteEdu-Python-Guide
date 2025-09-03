'''
if n is odd ---> weird
if n is even and in range between 2 to 5 ---> not weird
if n is even and in range of 6 to 20 ---> weird
if n is even and greater than 20 --> not weird
'''
n=int(input("Enter value of n : "))

if n%2!=0:
    print("Weird")
elif n%2==0 or n<=2 or n >=5:
    print("not weird")
elif n%2==0 or n<=6 or n>=20:
    print("weird")
elif n%2==0 or n<=20:
    print("not weird")
else:
    print("yes pal")