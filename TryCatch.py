try:
      n1 =int(input("please enter number 1\n "))
      n2 = int(input("please enter number 2 \n"))
      print("deveid is :",n1/n2)
except ValueError:
        print("please enter integer number")
except ZeroDivisionError:
        print("must enter  secound number not zero")
else:
        print("everything good")
finally:
        print("good luck")




