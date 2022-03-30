#EVEN
#for Even number
for number in range (1,21):
    if number  % 2 == 0:
        print(number)
#For Even
for number1 in range (1,51):
    if number1 %2==0:
       print(number1)
#---------------------------------------------------------------------------------------
#REVERSE STRING WITHOUT USING INBUILT FUNCTION
S= "sudarshan Rajendra Kulawade"
print(S[::-1])
print(len(S))

#----------------------------------------------------------------------------------------

#Without Using inbuilt Function Tell the legth Of the following
x2="Computer Programming"
count=0
for Number in x2:
    count=count+1
    print(count)
#inbuilt dunction
print(len(x2))
#----------------------------------------------------------------------------------------
#remove space without using inbuilt function
x2="Computer Programming"
print(x2.replace(" ",""))
#-----------------------------------------------------------------------------------------
#convert Y4 Into TUPLE
Y=[2,4,6,7,[5,8,9]]
Y[4]=(5,8,9)
print(Y)
#------------------------------------------------------------------------------------------
#print only integrs from the list
z1=[12,34,"netra",7,"pune",343,"nashik"]
for element in z1:
    if type (element) == int:
        print(element)
#-----------------------------------------------------------------------------------------
#Write a program to find sum of elements in the lsit

z2=[12,22,34,5,1]
sum=0
for number2 in z2:
    sum= number2+sum
print(sum)

#-------------------------------------------------------------------------------------------
#Find and display the largest number of a list without using built-in function max().
# Your program should ask the user to input values in list from keyboard.

#Source Code

mylist = []
size = int(input('How many elements you want to enter? '))

print('Enter',str(size),'positive numbers')

for i in range(size):
    data = int(input())
    mylist.append(data)

max = 0
for data in mylist:
    if data > max:
        max = data

print('The largest number in list is', max)

#---------------------------------------------------------------------------------------

#How to print maximum Number without usinginbuilt function

Z1=(88,3,2,1,6)
maxnum=0
for number in Z1:
   if number > (maxnum):
     maxnum=number
     print(maxnum)
#---------------------------------------------------------------------------------------

#For multiplication using for loop


total=1
for element in Z1:
    total=total*element
    print(total)

#-------------------------------------------------------------------------------------------

#print only integrs from the list
z1=[12,34,"netra",7,"pune",343,"nashik"]
for element in z1:
    if type (element) != int :
        print(element)
#----------------------------------------------------------------------------------------------
#PRINT MAXIMUN NUMBER FROM THE STRING
X1=[22,45,455,665,454,2,35,54]
total=0
for element in X1:
    if element > total:
        total=element
print(total)  #665

B1=[1,2,3,6,5,89,9,5,]
max=0
for element  in B1 :
    if element > max:
        max=element
print(max)   #89


K=("Karan Kamble")
print (K[::-1])

#-------------------------------------------------------------------------------------------------------

# check Palindrome check
k = "madam"
k1 = k[::-1]
if (k==k1):
    print("given string is palindrome")
else:
    print("given string is not palindrome")

S1="BunuB"
S=S1[::-1]
if (S==S1):
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")

#------------------------------------------------------------------------------------------------


#write the python program to find how many uppercase and lowercase letters are in the string
k3 = "I live in Pune and Pune is a Great city."
upper=0
lower=0
for letter in k3:
    if letter.isupper():
        upper=upper+1
    elif letter.islower():
        lower=lower+1
else:
    pass
print(f"The number of lowercase letter {lower}") #using F string we use curly braces
print(f"The number of uppercase letter {upper}")
print("The number of uppercase letter" ,upper)#without Using Curly brace
#---------------------------------------------------------------------------------------------------------



#Wothout Using Inbuilt function count lenght of the following string

x2="Computer Programming"
count=0
for Number in x2:
    count=count+1
    print(count)

#Using Inbuilt FUnction
print(len(x2))

#---------------------------------------------------------------------------------------------------
#write python program to check whether the given string is pangram or not
alphabate = "abcdefghijklmnopqrstuvwxyz"
k4 = "The quick brown fox jumps over the lazy dog "
for letter in alphabate:
    if letter not in k4.lower():
        print("The string is not a pangram")
print("The string is a pangram")

alphabate= "abcdefghijklmnopqrstuvwxyz"
S1="dog lazy the over jumps fox brown quick the"

for letter in alphabate:
    if letter not in S1.lower():
        print("the string is not a pangram")

print("the string is pangram") #If we use else then it will print ="26 "time the the print Statement thats why
#we came outside the loop and print( the statement we want)
#-------------------------------------------------------------------------------------------------------------------
#write the python program how many times each letter appears in the string
k5 = "Pune is well-known for historical reason"
d = {}
for letter in k5:
    if letter not in d.keys():
        d[letter]=1
    else:
        d[letter]=+1
print(d)

#add all elements in the list & give total
x3 = [2,45,21,6,7,8,12]
sum=0
for num in x3:
    sum=sum+num
print(sum)


S="sudarshan rajendra kulawade"
print(S.title())
S1=S[0:10]
print(S1)
print(S1.upper())

k=S.replace(" ","")
print(k)

w=(S[19:27])
print(w.upper())

R=S[::-1]
print(R)

print(S.isalpha())
print(S.isalnum())
print(S.isdigit())
print(S.isnumeric())
print(S.islower())
print(S.isupper())
print(S.istitle())

print(S.join(R))

#12.join()
#it will join the list of words and make a whole string
d='pune is historical city'
#print(d.split())
x=d.split()
print(x)
print(" ".join(x))
print("@".join(x))
print("#".join(x))

#13.strip()
#it will remove the whitespace around the string but
# not inside the string
b="  Python and Javascript are in demand currently"
print(b)
print(b.strip()) #default strip will be space

t1="....hello........???"
print(t1)
print(t1.strip(".?"))

t3=",,,,,,,,,hello,,,,,,"
print(t3.lstrip(','))
print(t3.rstrip(','))
print(t3.strip(","))


d3="my mail id is hello@gmail.com"
print(d3.split())
print(d3.split("@"))







