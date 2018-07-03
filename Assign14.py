f=open("abc.txt","w")
l=[1,2,3]
f.write('“Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds.\n'' Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.\n” That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it.\n “Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy.\n' "They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us.\n"' That’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird')
f.close()

#question 1
print("question 1")
f=open("abc.txt","r")
d=f.readlines()
print(d[-1])

#question 2
print("question 2")
f=open("abc.txt","r")
d=f.readlines()
w=[]
l=[]
for l in d:
        w+=l.split()
for i in w:
        print(i)
        
f.close()

#question3
f=open("abc.txt","r")
d=f.readlines()
f1=open("copy.txt","w")
for i in d:
        f1.write(i)
f.close()
f1.close()

#question 4
x=int(input("enter number of lines you want to enter"))
f=open("y.txt","w")
for i in range(x):
    i=input("enter something")
    f.write(i)

y=int(input("enter number of lines you want to enter"))
f1=open("hello.txt","w")
for j in range(y):
    j=input("enter something")
    f1.write(j)

f=open("y.txt","r")
read=f.readlines()
f1=open("hello.txt","r")
read_1=f1.readlines()

f3=open("copy1.txt","w")
for i in read:
    f3.write(i+"\n")
for j in read_1:
    f3.write(j+"\n")
f.close()
f1.close()
f3.close()

#question 5
x=10
l=[]
f=open("num.txt","w")
for i in range(x):
    i=int(input("enter element"))
    l.append(i)
    l.sort()
    
f.write(str(l))

f=open("num.txt","r")
read=f.readlines()
f1=open("num_copy.txt","w")
f1.write(str(read))
f.close()
f1.close()

    
    
    




