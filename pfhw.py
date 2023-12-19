#remove duplicate from the list without using set() in python
i=1
mylist =[1,2,3,4,5,6,7,8,9]
newlist=[]
for i in mylist:
    if i not in newlist:
        newlist.append(i)
print(mylist)
print(newlist)





#add two matrix
a=[[3,5][4,6]]
b=[[6,4][5,3]]
for i in a:
    print(i)
    for i in a:
     print(b)
for i in range(1):
   for j in range(1):
      c=a[i][j]+b[i][j]
print("the sum of two matrix is :" ,c)









