String1=input("Enter String 1")
String2=input("Enter String 2")
def Middle(String1, String2):
  Index = int(len(String1) /2)
  String3= String1[:Index-1:]+ String2 +String1[Index-1:]
  print("appending String2 in String1", String3)
  
String3=Middle(String1,String2)
