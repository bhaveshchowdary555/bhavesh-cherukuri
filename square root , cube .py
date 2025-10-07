i = int(input("enter i value :"))
print("1.square")
print("2.square root")
print("3.cube")
opp = int(input("enter your command :"))
if opp==1:
    print(i**2)
elif opp==2:
    print(i**0.5)
elif opp==3:
    print(i**3)
else :
    print("wrong choice")