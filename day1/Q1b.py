list= [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
	no = int(input())
	list.append(no) 	
print(list) 
reverse=list[::-1]
print(reverse)
