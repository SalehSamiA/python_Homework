class item :
    name=" "
    price=0.0
    def __init__(self,name,price) :
      self.name=name
      self.price=price
    def printItem(self):
        print(self.name , "-->" , str(self.price))
    def discount(self , discount):
            self.price = self.price - self.price * discount
class Menu:
    def __init__(self):
        self.items=[
            item("humbrger",5.0),
            item("wings", 2.0),
            item("rice", 1.5),
            item("sald", 2.5)
        ]
    def printMenu(self):
      for item in self.items :
          item.printItem()
    def discountMenu(self,discount):
        if discount >= 0.05 and discount <= 0.4 :
            for item in self.items:
                item.discount(discount)
                item.printItem()
        else:
            print("wrong discount")

print("welcome to our resturant")
while True:
    print("\n******************")
    print("please input your choice")
    print("1 - print menu")
    print("2 - print discount")
    menu=Menu()
    try:
        choice=int(input())

        if  choice==1:
            menu.printMenu()
        elif choice==2:
            print("input discount between 0.05 and 0.4")
            discount=float(input())
            menu.discountMenu(discount)
        else:
         print("wrong input")
    except ValueError:
        print("wrong input")

