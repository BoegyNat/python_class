import math
import random



# x=5

# # x=x+10

# name = input("Please enter your name: ")
# year = int(input("Please enter your year of birth: "))
# print("My name is ",name)
# old = 2024-year
# print("I am ",old)
# print("I am ",2024-year)




# def calculate_circle_properties(radius):
#     # Calculate circumference
#     circumference = 2 * math.pi * radius
    
#     # Calculate area
#     area = math.pi * (radius ** 2)
    
#     return circumference, area

# print("Welcome to the Circle Calculator!")

# #Get input radius from user
# radius = float(input("Please enter the radius of the circle: "))

# # Calculate circumference and area
# # circumference, area = calculate_circle_properties(radius)
#     # Calculate circumference
# circumference = 2 * math.pi * radius
    
#     # Calculate area
# area = math.pi * (radius ** 2)


# # Display the results
# print(f"The circumference of the circle is: {circumference}")
# print(f"The area of the circle is: {area}")




# fname,lname = input("Enter Your Name : ").split() # สมชาย สมหวัง
# print("Your fullname is ",fname+" "+lname)
# print("Your firstname is ",fname)
# print("Your lastname is ",lname)



# a = 500
# print(f"It is {a:.1000000f} lolololol")


# a =[1,2,3,4,5,6,7,8,9.2,"100",True] #list

# print(type(a))

# print(type(a[10]))

# print(a.append(100))

# print(a)

# print(len(a))

# print(a[len(a)-1])

# x = input().split()

# x[1] = int(x[1])
# x[3] = int(x[3])

# print(x[1]+ x[3])

# x[0] = int (x[0])
# x[0] = bool(x[0])
# x[1] = float(x[1])
# x[2] = int(x[2])

# print(x)

# a = [16, 2, 77, 40,0,"000",0.0, 1,1,1,112071,55,8,2,82]
# 16 40 0.0
# print(a[0:7:3])

# x = input("Input Your numbers: ").split()
# x = [int(i) for i in x]
# y = x[0] + x[len(x)-1]
# print(f"The result of the first number plus the last number is {x[0]} + {x[len(x)-1]} = {y}")
# x.append(y)
# print(f"Your list is {x}")



# x = input("Input Your numbers: ").split()
# x = [int(i) for i in x]
# print(f"min : {min(x)}")
# print(f"max : {max(x)}")
# print(f"sum : {sum(x)}")
# print(f"number of min : {x.count(min(x))}")
# print(f"number of max : {x.count(max(x))}")
# print(f"index of the first min : {x.index(min(x))}")
# print(f"index of the first max : {x.index(max(x))}")
# print(f"average : {sum(x)/len(x)}")
# x.sort()
# print(f"sort list : {x}")
# x.reverse()
# print(f"reverse list : {x}")
# x.remove(max(x))
# print(f"remove max : {x}")

# x= [1,5,2,85,2,8]

# if(x.count(10)!=0):
#     x.remove(10)
# else:
#     print("10 is not in the list")
# print(x)

# cat = {"name" : 'สามสี', "sound": 'meow', "Legs": 4 , "like" : "fish"}



# cat["name"] = "John"
# cat["sound"] = "Box Box"

# print(f"ฉํนมีแมวชื่อ {cat['name']} มันร้อง Box Box มี 4 ขา ชอบกิน steak")

# cat["weight"] = 10
# cat["ลูก"]=5

# print(cat)

# person1 = {"name" : "Atom", "age" : 13, "hieght" : 155, "weight" : 50, "gender" : "female"}
# person2 = {"name" : "Auto", "age" : 11, "hieght" : 150, "weight" : 45, "gender" : "male"}
# person3 = {"name" : "Boegy", "age" : 21, "hieght" : 170, "weight" : 80, "gender" : "male"}

# listOfList = [["Atom", 13, 155, 50, "female"], ["Auto", 11, 150, 45, "male"], ["Boegy", 21, 170, 80, "male"]]
# dictOfList = {
#     "Atom" : [13, 155, 50, "female"], 
#     "Auto" : [11, 150, 45, "male"], 
#     "Boegy" : [21, 170, 80, "male"]
#     }
# listOfDict = [
#     {"name" : "Atom", "age" : 13, "hieght" : 155, "weight" : 50, "gender" : "female"},
#     {"name" : "Auto", "age" : 11, "hieght" : 150, "weight" : 45, "gender" : "male"},
#     {"name" : "Boegy", "age" : 21, "hieght" : 170, "weight" : 80, "gender" : "male"}
#             ]

# print(person1)
# index,value = input("Input index and value : ").split()

# person1[index] = value

# print(person1)

# x= [1,[2],[[8],"win"],5]
# print(x[2][1]) 
# x=[[[[2]]],["win"]]
# print(x[1][0])
# x=[[[[2]]],["WIN"],["w","i","n"],"win"]
# print(x[3])




# y = [[1, 2 ,3] ,[4, 5, 6] ,[7, 8, 9]]
# print(x[0])
# print(x[1])
# print(x[2][0]) #4
# print(x[2][1]) #5
# print(x[2][2][2]) #20
# print(x[2][1])



# person1 = {"name" : "Atom", "age" : 13, "hieght" : 155, "weight" : 50, "gender" : "female" ,"color" : "white"}

# person2 = {"name" : "Auto", "age" : 11, "hieght" : 150, "weight" : 45, "gender" : "male"}

# print(person1["name"])
# print(person2["age"])

# person1["habit"] = "sleep"
# person2["habit"] = "eat"

# print(person1)
# print(person2)

# Heroes = [
#     {"name" : "ไอ้ปื๊ด", "type" : "Melee", "hp" : 165, "atk" : 20},
#     {"name" : "น้องไนซ์",  "type" : "Magician", "hp" : 140, "atk" : 25},
#     {"name" : "พี่หน่วง",  "type" : "Range", "hp" : 120, "atk" : 30},
#     {"name" : "เก่ง พลังช้าง",  "type" : "Defence", "hp" : 300, "atk" : 10}
#             ]



# index, name, type, hp, atk = input("Edit Your Heroes : ").split()

# Heroes[int(index)] = {"name" : name, "type" : type, "hp" : hp, "atk" : atk}

# Heroes[int(index)]["name"] = name

# print(Heroes)

# a = [[8, [3, 9], 100], 150, "win", [[[[8, [9]]]]]]
# print(a[a.index("win")])


# age = int(input("How old are you? "))
# if age<13 :
#     print("ได้เล่นผาเทียมแบบที่ 1")
# else :
#     print("ได้เล่นผาเทียมแบบที่ 2")
# print("ได้น้ำดื่ม")
# print("จ่ายตัง")

# buy = input("Do you want to buy (yes or no) : ")
# if buy == "yes" :
#     print("รวย")
# else :
#     print("ออม")
# print("ทำงานต่อ")

# money = 100
# lottery = input("Do you win (yes or no) : ")
# if lottery == "yes" :
#     print("รวย")
#     money += 1000000
# print(f"คุณมีเงินเหลือ {money} บาท")


# money = 100
# buy = input("Do you want to buy (yes or no) : ")
# if buy == "yes" :
#     money -= 100
#     choose = int(input("Choose Number (1-10) : "))
#     reward = random.randrange(1,10)
#     print(f"Reward is {reward}")
#     if choose == reward :
#         print("รวย")
#         money += 1000000
# else :
#     print("ออม")

# print(f"คุณมีเงินเหลือ {money} บาท")

# myUser = {"username" : "admin", "password" : "admin123"}
# username = input("Username : ")
# password = input("Password : ")
# if myUser["username"] == username :
#     if myUser["password"] == password :
#         print("Login Success")
#     else :
#         print("Password Incorrect")
# else :
#     print("Username Incorrect")

# choose = int(input("What service do you want (1:Deposit money, 2:Withdraw money) : "))
# myMoney = 1000
# if choose == 1 :
#     print("Deposit money")
#     money = int(input("How much money do you want to deposit : "))
#     if money > 0 :
#         myMoney += money
#         print("Deposit Success")
#     else :
#         print("Deposit Failed")
# else :
#     print("Withdraw money")
#     money = int(input("How much money do you want to withdraw : "))
#     if money > 0 and money <= myMoney :
#         myMoney -= money
#         print("Withdraw Success")
#     else :
#         print("Withdraw Failed")
# print(f"You have {myMoney} bath")








# heros =[
#     {"name" : "ไอ้ปื๊ด", "type" : "Melee", "hp" : 165, "atk" : 20},
#     {"name" : "น้องไนซ์",  "type" : "Magician", "hp" : 140, "atk" : 25},
#     ]
# print("ตัวละครของคุณทั้งหมดคือ")
# print(heros)

# mode = int(input("เลือกโหมดที่ต้องการ (1:Add , 2:Delete) : "))
# if mode == 1 :
#     print("เพิ่ม heros")
#     index, name, type, hp, atk = input("Add Your Heroes : ").split()
#     heros.append({"name" : name, "type" : type, "hp" : hp, "atk" : atk})
# elif mode == 2 :
#     print("ลบ heros")
#     index = int(input("ลบที่ index ที่เท่าไหร่ : "))
#     if 0 <= index < len(heros) :
#         heros.pop(index)
#     else :
#         print("index ไม่ถูกต้อง")
# else :
#     print("โหมดที่เลือกไม่ถูกต้อง")


# เลือกโหมดที่คุณต้องการ(1:Add , 2:Delete) 2
# 1:Add heros
# เพิ่ม heros
# # index, name, type, hp, atk = input("Add Your Heroes : ").split()
# 2:Delete heros
# # index = int(input("ลบที่ index ที่เท่าไหร่ : "))
# ex: ลบที่ index ที่เท่าไหร่ 1
# ต้องเช็คindex ด้วย ว่ามีจริงไหม


# import random

# # คอมพิวเตอร์สุ่มตัวเลขระหว่าง 1 ถึง 10
# secret_number = random.randint(1, 10)
# guess = None

# print("ยินดีต้อนรับเข้าสู่เกมทายเลข!")
# print("คอมพิวเตอร์ได้สุ่มเลขระหว่าง 1 ถึง 10 ไว้แล้ว")
# print("ลองทายดูว่าคือเลขอะไร")

# # ใช้ while-loop เพื่อให้ทายจนกว่าจะถูกต้อง
# while guess != secret_number:
#     guess = int(input("ทายเลขของคุณ: "))
     
#     if guess < secret_number:
#         print("เลขที่ทายต่ำไป! ลองทายใหม่อีกครั้ง")
#     elif guess > secret_number:
#         print("เลขที่ทายสูงไป! ลองทายใหม่อีกครั้ง")
#     else:
#         print("ยินดีด้วย! คุณทายถูกต้องแล้ว!")







# import random

# atom = 0
# auto = 0

# while atom < 3 and auto < 3 :
#     guess = random.randint(0, 1)
#     print("guess",guess)
#     if guess == 0 :
#         atom += 1
#     else :
#         auto += 1
#     print("atom = ",atom," / auto = ",auto)




# x = int(input("input number 20-1"))
# while x >= 0 :
#       x = x - 2
#       print(x)      



# word = input("Insert your word: ")
# round = int(input("Insert round: "))
# i = 0
# while i < round:
#     print(word)
#     i+=1

# n = 20
# i = 0
# while i < n :
#     print("anything...")
#     i+=1

# j = 1
# for i in range(10):
#     if 10 % j == 0:
#         j+=1
#     print(f"loading... {j}%")

# print(range(5,10))

# for i in range(100,-101,-1):
#     print(i)


# n =  int(input("Input Your numbers: "))
# for i in range(n,-1,-2):
#     print(i,end=" ")


# w = input("input word")
# YOU = int(input("Input any num"))
# for i in range(YOU,0,-1):
#     print(w)
# for i in range(0,10):
#     print(w)


# for i in range(-8,-102,-2):
#     print(i)






# i = 10
# while i <= 10000:
#    print(i)
#    digit = 0
#    it = i
#    while it >= 10:
#         it = it * 0.1
#         digit += 1
#    i = i + (10**digit)


# digit= 0
# for i in range(10,1000,10**digit):
#     print(i)
#     digit = 0
#     it = i
#     while it >= 10:
#         it = it * 0.1
#         digit += 1


# x = int(input("insert number of num: "))
# sum = 0
# for i in range(x):
#     num = int(input(f"num{i+1}: "))
#     sum += num
# print(f"Ans: {sum}")

# w1 = input("Insert word1: ")
# w2 = input("Insert word2: ")
# n = int(input("insert number of word: "))
# for i in range(n):
#     if i % 2 == 0:
#         print(w1)
#     else:
#         print(w2)

# import random

# play = input("do u want to play rock paper scissor (yes or no) ")
# while play == "yes":
#     score_player = 0
#     score_bot = 0
#     for i in range(3):
#         print("round", i + 1)
#         player = input("player: ")
#         bot = random.randint(1, 3)
#         if bot == 1:
#             bot = "r"
#         elif bot == 2:
#             bot = "p"
#         else:
#             bot = "s"
#         print("bot:", bot)
#         if player == "r" and bot == "s":
#             score_player += 1
#         elif player == "p" and bot == "s":
#             score_bot += 1
#         elif player == "p" and bot == "r":
#             score_player += 1
#         elif player == "s" and bot == "r":
#             score_bot += 1
#         elif player == "s" and bot == "p":    
#             score_player += 1
#         elif player == "r" and bot == "p":
#             score_bot += 1
#         else:
#             print("Draw!")
#     if score_player > score_bot:
#         print("player win")
#     elif score_player < score_bot:
#         print("bot win")
#     else:
#         print("Draw!")
#     play = input("do u want to play rock paper scissor (yes or no) ")


# list = [1,2,3,4,5]
# fruit = ["apple","banana","cherry","grape","orange"]
# for i in range(len(list)):
#     print(list[i])

# for one in fruit:
#     print(one)

# list_Movie = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "The Lord of the Rings: The Return of the King", "Inception", "The Godfather: Part II", "The Dark Knight Rises", "Interstellar", "The Avengers"]

# Movie list:
# 1: The Shawshank Redemption
# 2: The Godfather
# 3: The Dark Knight
# 4: Pulp Fiction
# 5: The Lord of the Rings: The Return of the King
# 6: Inception
# 7: The Godfather: Part II
# 8: The Dark Knight Rises
# 9: Interstellar
# 10: The Avengers

# What do you want to watch? (1-10): 1

# Here is the ticket for The Shawshank Redemption.


# print("Movie list:")
# for i in range(len(list_Movie)):
#     print(f"{i+1}: {list_Movie[i]}")

# choose = int(input("What do you want to watch? (1-10): "))
# print(f"Here is the ticket for {list_Movie[choose-1]}")

# list_movie = []
# Movie = int(input("How many movie do you want to add? "))
# for i in range (Movie) :
#     M = (input(f"{i+1}. "))
#     list_movie.append(M)
# print(f'Movies {list_movie}')

# print("Movie list:")
# for i in range(len(list_movie)):
#     print(f"{i+1}: {list_movie[i]}")
# choose = int(input("What do you want to watch? (1-10): "))
# print(f"Here is the ticket for {list_movie[choose-1]}")


# for i in range(5):
#     for j in range(5):
#         if(i%2==0):
#             if(j%2==0):
#                 print("*",end=" ")
#             else:
#                 print("-",end=" ")
#         else:
#             if(j%2!=0):
#                 print("*",end=" ")
#             else:
#                 print("-",end=" ")
#     print()

# for i in range(5):
#     for j in range(5):
#         if i==0:
#             print("-",end=" ")
#         elif j==0:
#             print("-",end=" ")
#         elif i==4:
#             print("-",end=" ")
#         elif j==4:
#             print("-",end=" ") 
#         else:
#             print("*",end=" ")
#     print()

# for i in range(5):
#     for j in range(5):
#         if i==0 or i==4 or j==0 or j==4:
#             print("-",end=" ")
#         else:
#             print("*",end=" ")
#     print()

# for i in range(5):
#     for j in range(5):
#         if i==0 or i==4 or j==0 or j==4 or i==j:
#             print("-",end=" ")
#         else:
#             print("*",end=" ")
#     print()

# for i in range(5):
#     for j in range(5):
#         if i!=0 and j!=4 and i<=j:
#             print("-",end=" ")
#         else:
#             print("*",end=" ")
#     print()

# for i in range(5):
#     for j in range(5):
#         if i==j or i+j==4:
#             print("-",end=" ")
#         else:
#             print("*",end=" ")
#     print()

# for i in range(5):
#     for j in range(5):
#         if (i==j or i+j==4) and (i!=4 and j!=4 and i!=0 and j!=0):
#             print("-",end=" ")
#         else:
#             print("*",end=" ")
#     print()

# for i in range(5):
#     for j in range(5):
#         if (i==j or i+j==4 or i==0 or i==4 or j==0 or j==4):
#             print("*",end=" ")
#         else:
#             print("-",end=" ")
#     print()

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# rows = 5
# for i in range(rows, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# rows=10
# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#         if j == i:
#             break
#     print()



# rows = 5
# for i in range(rows):
#     for j in range(rows):
#         if -j+2>=-i and j>=-i+2 and j<=-i+6 and -j-2<=-i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# rows = 11
# for i in range(rows):
#     for j in range(rows):
#         if -j+5>=-i and j>=-i+5 and j<=-i+15 and -j-5<=-i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# for i in range(10):
#     for j in range(10):
#         if j+i==9:
#             break
#         print(i, end=" ")
#     print()

# a = 10
# while a < 20:
#    a += 1
#    if a%10== 0:
#       continue
#    print("value of a:", a)


# xo=[[" "," "," "],[" "," "," "],[" "," "," "],]

# for i in range(3):
#     for j in range(3):
#         print("|" ,end=" ")
#         print(xo[i][j], end=" ")
#         print("|")
#     print("- - - - - -")
# print()


# xo=[[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],]


# while True:
    
#     for i in range(3):
#         for j in range(3):
#             print(xo[i][j], end=" ")
#         print()
#     ans1,ans2 =input("draw :").split(" ")
    

#     xo[int(ans1)][int(ans2)]="X"


# x=1
# while x<10:
#   x-=1
#   print(x)
# print('exit-loop')


# width = int(input("Enter the width: "))
# height = int(input("Enter the height: "))

# for i in range(height):
#     for j in range(width):
#         if i == 0 or i == height - 1:
#             print("-", end=" ")
#         elif j == 0 or j == width - 1:
#             print("|", end=" ")
#         else:
#             print("*", end=" ")
#     print()

# map=[]
# print("  ", end="")
# for i in range(width):
#     print(f"{i}", end=" ")
# print()
# print("- " * (width+2))
# for i in range(height):
#     map.append([])
#     for j in range(width):
#         if j == 0 :
#             print("|", end=" ")
#         print("*", end=" ")
#         map[i].append("*")
#         if j == width - 1:
#             print("|", end=" ")
#     print()
# print("- " * (width+2))

# print("<-------------------------------------->")


# while True:
#   pos = input("Enter the position: ").split(" ")
#   if pos[0] == "exit":
#     break
#   pos = [int(pos[0]), int(pos[1])]
#   map[pos[0]][pos[1]] = "X"

#   print("- " * (width+2))
#   for i in range(height):
#       for j in range(width):
#           if j == 0 :
#               print("|", end=" ")
#           print(map[i][j], end=" ")
#           if j == width - 1:
#               print("|", end=" ")
#       print()
#   print("- " * (width+2))
  


# x = [3,2,1,58,5,8,10,8,9,33,2,1,58,5,8,10,8,9,33,2,1,58,5,8,10,8,9,33,2,1,58,5,8,10,8,9,33,2,1,58,5,8,10,8,9,33,2,1,58,5,8,10,8,9,33,2,1,58,5,8,10,8,9,3]


# sum = 0
# for i in x:
#     sum+=i
# print(sum)

# max = 0
# for i in x:
#     if i > max:
#         max = i
# print(max)

# print(max(x))

# score = int(input("Input Your score: "))
# grade = ""
# match score:
#     case s if s >= 80:
#         grade = "A"
#     case s if s >= 70:
#         grade = "B"
#     case s if s >= 60:
#         grade = "C"
#     case s if s >= 50:
#         grade = "D"
#     case _:
#         grade = "F"
# print(f"Your grade is {grade}")


# def EvenOrOdd(x):
#     if x % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# EvenOrOdd(15)

# def บวกเลข(x,y):
#     return x+y    

# x = บวกเลข(2,3)+100*80
# print(x)

# def X():
#     x=20
#     y=30
#     z=x+y
#     return x,y,z

# def printX():
#     x,y,z = X()
#     print(f"in x = {x}") 
#     print(f"in y = {y}") 
#     print(f"in z = {z}")


# x = 1
# print(f"out x = {x}") 
# printX()

# def sumAndAvg(x,y,z):
#     sum = x+y+z
#     avg = sum / 3
#     return sum,avg



# total, mean = sumAndAvg(15, 20, 30)
# print(f"Sum: {total}, Average: {mean:.2f}")

# def printLine(sym,count):
#     for i in range(count):
#         print(sym, end="")
#     print()


# printLine("=", 30)
# print("Hello, My name is Atom & Auto")
# printLine("-", 30)

# Student = {
#     "John Wick":{"Math":50, "Science": 85,},
#     "Jackie Chan":{"Figthing":100, "Math": 25}
#     }


# def add_student(name):
#     Student[name] = {}

# def add_subject(name,subject,score):
#     Student[name][subject] = score

print("hello world")
print("hello world")

# add_student("Atom")
# add_subject("Atom","Math",50)
# add_subject("Atom","Science",85)

# add_student("Auto")
# add_subject("Auto","Figthing",100)
# add_subject("Auto","Math",25)

# print(Student)

for i in range(1, 76):
    print(f'@JsonProperty("orderTypeName{i}")\nprivate String orderTypeName{i};\n@JsonProperty("total{i}")\nprivate Double total{i};\n@JsonProperty("tax{i}")\nprivate Double tax{i};\n')