#Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.
def pel():
    a=int(input("enter number:"))
    if isinstance(a,int):
        a=str(a)
        b=a[::-1] 
        if a==b:
            print("it is pelindron")
        else:
            print(" it is not pelindron")
    else:
        print("the number is not integer")
pel()
 
