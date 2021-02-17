students={
    1000:{"id":1000,"name":"akhil","course":"django","qualification":"btech"},
    1001:{"id":1001,"name":"sukesh","course":"django","qualification":"btech"},
    1002:{"id":1002,"name":"jamsheer","course":"django","qualification":"btech"},
    1003:{"id":1003,"name":"nikhil","course":"django","qualification":"btech"},
    1004:{"id":1004,"name":"gokul","course":"django","qualification":"mca"},
}

def get_students(**kwargs):
    id=kwargs("id")
    prop=kwargs("property")
    if id in students:
        print(students[id]["name"])
    if prop in students[id]:
        print(students[id]["prperty"])
    else:
        print("invalid")
        else:
        print("doesnot exist")
get_students(id=1000,prop="course")