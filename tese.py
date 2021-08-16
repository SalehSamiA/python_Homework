try:
      n =int(input("please enter number 1\n "))
      if n == 1:
       print("Sandwich ", 250, "JD")
       print("Drink ", 150, "JD")
       print("French ", 150, "JD")
       print("coffee ", 250, "JD")
       print("maxicco ", 350, "JD")
       print("pizza ", 450, "JD")
       print("Donuts ", 250, "JD")
       print("Burger ", 250, "JD")
       print("HotDog ", 150, "JD")
      elif n == 2:
       print("Sandwich after discount 0.4 ", (250 / 0.4), "JD")
       print("Drink after discount 0.07", (150 / 0.7), "JD")
       print("French after discount 0.2", (150 / 0.2), "JD")
       print("coffee after discount 0.10", (250 / 0.10), "JD")
       print("maxicco after discount 0.10", (350 / 0.10), "JD")
       print("pizza after discount 0.05", (450 / 0.05), "JD")
       print("Donuts after discount 0.015", (250 / 0.015), "JD")
       print("Burger after discount 0.025", (250 / 0.025), "JD")
       print("HotDog after discount 0.3", (150 / 3), "JD")
except :
    print(" The number entered is not one of the required numbers")

else:
        print(" We wish you a wonderful visit")
finally:
    print(" Thank you for your visit")





