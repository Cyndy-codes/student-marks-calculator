# get marks
def get_mark(subject):
    while True:
        try:
            mark=float(input(f"Enter{subject}mark:"))
            if 0<=mark<=100:
                return mark
            print("invalid mark.enter a mark between 0 and 100")
        except ValueError:
            print("please enter a number")

# calculate total and average
def calculate_results(marks):
    total=sum(marks)
    average=total/len(marks)
    return total,average

# calculate grade
def get_grade(average):
    if average>=80:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:
        return "C"
    elif average>=50:
        return "D"
    else:
        return "E"
    
#saved  results
def view_results():
    try:
        with open("students_results.txt","r") as file:
            results =file.read()
            print("\n---saved results----")
            print(results)
    except FileNotFoundError:
        print("\nNo saved results found yet.")

#students menu
print("\n----students marks calcultor-----")
print("1.enter a new student")
print("2.view saved results")
print("3.exit")

choice=input("enter your choice")

if choice=="1":
    print("\n enter students details:")
name=input("enter the name")
math=get_mark("math")
english=get_mark("english")
networking=get_mark("networking")
computerstudies=get_mark("computerstudies")
Database=get_mark("database")

# calculate total and average
marks=[math,english,networking,Database,computerstudies]
total, average,=calculate_results(marks)

#calculate grade
grade=get_grade(average)

#display results
print("\n ----students results------")
print("name",name)
print("total:",total)
print("average",average)
print("grade",grade)

# save results
with open("students_results.txt","a") as file:
    file.write(
        f"{name}-Math:{math},english:{english},"f"networking:{networking},database:{Database}"
        f"computer studies:{computerstudies},totla:{total},"f"average:{average},grade{grade}\n")
    print("results saved succesfully")
    view_results()
if choice =="2":
    view_results()

if choice =="3":
    print("goodbye")

