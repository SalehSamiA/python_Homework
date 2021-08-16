s=98
class student :
    s=40
    print(s)


    firstname=""
    Lastname=""
    avg=0.0
    SID=""
    Major=""

s=student()
print(type(s))
s.firstname="Saleh"
s.Lastname="Sami"
s.SID="31818001052"
s.Major="CS"
print(s.firstname +" "+s.Lastname+" "+s.Major+" "+s.SID)

class car:

 def __init__(self,color,p,e,t) :
    self.engin = e
    self.color =color
    self.price = p
    self.type = t
 def print(self):
        print(self.type," ",self.color," ",self.engin," ",self.price)
car1=car("Blake",7000,1500,"Hondi")
car2=car("Blake",15000,2100,"Kia")
car1.print()
car2.print()
