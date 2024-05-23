import numpy as np
# print(np.__version__)
# arr=np.array([22,43,56,54,64])
# print(arr.dtype)
# print(arr[1:4])
# arr1=np.array(["","",""],dtype='S')
# print(arr1.dtype)
# #print(arr[1,-2])
# print(type(arr))
#COPY AND VIEW METHODS DIFFERENCE
# orgarr=np.array([22,43,56,54,64])
# copyarr=orgarr.copy()
# orgarr[0]=123
# print(orgarr)
# print(copyarr)
# viewarr=orgarr.view()
# print(viewarr)

arr=np.array([[22,43,56,54,64,55,66,77,88,99,55,66]])
for z in arr:
    print(z)
arr1=np.array([[22,43,56,54,64,55],[66,77,88,99,55,66]])
for x in arr1:
    for y in x:
        print(y)
print(arr.shape)
reshapedarr=arr.reshape(2,3,2)
print(reshapedarr)
# arr=np.array([22,43,56,54,64,55])
# arr1=np.array([66,77,88,99,55,66])
# arr2=np.concatenate((arr,arr1))
# print(arr2)

# arr3=np.array([22,43,56,54,64,55])
# arr4=np.array_split(arr3,4)
# print(arr4)

# arr4=np.array([64,22,43,34,64,56,54,64,55])
# print(np.sort(arr4))
# x=np.where(arr4%2!=0)
# print(x)