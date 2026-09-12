#COLLECTIONS
#LIST [A, B, C, D] SOLID
#TUPLE (A, B, C, D)
#SET {A. B. C. D}
#DICTIONARY {1:A, 2:B, 3C}

#COLLECTION WITHIN COLECTION
#LIST OF LIST [[A,B,C,D],[1,2,3,4]]

#list mutable ordered duplicate
#Tuple immutable ordered duplicate
#Set mutable not ordered no duplication

myList =["apple", "banana", "cherry", "dalandan","orange"]
myTuple = ("apple", "banana", "cherry", "dalandan","orange")

myList.append("orange") #append - idagdag sa dulo
print(myList)

myList.insert(2, "Chico")
print(myList)

print(myList[0])#start (apple)
print(myList[4])#dalandan
print(myList[len(myList)-1]) #ends (orange)

print(myList.index("Chico")) #to get the position
print(myList.count("Chico")) #to get the count
myList.remove("Chico")
print(myList)

myStudents = [
    ["Name", "Age", "City", "Year", "Section"],
    ["Leonel Calderon", 20, "Pasig", "First", "One"],
    ["Mark Romualdez", 25, "Mandaluyong", "First", "Two"],
    ["Carlo Santos", 18, "Taguig", "Second", "Four"],
    ["Robert Bollic", 26, "Pateros", "Third", "One"],
]
#list of list | Second
print(myStudents[3][3])
print(myStudents[3][myStudents[0].index("Year")])