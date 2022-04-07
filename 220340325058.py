#220340325058 Vishal Khetmalis
#Q.1) Convert given hrs & mins in second
hrs=int(input("Enter the time in hours: "))
min=int(input("Enter the time in minutes: "))
sec=(min*60)+(hrs*3600)
print("Given time in seconds is: ",sec)

#Q.2) Write code to find the average of ‘n’ numbers entered by the user to function avg ( )
def avg(*n):
    count=0
    sum=0
    for i in n:
        sum=sum+i
        count+=1
    average= sum/count
    print("Average of entered numbers is: ",average)
avg(10,20,30,40)

#Q.4) Write a code to accept a number & print in words.
num=int(input("Enter a number: "))
if num

#Q.5) Create class math
class Math:
    def Set_data(self,a,b):
        self.num1=a
        self.num2=b
    def Add(self,n1,n2):
        self.num1=n1
        self.num2=n2
        result=n1+n2
        print("Addition is: ",result)
    def Div(self,n1,n2):
        self.num1=n1
        self.num2=n2
        result=n1//n2
        print("Divisiion is: ",result)
    def Sub(self,n1,n2):
        self.num1=n1
        self.num2=n2
        result=n1-n2
        print("Substraction is: ",result)
    def Mul(self,n1,n2):
        self.num1=n1
        self.num2=n2
        result=n1*n2
        print("Multiplication is: ",result)
o1=Math()
o1.Set_data(15,10)
o1.Add(15,10)
o1.Div(15,10)
o1.Sub(15,10)
o1.Mul(15,10)

#Q.7) Convert Paise in Rupees & Paises
rs=int(input("Enter amount: "))
ps= rs%100
rp=rs//100
print(rs," is ",rp,"Rupees ",ps,"Paise")

#Q.9) Accept String & print only alternate characters on a string.
s=input("Enter a string: ")
print(s[::2])

#Q.10) Create menu driven code for 1) Accept 2 numbers 2) Add 3) Sub 4) Mul 5) Div
while True:
    choice=int(input("Enter \n1) Accept 2 numbers \n2) Add \n3) Sub \n4) Mul \n5) Div \nChoice:"))
    if choice==1:
        n1=int(input("Enter first number: "))
        n2=int(input("Enter second number: "))
    elif choice==2:
        add=n1+n2
        print("Addition is:",add)
    elif choice==3:
        sub=n1-n2
        print("Substraction is:",sub)
    elif choice==4:
        mul=n1*n2
        print("Multiplication is:",mul)
    elif choice==5:
        div=n1//n2
        print("Division is:",div)
    else:
        choice==0
        break
    
