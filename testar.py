x=int(input("Enter your mark"))
if x>24:
    print("You have passed the exam")
    if x>90:
        print("You have A++")
    elif x>80 and x<90:
        print("you have an A")
    elif x>70 and x<80:
        print ("you have a B")
    elif x>60 and x<70:
        print ("you have c")
    elif x>50 and x<60:
        print ("you have d")
       
else:
    print("you have failed the exam")

