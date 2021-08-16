#Write a function to input integer values into 2D array
#•Write a function to print out 2D array
#•Write a function to Array Transformations by  flip rows and columns
#•Write a function to sum the main dialog in 2d
#•Write a function to return the sum of the element under the main dialog.
import numpy as np
       def inputArray():
          print("please Enter 5 integer into 2 Array")
          arr=np.array([[input()],[input()]])
       def PrintArray():
            x=inputArray()
            print(x)
       def Transformations():
            y=np.array([2,3,2,4],[2,3,4,5])
            print(y.T)
            print(y.transpose())
Transformations()


