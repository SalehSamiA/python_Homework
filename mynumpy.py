import numpy as np
x=np.array([[1,2,3,4,5],
           [4,5,6,12,7],
           [1,23,45,6,7]
           ])


y=np.array([[6,2,3,4,5],
           [4,5,6,12,4],
           [1,23,45,4,7],
           [1,3,2,5,3],
            [4,6,7,8,9]])
print(x)
print(x.shape)
print(x.reshape(15))
print(np.where(x == 4))
print(np.dot(x,y))
print(x.T)
print(x.transpose())
print(x.T.shape)