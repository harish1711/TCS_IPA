class Employee():
    def __init__(self,eid,ename,dept,age,promotion=None):
        self.eid=eid
        self.ename=ename
        self.dept=dept
        self.age=age
        self.promotion=promotion
#then create another class Organization with instance input as elist or employee list
class Organization():
    def __init__(self,elist):
        self.elist=elist
#then create a method for validating the promotion with 2 list as input
    def validate(self,li1,li2):
        #create a list for saving the values
        org=[]
        for i in self.elist:
            for j in range(3):#i took range as 3 here ill tell you all later about it
                if i.dept == li1[j]:
                    if i.age==li2[j]:
                        org.append((i.eid,"eligible"))
                    elif i.age>li2[j]:
                        org.append((i.eid,"overdue"))
                    elif i.age<li2[j]:
                        re=li2[j]-i.age
                        org.append((i.eid,str(re)+" years left"))
        return org
#now create a main function to give inputs
if __name__=="__main__":
    n=int(input())
    elist=[]
    for i in range(n):
        eid=int(input())
        ename=input()
        dept=input()
        age=int(input())
        emp=Employee(eid,ename,dept,age)#here there is noo needd to pass promotion details since it can bee null
        elist.append(emp)
    li1=[]
    li2=[]
    #the TCS mentioned us to give as obj but here i passed as list ans it had a range of 3 so that i gave 3 as range in above
    for i in range(3):
        a=input()#dept input
        b=int(input())#are required to validate
        li1.append(a)
        li2.append(b)
    org=Organization(elist)
    rslt=org.validate(li1,li2)
    if rslt:
        for i in rslt:
            print(i[0]," ",i[1])
# i have input for the code so i will try it
# i got the output for this code
#And guys if u ask if will clr the test NAHH i messed up there and i didnt get output since i had no time :(
# I have added the code link in the description link you all can access it guys and ALL the best for the next IPA test..:)
#Thank you for watching

#inputs
# 4
# 001
# rick
# accounts
# 4
# 002
# martin
# science
# 2
# 003
# sam
# development
# 4
# 004
# ram
# accounts
# 2
# accounts
# 3
# science
# 2
# development
# 2

