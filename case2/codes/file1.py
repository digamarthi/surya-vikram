# def add(a,b):
#     return a+b
# x = add(10,20)  #here x is variable used to store a values
# print(x)
#
#
# def myfun(name):         # here name is called as parameter or aurgements or values
#     print("surya bhai",name)
#
# myfun("gulabii ")
#
# def mylife(a,b):
#     return a-b
# print(mylife(10,20))
#
#
# xy = 100
#
# def cool():
#     global xy
#     xy=420
#     print(xy)
# cool()
#
# print(xy)
#
#
# def print_all():
#     print("a")
#     print("b")
# def print_all():
#     print("c")
#     print("d")
# print_all()
#
# data1 = [1,2,3,4]
# data2 = [5,6,7,8,2,4]
# data3=[]
#
# for i in data1:
#     if i in data2:
#         data3.append(i)
# print(data3)

# def com_list(a,b):
#     # global data3
#     data3 = []
#     for i in data1:
#         if i in data2:
#             data3.append(i)
#     #print(data3)
#     return data3
#
# data1 = [1,2,3,5]
# data2 = [6,67,1,5]
# out= com_list(data1,data2)
# print(out)
#
# # print(data3)

# def test1(*arg12):
#     print("arg12.032"
#           " is",arg12,type(arg12))
#     print("***********************")
# test1(1,2,3,4,4)
# test1("asjdj")
# test1()
# x = [12,34,11]
# y = [33,44,55]
# test1(x,y)


#oops

# class myclass:
#     def test1(self):
#         print("hi")
#     def test2(x,name):
#         print("my name",name)
#
# x = myclass()
# x.test1()
# x.test2("mahi")

list1 = ["hi", "vinay", "this", "work12"]

# Iterate through the list
for item in list1:
    # Check if the item contains digits
    if any(char.isdigit() for char in item):
        print(f"'{item}' contains a number")


list1 = ["hi", "vinay", "this645", "work12"]

for item in list1:
    has_number = False
    for char in item:
        if char.isdigit():
            has_number = True
            break
    if has_number:
        print(item)


















































































