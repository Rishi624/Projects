

















 


















# a = 4
# b = "4"
# print(a==b) # Checks value is same or not
# print(a is b) #Checks memory location is same or not
#location is not same for two same lists but same for tuples as they are immutable means python fixes same location for constants

# a = [1,2,3,4,5]
# b = list(map(lambda x:(x/2),a)) #maps each element with function and operates that function on it. In place of lamda you cang give function name if it is defined
# print(b)

# a = [1,2,3,4,5]
# b = list(filter(lambda x:x>2,a))
# print(b)

#reduce this function should be imported from module functools
# from functools import reduce
# num = [1,2,3,4,5]
# b = reduce(lambda a,b:a+b,num)
# print(b)

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# result = list(zip(list1, list2))
# print(result)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')] This is also applicable for tuples also

# llist = [1,1,1,2,3,3,4,4,5]
# variable = list(dict.fromkeys(llist)) #print(variable)  prints list without repetition of elements

# f = open('myfile.txt','r')#Here myfile.txt is name of your file and r is for read mode and w is for write mode a is for append mode
# If we not write anything like 'r' read mode r will be taken as default and also similarly x for creating file

# content = f.read()  # Reads the entire file content into a string and also if we write any number in () it will read that many characters only
# print(content)
# f.close() #File will be closed and we cannot read contents

# marks = [1,2,3,4,5,6,7]
# for index,mark in enumerate(marks):
#     print(mark)
#     if(index==3):
#         print("You got two marks")

# a = int(input("Enter between 5 and 9"))
# if(a<5 or a>9 or a!="quit"):
#     raise ValueError("Enter a valid number")

# def func1():
#   try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
#     return 1
#   except:
#     print("Some error occurred")
#     return 0

#   finally:
#     print("I am always executed")#Try without writing finally then you will understand
# x = func1()
# print(x)

# rollno = {
#     "Rishi" : 2024104830,
#     "Sushi" : "18SJCB0106" 
# }
# print(rollno["Rishi"])
# print(rollno["Sushi"])
# print(rollno.keys())
# for key,value in rollno.items():
#     print(f"Value of key {key} is {value}")
# rollno.pop("Rishi") #Removes key and value. If you use .popitem then it removes last key value pair
# Instead of pop item you can use del rollno["Rishi"]
# rollno.count(x)
# If you want to combine two dicts just do dict1.update(dict2)

# def square(n):
#     '''Take value of n''' 
#     print(n**2)
# square(5)
# print(square.__doc__)
# Docstrings and comments are not same doc strtings are read and can be printed by this
# And also doc strings are used for clases and def

# Cororpati
# questions = [
#     ['Full form of g in gitam','Gaffa','Gukwa','Gandhi','None',3],
#     ['Full form of g in gitam','Gaffa','Gukwa','Gandhi','None',3],
#     ['Full form of g in gitam','Gaffa','Gukwa','Gandhi','None',3],
#     ['Full form of g in gitam','Gaffa','Gukwa','Gandhi','None',3],
# ]

# cash = [10000,20000,50000,100000]
# your_money = 0
# for i in range(0,len(questions)):
#     question = questions[i]
#     print(f"Question for Rs. {cash[i]} is {questions[i]}")
#     print(f"1. {question[1]}    3. {question[2]}")
#     print(f"3. {question[3]}    4. {question[4]}")
#     reply = int(input("Enter answer number"))
#     if reply==question[-1]:
#         print(f"Correct answer you won Rs. {cash[i]}")
#         your_money+=cash[i]
#         print(f"Ypu won a total of Rs. {your_money}")
#     else:
#         print(f"Better luck next time")
#         break

# precision_value = format(123.4567, '.2f')
# print(f"For only {price:.2f} rupees")
# l = [1,123,3,3,"j hbtrgkioer"]
# print(l)
# l.append("fxjk")#adds element to list
# l.sort(reverse = True)#sets in ascending order not applicable is strings are present. If true descending order
# l.insert(1,899) #It assigns 899 at index 1
#print(t.index(3)) prints index of 3 if two are there it prints first one
# print(l)
# m = [10,20,30]
# l.extend(m)#ELements of m will add lo  l at last positions
# k = l+m #I you want to add two lists
# var = l.copy()#Copies to var
#l.count(3)#Counts how many times 3 came in list
#l.pop(3)#It removes elemt 3 from list not applicable to tuples
#  lst = [i*i for i in range(1,10) if i%2==0]
# print(lst)

# import time
# var = time.strftime('%H:%M:%S')#prints time int that format if we need only hours write only %H similarly others

