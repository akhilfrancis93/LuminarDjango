students={
    1000:{"id":1000,"name":"akhil","course":"django","qualification":"btech"},
    10001:{"id":1001,"name":"sukesh","course":"django","qualification":"btech"},
    1002:{"id":1002,"name":"jamsheer","course":"django","qualification":"btech"},
    1003:{"id":1003,"name":"nikhil","course":"django","qualification":"btech"},
    1004:{"id":1004,"name":"gokul","course":"django","qualification":"mca"},
}
id=int(input("enter student id"))
property=input("enter student property")
if id in students:
    print(students[id]["name"])
    if property in students[id]:
        print(students[id][property])
    else:
        print("invalid property")
else:
    print("invalid")