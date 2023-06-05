
#super market bill generator
from datetime import datetime
Name=input("Enter your name:")
#items
lists='''
Almonds        Rs-100/kg
oil            Rs-75/liter
wheet flour    Rs-80/kg
Sugar          Rs-28/kg
chilli powder  Rs-90/each
Salt           Rs-30/kg
shampoo        Rs-110/250ml
Bread Brown    Rs-30/each
Eggs           RS-6/each

'''
#declartions
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#dict for items
items={"Almonds":100,"oil":75,"wheet flour":80,"Sugar":28,"chilli powder":90,
"Salt":30,"shampoo":110,"Bread Brown":30,"Eggs":6}

option=int(input("For items press 1:"))
if option==1:
    print(lists)
    
for i in range(len(items)):
    inp1=int(input("To select items press1 or 2 for return:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry invalid input")
    else:
        print("you entered wrong input")
    inp=input("proceed with bill the items yes or no:")
    if inp=="yes":
        pass

        if finalamount!=0:
            print(35*"*","Super Market",35*"*")
            print(37*" ","Guntur")
            print("Name:",Name,42*" ","Date:",datetime.now())
           #print("Bill generated")
            print(84*"*")
            print("SNO",9*" ","ITEMS",2*" ","QUANTITY",6*" ","PRICE")
            for i in range(len(pricelist)):
                print(i,8*" ",3*" ",ilist[i],6*" ",qlist[i],11*" ",plist[i])
            print(84*"*")
            print("TotalAmount:","Rs-",totalprice)
            print("gst amount:","Rs-",gst)
            print(22*"-")
            print("FinalPrice:","Rs-",finalamount)
            print(22*"-")
            print(34*"*","Thanks For Visit",33*"*")

