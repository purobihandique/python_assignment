students=[]

def addStu(students,id,name,grade):
    for stu in students:
        if stu["id"] == id:
            print(f"student with id : {id} already exist...")
            return

    new = {"id":id,"name":name,"grade":grade}
    students.append(new) 
    print(f"student {name} is added successfully...")

def display(students):
    if len(students)==0:
        print("no studnt record found")
    else:
        for std in students:
            print(f"id : {std["id"]} , name : {std["name"]}, grade= {std["grade"]}")
        

addStu(students,1,"Pallab","A")
addStu(students,1,"Pal","A")

display(students)