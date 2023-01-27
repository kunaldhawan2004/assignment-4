y=int(input("enter some year :"))
if y%4==0 and y%100!=0:
    print("this year is leap year")
elif y%400==0:
    print("this is a leap year")
else :
    print("this is not a leap year")
 
