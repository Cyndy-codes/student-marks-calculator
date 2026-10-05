import os
print("program folder",os.getcwd())
def get_mark(subject):
    while True:
        try:
            mark=float(input("Enter" + subject + "mark"))
            if mark<0 or mark>100:
                print("invalid marks")
            else:
                return mark
        except ValueError:
           print("please enter a number")
def get_grade(average):
    if average>=70:
        return"A"
    elif average>=60:
        return "B"
    elif average>=50:
        return "C"
    elif average>=40:
        return "D"
    elif average>=30:
        return "E"
    else:
        return "E"

while True:
    print("\n----STUDENTS MARKS CALCULATOR-----")
    print("1.Enter students marks:")
    print("2.View saved results:")
    print("3.Exit:")

    choice=input("enter your choice:")

        
    if choice == "1":
        name=input("Enter students name:")
        math=get_mark("Math")
        english=get_mark("English")
        networking=get_mark("Network")
        kiswahili=get_mark("Kiswahili")


        total=math+english+kiswahili+networking
        average=total/4
        grade=get_grade(average)

        print("\n---STUDENTS  RESULT-----")
        print("Total:",total)
        print("Average:",average)
        print ("Grade:",grade)
    if choice == "1":
        with open ("student_results.txt","a") as file:
            file.write("Student:" +name + "\n")
            file.write("Total:" +str(total)+ "\n")
            file.write("Average:"+str(round(average,2))+ "\n")
            file.write("Grade:" +grade+"\n")
            file.write("\n------------------------" )
            print("Result saved successfully")
            print("The file has been saved")


    elif choice == "2":
        print("\n-----SAVED RESULTS-----")
        try:
            file= open("student_results.txt","r") 
            print(file.read()) 
                 
            file.close()
        except FileNotFoundError:
            print("No saved  results yet.")
        input("press Enter to run to the menu...")  

    elif choice == "3":
        print("Thanks for choosing Students Marks Calculator")
        break
    else:
        print("invalid choice")