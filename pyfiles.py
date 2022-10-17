'''import os as o
p="C:\\Users\\HP\\OneDrive\\Desktop\\work.webdevs"
if o.path.exists(p):
    print("hey!it exists:)")
    if o.path.isfile(p):
        print("it is a file")
    if o.path.isdir(p):
        print("it is directory")
else:
    print("no")
------------------------------------------------
'''

'''

p="C:\\Users\\HP\\OneDrive\\Desktop\\docs.txt"
with open(p) as f:
    print(f.read())
print(f.closed)

---------------------------- '''
'''
p="C:\\Users\\HP\\OneDrive\\Desktop\\hero.txt"
t="i hope u rocked the code .heroo...!!"
with open(p,"a") as f:
    f.write(t)
print(f.closed)
--------------------------------------'''
'''
import shutil as s
import os as o
 
src="C:\\Users\\HP\\OneDrive\\Desktop\\hero.txt"
dst="E:\\exploit\\herodupe.txt"
s.copyfile(src,dst)
if o.path.exists(dst):
    print("file is sucessfully copied")

------------------------------------------------'''

'''
import os as o

src="C:\\Users\\HP\\OneDrive\\Desktop\\Human.txt"
dst="C:\\Users\\HP\\OneDrive\\Desktop\\Human_Being.txt"

o.replace(src,dst)  --> used for renaming.

# moving a file:-
src="C:\\Users\\HP\\OneDrive\\Desktop\\Human_Being.txt"
dst="C:\\Users\\Public\\for_demo\\hb1"

o.replace(src,dst)


--------------------------------------------------'''
'''
import os as o
import shutil as s

fp="C:\\Users\\HP\\OneDrive\\Desktop\\stdir"
try:
    s.rmtree(fp)
except FileNotFoundError:
    print("the given file is not there")
except OSError:
    print("folder is not empty:)")
finally:
    print("hey,lets fuck!")

-------------------------------------------'''
'''
#print(help("modules"))

import random as r

pag=True

while pag:
    print("welcome! to the rock paper and scissors game:)\n")

    chuse=["rock","paper","scisors"]

    p=None
    c=r.choice(chuse)
    while p not in chuse:
        p=input("select rock,paper,scissors\n").lower()
        if p==c:
            print(f"computer:{c}")
            print(f"player:{p}")
            print("Tie!")
        elif p=="rock":
            if c=="paper":
                print(f"computer:{c}")
                print(f"player:{p}")
                print("you loose:(")

            if c=="scisors":
                print(f"computer:{c}")
                print(f"player:{p}")
                print("you win:)")


        elif p=="paper":
            if c=="scisors":
                print(f"computer:{c}")
                print(f"player:{p}")
                print("you loose:(")

            if c=="rock":
                print(f"computer:{c}")
                print(f"player:{p}")
                print("you win:)")

        elif p=="scisors":
            if c=="rock":
                print(f"computer:{c}")
                print(f"player:{p}")
                print("you loose:(")

            if c=="paper":
                print(f"computer:{c}")
                print(f"player:{p}")
                print("you win:)")
    pag=input("to play again press y else n\n").lower()
    if pag!="y":
        pag=False
print("bye..!")

-----------------------------------------------------------------------
-----------------------------------------------------------------------'''

'''
print("welcome to quiz!")

qstns={
     "fav hero":"c",
     "fav actress":"b",
     "fav color":"c",
     "lover":"b",
      
    }
options =[["a.ram","b.nani","c.prabhas"],
          ["a.rakul","b.keerthi","c.sonali"],
          ["a.red","b.green","c.blue"],
          ["a.bhav","b.joshna","c.manvi"],
          ]
# -------------------------------------

def check_answers(real_answer,guessed):
    if real_answer==guessed:
        print("correct!")
        return 1
    else:
        print("wrong!")
        return 0

#-------------------------------

def score(cgss,gsa):
    # cgsa = correct guesses (it is a number),gsa =guesses it is a list
    print("-----------------------")
    print("results")
    print("-----------------------")
    print()
    print("answers : ",end="")
    for an in qstns:
        print(qstns.get(an),end=" ")
    print()
    print("guessed_answers : ",end="")
    for i in gsa:
        print(i,end=" ")

    print()
    ts=int((cgss/len(qstns))*100)     #ts=total score
    print(f"your score :{ts}%")
    

#-------------------------------



def new_game():
    qno=1
    cgs=0           #correct guesses
    gs=[]            #guesses
    for key in qstns:
        print("--------------------------")
        print(qno,end=")")
        print(key)
        print()
        for i in options[qno-1]:
            print(i)
        print()
        guess=input("enter (a,b,c) : ").lower()
        gs.append(guess)

        # now sending the guessed answer and correct answer to
        # to the check_answer function.

        cgs+=check_answers(qstns.get(key),guess)
        
        
        qno+=1

    # now invoking score function

    score(cgs,gs)


        
        
new_game()

#-------------------------------
def play_again():
    intrest=input("do u want to play again(yes/no) : ").lower()
    if intrest=="yes":
        return True
    else:
        return False

while play_again():
    new_game()
print("Byeee!:)")

'''
#----------------------------------------------------------------------
                     #object oriented programming :)
#-----------------------------------------------------------------------

''' --------------------------------------------------------
#from car import Cars
from car import *


c1=Cars("tesla",2024,"15cr",500)
c2=Cars("ford",2023,"10cr",190)

#c1.drive()
#c1.instruct()
print(c1.wheels)
print(Cars.wheels)
print("after chanching for an object")
#c1.wheels=10
print("it is not a car :) " ,c1.wheels)

print("after changing the entire class variable:")
Cars.wheels=5
print(c2.wheels)
print(c1.wheels) 

------------------------------------------------------------'''

#----------------------------------------------------------
             #inheritence
#----------------------------------------------------------

'''
#single inheritence:

class Animal:

    def __init__(self,name):
        self.name=name

    alive=True

    def eat(self):
        print(f"the {self.name} is eating")

    def roaming(self):
        print(f"the {self.name} is roaming")

class Rabbit(Animal):

    def run(self):
        print("the rabbit is running")

class Cow(Animal):

    def graze(self):
        print("the cow is grazing")

rab=Rabbit("rabbit")
rab.eat()

cow=Cow("cows")
cow.eat()
cow.graze()
rab.run()

'''

'''
               #----------------------------------

                   #multi level inheritence:-

               #-----------------------------------

# it means an child class(grand child) inherits from an another
# child class(dad) {main parent is grand pa:) } is called an m.l.i

class Organism:
    

    alive =True

    def __init__(self,name):
        self.name=name

    def bg(self,certified_by):
        print(f"{self.name} belong to organism by {certified_by}")

class Animal(Organism):

    def eat(self):
        print(f"the {self.name} is eating")

class Dog(Animal):
    heo=20
    def looks(self,face):
        #self.cface = face --> ila ina or direct ina same .
        print(f"the dog {face} looks cute")


dog =Dog("Doggy")
niky = Dog('dobor')
#niky.looks('silky')
#dog.looks("round_face")
dog.bg("darwin")
niky.bg("kon")
   
'''


'''
         #------------------------------------------
                 #multiple inheritence
         #------------------------------------------


class prey:
    def flee(self):
        print("the animal is fear")

class predator:
    def hunt(self):
        print("the animal is hunting")

class fish(prey,predator):
    def both(self):
        print("hey! iam inheriting both")

f=fish()
f.flee()
f.hunt()

'''


'''
         #------------------------------------------
                 #method overriding
         #------------------------------------------

class colage:
    def teach(self):
        print("teacher is teaching")

class frnd(colage):
    
    def teach(self):
        print("frnd explain in better")

fr=frnd()
fr.teach()
    
'''


'''
         #------------------------------------------
                 #method chaining
         #------------------------------------------

class Car:
     def turn_on(self):
         print("the car is turn on")
         return self

     def drive(self):
         print("the car is driving")
         return self

     def break_on(self):
         print("you pressed the car breaks")
         return self

     def turn_off(self):
         print("the car is turn off")
         return self

car=Car()
car.turn_on().drive().break_on().turn_off()

# self is required to return at the end of each method to continue method chaining.

#to be more redable:-
#the \ is a line continution character

car.turn_on()\
.drive()\
.break_on()\
.turn_off()

'''

'''

#            ---------------------------
                        # super()
#            ----------------------------


class Common_dimension:

    def __init__(self,w,l):
        self.w=w
        self.l=l

class Square(Common_dimension):

    def __init__(self,wid,ln):
        super().__init__(wid,ln)

    def area(self):
        return self.w*self.l

class Cube(Common_dimension):

    def __init__(self,wid,ln,hgt):
        super().__init__(wid,ln)
        self.hgt=hgt

    def vol(self):
        return self.w*self.l*self.hgt

sq=Square(5,5)
cb=Cube(7,7,7)
print(sq.area())
print(cb.vol())

    '''

'''

                        #ABSTRACT CLASS

from abc import ABC,abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("the car is going")

class Bike(Vehicle):
    def go(self):
        print("the bike is riding")

#vh=Vehicle()
cr=Car()
cr.go()
bk=Bike()
bk.go()

    '''


'''
                          #PASSING OBJECT AS AN ARGUMENT

class Car:
    color=None

def change_color(car,clr):
    car.color=clr

cr1=Car()
cr2=Car()
cr3=Car()

change_color(cr1,"crimson")
change_color(cr2,"green")
change_color(cr3,"blue")

print(cr1.color)
print(cr2.color)
print(cr3.color)

'''

'''


                    #DUCK TYPING

class Duck:
    def walk(self):
        print("the duck walking")
    def talk(self):
        print("the duck quacking")
class Chicken:
    def walk(self):
        print("the chick is walking")
    def talk(self):
        print("the chick is chucking")

class Person:
    def catch(self,dk):
        dk.walk()
        dk.talk()
        print("hey u catched")
#duk=Chicken()
#duk.walk()

chk=Chicken()
pr=Person()
pr.catch(chk)

'''

                                #WALRUS OPERATOR

#print(hero:=True)
#print(power:="powerful people comes from powerful places")

#general way without walrus:-

'''
foods=[]

while True:
    food=input("u r req ")
    if food=="quit":
        break
    foods.append(food)

print(foods)
    '''

#now same above program using walrus operator:-

'''
foods=[]

while ((food:=input("u r req "))!="quits"):
    foods.append(food)

print(foods)
'''

'''

                    #FUNCTION TO A VARIABLE/CREATING ALIAS TO A FUNCTION

def iam():
    print("hey!got it")

#iam()
nen=iam
#nen()

say=print
say("hello guru premakosame :)")
say(nen)
say(iam)

'''



                #HIGHER ORDER FUNCTIONS
'''

#let us see function accepting function accepting function as an argument.

def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()

def voice(func,word):
    print(func(word))


voice(loud,"now i speek loud")
voice(quiet,"now i speak quiet")

'''

'''

#now,let us see function returning a function

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide=divisor(5)

print(divide(10))

'''

                   #LAMBDA FUNCTION
'''

#without lambda in normal way

def quadexpval(x):
    return x*x+2*x+5
print(quadexpval(2))

#now doing the same task using lambda function

quadexpval = lambda x:x*x+2*x+5

print(quadexpval(2))



ag_chk=lambda ag:"eligible to fuck" if ag>=18 else "wait for some years"
print(ag_chk(2))

'''

                    #SORTING OF ITERABELS
'''

list=["hero","villan","game","nice","happy"]
list.sort(reverse=True)
print(list)

sorted_list=sorted(list,reverse=True)
print(sorted_list)


#LEVEL-2:-


tup=("hero","villan","game","nice","happy")
list2=sorted(tup)
print(list2,type(list2))



students=[
    ("hemanth",'a',18),
    ("bhav",'b',19),
    ("keerthi",'c',16),
    ]

gr=lambda gs:gs[2]
sorted_students=sorted(students,key=gr)
print(sorted_students)


students={
    'B':("hemanth",'a',18),
    'R':("bhav",'b',19),
    'O':("keerthi",'c',16),
    }

#print(students)

#ssl={k:v for k,v in sorted(students.items())}

# --> sorted(students.items() ==> gives list of tuples.
  EX:-[('B', ('hemanth', 'a', 18)), ('O', ('keerthi', 'c', 16)), ('R', ('bhav', 'b', 19))]
 
#print(ssl)
#print(type(ssl[0]))

ag=lambda st:st[1][0]

print("sorted students in the form of list of tuples")
ssl=sorted(students.items(),key=ag)
print(ssl)

#updated version
print("after sorted as per the key again transforming into the dictionary form.")
ssd={k:v for k,v in sorted(students.items(),key=ag)}
print(ssd)

#sorting a string:-

s="hemanth"
sn=sorted(s)
kk=""
for i in sn:
    kk=kk+i
print(kk)

'''

'''
                   #MAP FUNCTION

store=[
    ("shirt",2500),
    ("pant",4000),
    ("t-shirt",1500)
    ]
to_dolor=lambda data:(data[0],data[1]/100)
def to_dolor(data_tup):
    return (data_tup[0],data_tup[1]/150)

dolor_store=list(map(to_dolor,store))
print(dolor_store)

'''
'''

                         #FILTER FUNCTION

friends=[
    ('kiran',22),
    ('ram',21),
    ('bhav',20),
    ('yash',17)
    ]
ag_chk=lambda frnd_data: frnd_data[1]>=18

drnk_friends=list(filter(ag_chk,friends))
print(drnk_friends) 

'''

                            #REDUCE FUNCTION
'''
import functools as ft

word_letters=['f','r','i','e','n','d','s',]

word_build=lambda x,y:x+y

word_of_letters=ft.reduce(word_build,word_letters)

print(word_of_letters)

#let us create for finding factorial

fct=[1,2,3,4,5,6,7]

fct_find=lambda x,y:x*y

factorial=ft.reduce(fct_find,fct)
print(factorial)
 

'''

'''

#----------------------------------------------------------------
                   #Counter
#-----------------------------------------------------------------

from collections import Counter
l = [1,2,1,3,1,4,3,3,3,2,2,9,10]
cnt = Counter(l)
# EX:-
      print(cnt)
      Counter({3: 4, 1: 3, 2: 3, 4: 1, 9: 1, 10: 1})
      

print(type(cnt))
<class 'collections.Counter'>

print(cnt[3])
4

mc = cnt.most_common(2)
print(mc)
[(3, 4), (1, 3)]
print(type(mc))
<class 'list'>

'''

'''

                             #LIST COMPREHENSION


         
#normal:-    
squares=[]
for i in range(1,11):
    squares.append(i*i)

print(squares)

#lc1:-

suares=[i*i for i in range(1,11)]      
print(squares)

#lc2:-
even_squares=[i*i for i in range(1,11) if i%2==0 ]  
print(even_squares)

#lc3:-

#printing even number as 'e' and odd number as 'o'

writing_even_odd=['e' if i%2==0 else 'o' for i in range(1,11) ]
print(writing_even_odd)

'''
'''

                      #DICTIONARY COMPRESHION
#normal:-
cities_temp_in_f={'tpt':84,'vizag':90,'kurnool':98.4}
print(cities_temp_in_f)

#dc1:-

cities_temp_in_c={ key :round((((val-32)*5)/9)) for (key,val) in cities_temp_in_f.items()}
print(cities_temp_in_c)

#dc2:-

cities_temp_in_c={ key :round((((val-32)*5)/9)) for (key,val) in cities_temp_in_f.items() if val>=90}

print(cities_temp_in_c)

#dc3:-

cities_temp={'tpt':84,'vizag':88,'kurnool':98.4}

discription_cities_temp={key:("warm" if val>85 else "cool" ) for (key,val) in cities_temp.items()}

print(discription_cities_temp)

#dc4:-

def temp_chk(tmp):
    if tmp>90:
        return "v.v.hot"
    elif 90 >= tmp >=85:
        return "hot"
    else:
        return "moderate"

ddt_discription_cities_temp={key: temp_chk(val) for (key,val) in cities_temp.items()}
print(ddt_discription_cities_temp)

'''

                        #ZIP FUNCTION
'''
user_name=['ram','sam','hero','lion',]
password=['ra@134','sa@345','her#456','li@789']
gender=['m','f','m','an']
unpd=zip(gender,zip(user_name,password))
print(type(unpd))
#zip is an object u have to change into an any desirable iterable
#unpds=dict(unpd)
#print(unpds)
#print(list(zip(user_name,password,gender)))
#output:-

#{'m': ('hero', 'her#456'), 'f': ('sam', 'sa@345'), 'an': ('lion', 'li@789')}



user_name=['ram','sam','hero','lion',]
password=['ra@134','sa@345','her#456','li@789']

print(dict(zip(user_name,password)))
#output:-
{'ram': 'ra@134', 'sam': 'sa@345', 'hero': 'her#456', 'lion': 'li@789'}

print(list(zip(user_name,password)))
#output:-
[('ram', 'ra@134'), ('sam', 'sa@345'), ('hero', 'her#456'), ('lion', 'li@789')]

'''


#                         PURPOSE OF
#                   if __name__ = "__main__"


'''
import car as c
#print(__name__)   ==>__main__
#print(c.__name__) ==>car

          
if __name__=="__main__":
    print("running directly")
else:
    print("i think i was run by car")


c.__name__




def hello():
    print("hi,users iam wishing u a hello!")

if __name__=="__main__":
    #hello()
'''



                                 #TIME

#epoch = a date and time from which a computer measure system time(the computer thinks the time begin at
#that moment).==>it takes as reference and it is based on u r os and computer

import time as t
'''

print(t.ctime(0)) ==>Thu Jan  1 05:30:00 1970
print(t.ctime(20000000000)) ==>Tue Oct 11 17:03:20 2603

print(t.time())
print(t.ctime(t.time()))

time_obj=t.localtime()
print(time_obj)
formated_local_time=t.strftime("%D %b %y %H:%M:%S ",time_obj)
print(formated_local_time)



gm_time_obj=t.gmtime()
formated_gm_time=t.strftime("%d %B %Y %H:%M:%S ",gm_time_obj)
print(formated_gm_time)


print(t.strptime("20 April,2022","%d %B,%Y"))




time_tuple = (2022,5,20,5,20,30,6,0,0)
time_string=t.asctime(time_tuple)
print(time_string)

time_in_secs_from_ephoc=t.mktime(time_tuple)
print(time_in_secs_from_ephoc)

time_obj=t.localtime()
time_from_ephoc = t.mktime(time_obj)
print(time_from_ephoc)


'''



                          #ALL ABOUT THREADS

'''
import threading as td
import time as t

def eat(name):
    t.sleep(5)
    print(f"{name} completed eating!\n")
def drink(name):
    t.sleep(7)
    print(f"{name} completed drinking!\n")
def study(name):
    t.sleep(9)
    print(f"{name} completed studying\n")

# normal execution i.e sequentially it takes 15 secs to complete the entire tasks.

eat()
drink()
study()

# now creating threads and executing them simultaneously.

h="hemanth"

x=td.Thread(target=eat,args=(h,))
x.start()

y=td.Thread(target=drink,args=(h,))
y.start()

z=td.Thread(target=study,args=(h,))
z.start()

#synchronising the threads.

x.join()
y.join()
z.join()

print(td.active_count())
print(td.enumerate())          # detailed discription of threads
print(t.perf_counter())

'''
 
                          #DAEMON THREADS:-
'''

import threading as td
import time as t

def timer():
    print()
    print()
    cnt=0
    while True:
        t.sleep(1)
        cnt+=1
        print(f"started in for :{cnt} secs ")

x=td.Thread(target=timer,daemon=True)
x.start()


reply=input("respond to this program to exit :")

'''
 
                             #MULTI PROCESSING
'''
from multiprocessing import Process,cpu_count
import time as t

#print(cpu_count())

def counter(n):
    cnt=0
    while cnt<=n:
        cnt+=1

def main():
    a=Process(target=counter,args=(25,))
    
    b=Process(target=counter,args=(25,))
    
    c=Process(target=counter,args=(25,))
    
    d=Process(target=counter,args=(25,))

    a.start()
    b.start()
    c.start()
    d.start()
    
    


    a.join()
    b.join()
    c.join()
    d.join()

    print(t.perf_counter())

if __name__=="__main__":
    main()

        
'''

# ---------------------------------------------------------------------
                             # GUI

#----------------------------------------------------------------------










'''


# *args

def add(*nums):
    print(type(nums))
    a=list(nums)
    print(sum(a))

#add(1,2,3,4,5,6,7,8,9,10)

def vkwargs(** kwdic):
    print(type(kwdic))
    fn=""
    for k in kwdic:
        fn=fn+kwdic[k]+" "
    print(fn)

vkwargs(fir_name="Hemanth",mid_name="Kumar",Last_name="Reddy")

        
'''

# --------------------------------------------------------------------------
                                # ARRAY
# --------------------------------------------------------------------------


from numpy import *
'''
ar = array([[180,45,45],[0,57,0],[77,90,90]])
br = array([[18,45,45],[1,7,0],[77,9,90]])

#l1=list(map(int,input().strip().split()))
#l2=list(map(int,input().strip().split()))
#l3=list(map(int,input().strip().split()))
#ar = array([l1,l2,l3])
print(ar)
print(br)

#print(mean(ar,axis=1))

#print(median(ar,axis=1))

#print(std(ar,axis=1))
#print(var(ar,axis=1))

#print(average(ar,axis=1))

#print(percentile(ar,10,axis=1))

# set theory operations

#print(unique(ar))
#print(type(unique(ar)))
cr=union1d(ar,br)
print(cr)

'''

ar = array([1,2,3,4,5,7,8,9,0])
#print(ar)
#ar.shape=(3,3)
#print(ar)
#print(ar.shape)
#br= ar.reshape(9,1)

#print(br)


#a =arange(1,101)
#print(a)
#print(type(a))
#a.shape=(4,25)
'''
a=ones(4,dtype=int)
print(a.size)
b=append(a,25.5)
print(b)



a=array((2,3,4,77,7))
b,=where(a==max(a))

#a=linspace(1,100,endpoint=True,num=10,dtype=int,retstep=True)
print(b)
print(type(b))
print(b[0])

'''

#----------------------------------------------------------------------------
                          # PANDAS
#----------------------------------------------------------------------------



import pandas as pd
#from openpyxl.workbook import Workbook

# one way i.e in dictionary key as headings and values as (lists i.e is column)

data={
    'std_roll':[10,20,30,40,50],
    'std_name':['hemanth','kiran','iqbal','rukku','rohith',]
    }
df=pd.DataFrame(data)
'''
print(df.shape)
print(df)
print(df.head(2))
print(df.tail(2))

'''

#print(df[1:3])

#print(df.std_name)
#print(df[['std_name','std_roll']])

#print(df.describe())

#df.set_index('std_roll',inplace=True)


#----------------print(df.loc['std_roll'])---------------

# type-2 of creating a dataframe:-

data2 = [
    (1,'rakul'),
    (2,'ram'),
    (3,),
    (4,'fans')
    ]
df2 = pd.DataFrame(data2,columns=['number','celb_name'])
#print(df2)
#------------------------na_values={'celb_name':['None',1]}
#print(df2)

# type-3 of creating a dataframe:-

data3 = [

    {'rno':2,'name':'ram'},
    {'rno':4,'name':'sram'},
    {'rno':6,'name':'dram'},
    {'rno':8,'name':'fram'},

    ]
df3 = pd.DataFrame(data3)
#print(df3)

#print(df3)
#print(df3)
#print(df)
                        # --------------df.skiprows=1,df.header=3
#print(df)
#print(df[:4])







                        

