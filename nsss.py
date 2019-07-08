new=int(input(" "))
if(new%4==0 and new%100!=0 or new%400==0):
    print("yes")
else:
    print("no")