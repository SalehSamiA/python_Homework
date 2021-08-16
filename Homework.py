class resturant:
    print("Wellcome To Fast Food Resturant")

    def _init_num(n):
        try:
            n = int(input("please enter number 1 OR 2 \n "))

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
                print("Sandwich after discount 0.4 : ", abs((2.50 * 0.4)-2.5), "JD")
                print("Drink after discount 0.07 :", abs((1.50 * 0.07)-1.50), "JD")
                print("French after discount 0.2 :", abs((1.50 * 0.2)-1.50), "JD")
                print("coffee after discount 0.10 :",abs( (2.50 * 0.10)-2.5), "JD")
                print("maxicco after discount 0.10 :", abs((3.50 * 0.10)-3.5), "JD")
                print("pizza after discount 0.05 :", abs((4.50 * 0.05)-4.50), "JD")
                print("Donuts after discount 0.015 :",abs ((2.50 * 0.015)-2.50), "JD")
                print("Burger after discount 0.025 :",abs ((2.50 * 0.025)-2.50), "JD")
                print("HotDog after discount 0.3 :",abs ((1.50 * 0.3)-1.50), "JD")
        except:
            print(" The number entered is not one of the required numbers")

        else:
            print(" We wish you a wonderful visit")
        finally:
            print(" Thank you for your visit")


while True:

    s = resturant()
    s._init_num()