Name=input("Enter your Name : ")
marks = int(input("Enter your marks : "))

if(marks >=90):
    print("Grade A")
    if marks >=95:
        print("Excellent")
elif marks >=80:
    print("Grade B")
elif marks >=70:
    print("Grade C")
else:
    print("Better luck next time ! ",Name)