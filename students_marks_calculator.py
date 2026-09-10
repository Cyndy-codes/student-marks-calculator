name=input("enter your name:")
math=int(input("enter math mark:"))
english=int(input("enter english mark:"))
networking=int(input("enter networking mark:"))
database=int(input("enter database mark:"))
computerstudies=int(input("enter computer studies mark"))

total=math+english+networking+database+computerstudies
average=total/5
if average >=80:
    grade="A"
elif average >=70:
    grade="B"
elif average >=60:
    grade="C"
elif average >=50:
    grade="D"

else:
    grade="E"

print("\n----STUDENTS PROJECT----")
print("student:", name)
print("total:", total)
print("average:", average)
print("Grade:", grade)
print("Thank you for using the students_marks_calculator")