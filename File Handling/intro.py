#to open  a text file
# f = open('demo.txt',"r")   #variable in which file is stored is called the file handler
# print(f.read())
# print(f.readline()) #reads the entire program line by line

#while using write function, if the file doesnt't exist, it will create a file

# f1 = open("demo1.txt", "w")
# f1.write("Hi!!\n")
# f1.write("I am Onkar!\n")
# for i in f:
#     f1.write(i)
# f1.close()   #specifically telling the system to close the file
# try:    #Used to execute what is in finally even if error in functions in try block
#     f2 = open("demo3.txt","w")
#     f2.write("H1!!\n")
#     f2.write("This is a new file\n")
#     f2.write("made using try and finally block.\n")
#     f2.write("This is an important concept.\n")
#     #your code goes here
# finally:
#     f.close()
#This way we are making sure that fie is closed properly even if exception is raised that cause the program flow to stop

# another way is using with method
#In this we dont have to specify close method, it by default closes file when done

# #syntax: with ____ as file handler:
# with open("demo.txt") as f:
#     f.read() #example
#    # your code here

# f =open("demo.txt","r")
# print(f.read(10))
# print(f.tell())

# f = open("img.jpg",'rb') #in case of image file we use rb, it prints the binary of image
# copy = f.read()
# f1 = open("img_copy.jpg","wb")
# f1.write(copy)
# f1.close()
# for i in f:
#     f1.write(i)

# import os
# f4 = open("demo.txt","r")
# # os.remove("demo.txt")
# import os

# if os.path.exists("demo1.txt"):
#     os.remove("demo1.txt")
# else:
#     print("File does not exist")

#except:
    #this will raise the errors
#else:
    #this will execute if there are no errors
#finally:
    #this wil execute regardless the result of try and except

# try:
#     f = open("demo.txt")
#     try:
#         f.write("ABC")
#     except:
#         print("Error in file")
#     finally:
#         f.close()
# except:
#     print("Can't open the file")

# a = 5
# if a < 10:
#     raise Exception("Valus is less than 10")