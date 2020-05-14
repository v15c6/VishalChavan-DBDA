list1 = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
	no = int(input())
	list1.append(no) 	
print(list1) 
list2 = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
	no1 = int(input())
	list2.append(no1) 	
print(list2)
le=[]
lo=[]
for i in list1[1::2]:
    lo.append(i)
print(lo)
for j in list2[0::2]:
    le.append(j)
print(le)
list3=le+lo
print(list3)
