student={"role":100,"name":"akhil","course":"mca"}

print(student["name"])

if "total" in student:
    print("exist")
else:
    student["total"]=150
print(student)

student["total"]+=50
print(student["total"])
