print("------------------------------------")
print("------ticket pricing software-------")
print("------------------------------------")

print("please enter your age : ")
Age = int(input())

if(Age <= 5): 
    print("free entry")
elif(Age > 5 and  Age <= 18):
    print("ticket price : 900")
elif(Age >18 and Age <= 40):
    print("ticket price : 1200")
else:
    print("ticket price : 500")

