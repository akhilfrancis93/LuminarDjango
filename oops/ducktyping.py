class Swift:
    def start(self):
        print("swift can start")
    def accelerate(self):
        print("swift accelerate")
    def stop(self):
        print("swift stop")

class Celtos:
    def start(self):
        print("celtos can start")

    def accelerate(self):
        print("celtos accelerate")

    def stop(self):
        print("celtos stop")
class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.stop()

sw=Swift()
p=Person()
p.drive(sw)
